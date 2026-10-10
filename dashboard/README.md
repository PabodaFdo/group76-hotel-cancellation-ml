# Group 76 — HTML Prediction Dashboard

A responsive, local HTML/CSS/JavaScript dashboard that makes **real** predictions with Group 76's selected Random Forest pipeline. It does **not** generate fake predictions and does **not** require Flask, Streamlit, external charts, internet access, or retraining on each prediction.

## Installation

Copy the entire `dashboard/` folder into the **root** of your existing repository:

```
group76-hotel-cancellation-ml/
├── dashboard/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   ├── server.py
│   ├── export_model.py
│   └── README.md
├── data/processed/hotel_bookings_validated_phase3.csv
├── results/splits/group_holdout_indices.npz
├── results/metrics/final_random_forest_test_results.csv
├── results/eda/
└── src/preprocessing/pipeline.py
```

### 1. Export the fitted model **once**

Open PowerShell at the project root. Use the **Anaconda Python that ran your notebooks**:

```powershell
& "C:\ProgramData\anaconda3\python.exe" dashboard\export_model.py
```

This program verifies the processed dataset's SHA-256, loads the existing **saved training split**, trains the selected 100-tree Random Forest with the exact project pipeline/hyperparameters on **training data only**, and saves:

`results/final_model/random_forest_pipeline.joblib`

It does **not** use held-out test labels and does **not** tune/alter the previously selected classification threshold. Training happens just once (may take several minutes on an 8 GB RAM laptop).

**Alternative if you already have `final_model` fitted in a Jupyter kernel:** With the project's `final_group_notebook.ipynb` still running and `final_model` in memory, save it without retraining:

```python
import joblib
from pathlib import Path

path = data_path.resolve().parents[2] / "results/final_model/random_forest_pipeline.joblib"
path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump({
    "pipeline": final_model,
    "threshold": 0.40,
    "feature_names": list(X_train.columns),
    "training_count": len(X_train),
    "training_arrival_years": [2015, 2016, 2017],
}, path, compress=3)
print("Model saved:", path)
```

### 2. Start the local website

```powershell
& "C:\ProgramData\anaconda3\python.exe" dashboard\server.py
```

Open **http://127.0.0.1:8765** in Edge or Chrome.

The website displays your final evaluation CSV, comparison figures, and a real input form for the **21 approved model features**. Arrival year, month, week and day are derived from a single arrival-date input using the **dataset’s Sunday-start week-number convention** (verified on all 119,210 validated records), not ISO weeks. The backend uses `predict_proba()` on the fitted pipeline and applies the chosen **0.40** threshold. No individual booking values are stored by the server.

Stop the server with `Ctrl+C`.

## Notes for your university demonstration

- The **model must be exported** before it can make predictions. If it is missing, the UI reports *Model not exported* instead of showing fabricated scores.
- The trained model is based on **2015–2017 bookings**, so predictions for modern bookings are outside its historical training period and should **not be presented as validated production forecasts**. The form shows a warning for later dates.
- All **21 input features** must be available for a live operational prediction. In the form, the historical booking fields are under *Additional booking history*.
- The model is designed for **decision support** and must not automatically cancel or penalize customers. Country is an especially sensitive operational consideration and warrants fairness review.
- The model and scikit-learn pipeline are loaded from the local trusted `joblib` file. Never load an untrusted model file.
- This HTTP server listens on **127.0.0.1**, for a local demo only. It has no authentication/HTTPS and is **not** suitable for internet hosting or use with actual customer details without additional security/privacy work.
- This is an **additional demo deliverable** and does not replace your IT3091 final notebooks, testing methodology or report.

## Troubleshooting

**`ModuleNotFoundError`**: Use `C:\ProgramData\anaconda3\python.exe`, which matches your notebook environment. Installed versions used: NumPy 1.26.4, pandas 2.2.2, scikit-learn 1.5.1.

**`model not exported`**: Run export step 1, stop/restart server, and refresh the page.

**Port already in use**: Close the previous server with Ctrl+C.

**Charts not showing**: Verify `results/eda/m4_hotel_type_cancellation.png` and `results/eda/m4_market_segment_cancellation.png` exist in the repository.

**Unseen input categories / future years**: The model was not independently validated for these; inspect the warnings and avoid treating the score as reliable for real-world decisions.
