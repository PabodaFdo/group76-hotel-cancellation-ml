"""Export the selected Group 76 Random Forest using the original training indices.

Run once with the same Python environment used for the ML notebooks:
    python dashboard/export_model.py

This does NOT access labels from the held-out test set or retune the model.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.preprocessing.pipeline import build_preprocessor  # noqa: E402

DATA_PATH = ROOT / "data" / "processed" / "hotel_bookings_validated_phase3.csv"
SPLIT_PATH = ROOT / "results" / "splits" / "group_holdout_indices.npz"
MODEL_PATH = ROOT / "results" / "final_model" / "random_forest_pipeline.joblib"

EXPECTED_PROCESSED_SHA256 = "22032F7AB607AF9791001848A9FFD3F2AC85137B073D0F77E3186A02A668724A"
EXCLUDED = [
    "is_canceled", "assigned_room_type", "booking_changes", "deposit_type",
    "agent", "company", "adr", "required_car_parking_spaces",
    "total_of_special_requests", "reservation_status", "reservation_status_date",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest().upper()


def main() -> None:
    for p in (DATA_PATH, SPLIT_PATH):
        if not p.is_file():
            raise SystemExit(f"Required project file not found: {p}")

    digest = sha256(DATA_PATH)
    if digest != EXPECTED_PROCESSED_SHA256:
        raise SystemExit(
            "The processed dataset differs from the verified project dataset.\n"
            f"Expected SHA-256: {EXPECTED_PROCESSED_SHA256}\n"
            f"Actual SHA-256:   {digest}\n"
            "Do not train a new model until you confirm which dataset is correct."
        )

    df = pd.read_csv(DATA_PATH)
    with np.load(SPLIT_PATH) as saved:
        train_idx = saved["train_idx"]
        test_idx = saved["test_idx"]

    if len(df) != 119210 or len(train_idx) != 95334 or len(test_idx) != 23876:
        raise SystemExit("Dataset or saved split sizes do not match the verified project.")
    if np.intersect1d(train_idx, test_idx).size:
        raise SystemExit("The saved train/test split overlaps. Export stopped.")
    if np.unique(np.r_[train_idx, test_idx]).size != len(df):
        raise SystemExit("Saved split does not cover every record exactly once.")

    X = df.drop(columns=EXCLUDED).iloc[train_idx].copy()
    y = df["is_canceled"].iloc[train_idx].copy()
    if X.shape != (95334, 21):
        raise SystemExit(f"Unexpected training shape: {X.shape}")

    pipe = Pipeline([
        ("preprocessor", build_preprocessor(X)),
        ("classifier", RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            min_samples_leaf=5,
            class_weight=None,
            random_state=42,
            n_jobs=2,
        )),
    ])

    print("Training the selected Random Forest on the 95,334 training records only...")
    pipe.fit(X, y)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    artifact = {
        "pipeline": pipe,
        "threshold": 0.40,
        "feature_names": list(X.columns),
        "training_count": len(X),
        "processed_sha256": digest,
        "training_arrival_years": sorted(int(z) for z in X["arrival_date_year"].unique()),
        "app_version": "1.0",
    }
    joblib.dump(artifact, MODEL_PATH, compress=3)
    print("Saved model:", MODEL_PATH)
    print("Threshold:", artifact["threshold"])
    print("Input features:", len(artifact["feature_names"]))
    print("File size: {:.1f} MB".format(MODEL_PATH.stat().st_size / 1024**2))
    print("Done. Launch the dashboard with: python dashboard/server.py")


if __name__ == "__main__":
    main()
