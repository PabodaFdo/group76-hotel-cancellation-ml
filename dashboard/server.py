"""Local-only HTTP server for genuine Random Forest inference. No Flask needed.

Launch from the project root or elsewhere:
    python dashboard/server.py
Then open http://127.0.0.1:8765
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "results" / "final_model" / "random_forest_pipeline.joblib"
METRICS_PATH = ROOT / "results" / "metrics" / "final_random_forest_test_results.csv"
CHART_DIR = ROOT / "results" / "eda"
HOST, PORT = "127.0.0.1", 8765

NUMERICAL = {
    "lead_time": (0, 1000),
    "stays_in_weekend_nights": (0, 60),
    "stays_in_week_nights": (0, 70),
    "adults": (0, 60),
    "children": (0, 20),
    "babies": (0, 20),
    "is_repeated_guest": (0, 1),
    "previous_cancellations": (0, 50),
    "previous_bookings_not_canceled": (0, 100),
    "days_in_waiting_list": (0, 500),
}
CATEGORIES = {
    "hotel": {"City Hotel", "Resort Hotel"},
    "meal": {"BB", "HB", "FB", "SC", "Undefined"},
    "market_segment": {"Online TA", "Offline TA/TO", "Groups", "Direct", "Corporate", "Complementary", "Aviation", "Undefined"},
    "distribution_channel": {"TA/TO", "Direct", "Corporate", "GDS", "Undefined"},
    "reserved_room_type": {"A", "B", "C", "D", "E", "F", "G", "H", "L"},
    "customer_type": {"Transient", "Transient-Party", "Contract", "Group"},
}
ALLOWED_IMAGES = {
    "m2_target_distribution.png",
    "m3_lead_time_cancellation_rate.png",
    "m4_hotel_type_cancellation.png",
    "m4_market_segment_cancellation.png",
    "m4_arrival_month_cancellation.png",
}
ASSETS = {"/": ("index.html", "text/html; charset=utf-8"),
          "/index.html": ("index.html", "text/html; charset=utf-8"),
          "/styles.css": ("styles.css", "text/css; charset=utf-8"),
          "/app.js": ("app.js", "text/javascript; charset=utf-8")}

model_bundle: dict | None = None
model_error: str | None = None


def load_model() -> None:
    global model_bundle, model_error
    model_bundle = None
    model_error = None
    if not MODEL_PATH.exists():
        model_error = "The trained model has not been exported yet. Run: python dashboard/export_model.py"
        return
    try:
        bundle = joblib.load(MODEL_PATH)  # Load only your OWN trusted local model file.
        if not isinstance(bundle, dict) or not {"pipeline", "feature_names", "threshold"} <= bundle.keys():
            raise ValueError("The model artifact does not match the Group 76 dashboard format.")
        if len(bundle["feature_names"]) != 21:
            raise ValueError("The saved model must use exactly 21 project features.")
        model_bundle = bundle
    except Exception as exc:
        model_error = f"Cannot load saved model: {exc}. Re-export it in your Jupyter Python environment."


def build_record(payload: object) -> tuple[dict, list[str]]:
    if not isinstance(payload, dict):
        raise ValueError("Booking details must be a JSON object.")

    allowed = set(NUMERICAL) | set(CATEGORIES) | {"arrival_date", "country"}
    unknown = set(payload) - allowed
    if unknown:
        raise ValueError("Unexpected field(s): " + ", ".join(sorted(unknown)))

    try:
        arrival = date.fromisoformat(str(payload["arrival_date"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Enter a valid arrival date (YYYY-MM-DD).") from exc
    if arrival.year < 2015 or arrival.year > 2035:
        raise ValueError("Arrival year must be between 2015 and 2035.")

    # The source CSV numbers weeks Sunday–Saturday, with the first partial
    # week of the calendar year as week 1. This differs from ISO weeks.
    # Verified against all 119,210 records in the validated project dataset.
    sunday_first_week = int(arrival.strftime("%U"))
    january_first_is_sunday = date(arrival.year, 1, 1).weekday() == 6
    dataset_week_number = sunday_first_week + (0 if january_first_is_sunday else 1)

    record = {
        "arrival_date_year": arrival.year,
        "arrival_date_month": arrival.strftime("%B"),
        "arrival_date_week_number": dataset_week_number,
        "arrival_date_day_of_month": arrival.day,
    }

    for field, (low, high) in NUMERICAL.items():
        try:
            raw = payload[field]
            if isinstance(raw, bool):
                raise ValueError()
            numeric = float(raw)
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"Enter a valid number for {field.replace('_', ' ')}.") from exc
        if not math.isfinite(numeric) or numeric != int(numeric) or not low <= numeric <= high:
            raise ValueError(f"{field.replace('_', ' ')} must be a whole number from {low} to {high}.")
        record[field] = int(numeric)

    for field, options in CATEGORIES.items():
        value = payload.get(field)
        if not isinstance(value, str) or value not in options:
            raise ValueError(f"Select a valid {field.replace('_', ' ')} value.")
        record[field] = value

    country = payload.get("country")
    if not isinstance(country, str):
        raise ValueError("Please enter a country code.")
    country = country.strip().upper()
    if not re.fullmatch(r"[A-Z]{2,3}", country) and country != "UNKNOWN":
        raise ValueError("Use a two- or three-letter country code, e.g. PRT, GBR, FRA, or Unknown.")
    record["country"] = "Unknown" if country == "UNKNOWN" else country

    if record["adults"] + record["children"] + record["babies"] == 0:
        raise ValueError("A reservation needs at least one guest.")
    if record["stays_in_weekend_nights"] + record["stays_in_week_nights"] == 0:
        raise ValueError("Enter at least one stay night.")

    warnings = []
    years = (model_bundle or {}).get("training_arrival_years", [2015, 2016, 2017])
    if arrival.year not in years:
        warnings.append(
            f"Arrival year {arrival.year} is outside the historical 2015–2017 training period. "
            "The score may not generalize to contemporary bookings."
        )
    if model_bundle:
        fitted = model_bundle["pipeline"].named_steps["preprocessor"]
        try:
            cat_names = list(fitted.transformers_[1][2])
            one_hot = fitted.named_transformers_["cat"].named_steps["encoder"]
            if "country" in cat_names:
                idx = cat_names.index("country")
                if record["country"] not in one_hot.categories_[idx]:
                    warnings.append("This country code did not occur in the training data. The model treats it as an unseen category.")
        except (AttributeError, KeyError, ValueError, IndexError):
            pass
    return record, warnings


class Handler(BaseHTTPRequestHandler):
    server_version = "Group76LocalDashboard/1.0"

    def _headers(self, status: int, content_type: str, size: int) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(size))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.end_headers()

    def bytes_response(self, content: bytes, status: int = 200, mime: str = "application/octet-stream") -> None:
        self._headers(status, mime, len(content))
        self.wfile.write(content)

    def json_response(self, content: object, status: int = 200) -> None:
        self.bytes_response(json.dumps(content, allow_nan=False).encode("utf-8"), status, "application/json; charset=utf-8")

    def do_GET(self) -> None:
        path = urlsplit(self.path).path
        if path in ASSETS:
            filename, mime = ASSETS[path]
            self.bytes_response((HERE / filename).read_bytes(), mime=mime)
            return
        if path == "/api/status":
            self.json_response({
                "ready": model_bundle is not None,
                "error": model_error,
                "model": "Random Forest (Tuned)",
                "threshold": (model_bundle or {}).get("threshold", 0.40),
                "feature_count": len((model_bundle or {}).get("feature_names", [])),
                "historical_training_years": (model_bundle or {}).get("training_arrival_years", [2015, 2016, 2017]),
            })
            return
        if path == "/api/metrics":
            if not METRICS_PATH.is_file():
                self.json_response({"error": "Saved metrics CSV not found."}, 404)
                return
            record = pd.read_csv(METRICS_PATH).iloc[0].to_dict()
            self.json_response({k: float(v) if isinstance(v, (int, float)) else v for k, v in record.items()})
            return
        if path.startswith("/charts/"):
            filename = unquote(path[len("/charts/"):])
            if filename not in ALLOWED_IMAGES or not (CHART_DIR / filename).is_file():
                self.json_response({"error": "Chart not found."}, 404)
                return
            self.bytes_response((CHART_DIR / filename).read_bytes(), mime="image/png")
            return
        self.json_response({"error": "Not found"}, 404)

    def do_POST(self) -> None:
        if urlsplit(self.path).path != "/api/predict":
            self.json_response({"error": "Not found"}, 404)
            return
        if model_bundle is None:
            self.json_response({"error": model_error or "Model unavailable."}, 503)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 8192:
                self.json_response({"error": "Invalid request size."}, 413)
                return
            raw = json.loads(self.rfile.read(length).decode("utf-8"))
            row, warnings = build_record(raw)
            X = pd.DataFrame([row], columns=model_bundle["feature_names"])
            probability = float(model_bundle["pipeline"].predict_proba(X)[0, 1])
            threshold = float(model_bundle["threshold"])
            self.json_response({
                "probability": round(probability, 6),
                "threshold": threshold,
                "flagged": probability >= threshold,
                "label": "Elevated cancellation risk" if probability >= threshold else "Below alert threshold",
                "warnings": warnings,
                "note": "A decision-support score, not a guarantee or automated reservation decision.",
            })
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            self.json_response({"error": str(exc)}, 400)
        except Exception as exc:
            print("Prediction error:", repr(exc), file=sys.stderr)
            self.json_response({"error": "Prediction failed. Check the server output."}, 500)

    def log_message(self, format: str, *args: object) -> None:
        # Only log request methods/paths, never personal booking details.
        msg = format % args
        print(f"{self.address_string()} - {msg}")


def main() -> None:
    load_model()
    if model_error:
        print("MODEL STATUS:", model_error)
    else:
        print("MODEL STATUS: Ready for predictions")
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Dashboard: http://{HOST}:{PORT}")
    print("Local development/demo use only. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
