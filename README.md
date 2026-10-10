# IT3091 Machine Learning — Group 76

## Hotel Booking Demand — Cancellation Risk Prediction

### Project Information

| Item | Details |
|---|---|
| Module | IT3091 Machine Learning |
| Group | 76 |
| Track | Guided Data Track |
| Domain | Tourism and Hospitality |
| Dataset | Hotel Booking Demand |
| Primary Decision Lens | Cancellation Risk |
| Machine Learning Task | Binary Classification |

## 1. Project Overview

This project develops a machine learning solution to predict hotel booking cancellations using historical reservation information.

The primary stakeholders are hotel revenue management and operations teams. Predicting cancellation risk can support reservation monitoring, occupancy forecasting, and operational resource planning.

**Business question:** Can information available at booking confirmation help identify reservations at higher risk of cancellation?

The target variable is `is_canceled`, where `1` represents a cancelled booking and `0` represents a booking that was not cancelled.

## 2. Dataset

**Source:** [Hotel Booking Demand — Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

The original dataset contains 119,390 records and 32 columns.

After targeted cleaning, the validated dataset contains 119,210 records. The models use 21 selected input features.

Exact duplicate records were retained because unique reservation identifiers were unavailable. A supplementary sensitivity experiment assessed the effect of removing duplicates during model training. The results and limitations are documented in `notebooks/04_final/duplicate_sensitivity.ipynb`.

## 3. Machine Learning Approach

The project evaluated five classification approaches:

1. Dummy Classifier
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. Gradient Boosting

Preprocessing was implemented using shared scikit-learn pipelines. Model development used group-aware splitting and cross-validation to reduce overlap between identical input-feature combinations.

Hyperparameter tuning optimized PR-AUC. Threshold analysis was subsequently performed using out-of-fold predictions from the development data.

## 4. Final Model and Results

The selected model is a **tuned Random Forest** with a classification threshold of **0.40**.

| Metric | Held-Out Test Result |
|---|---:|
| Accuracy | 0.7939 |
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| ROC-AUC | 0.8857 |
| PR-AUC | 0.8434 |

The final evaluation used 23,876 held-out bookings.

The model correctly identified 6,676 cancellations, missed 2,242 cancellations, and generated 2,678 false cancellation alerts.

These predictions are intended to support hotel operations and should not automatically trigger consequential customer decisions.

## 5. Project Structure

| Path | Purpose |
|---|---|
| `data/` | Raw and processed datasets |
| `notebooks/01_data_understanding_eda/` | Dataset understanding and exploratory analysis |
| `notebooks/02_preprocessing/` | Cleaning, preprocessing, feature engineering and leakage review |
| `notebooks/03_modelling/` | Classification models and hyperparameter tuning |
| `notebooks/04_final/` | Final model evaluation and duplicate sensitivity analysis |
| `src/preprocessing/pipeline.py` | Shared preprocessing implementation |
| `results/metrics/` | Model evaluation results |
| `results/splits/` | Saved train/test split |
| `docs/logs/` | Decision, EDA, preprocessing and model comparison logs |
| `docs/recommendation/` | Member-specific and final recommendations |
| `report/` | Final report materials |
| `video/` | Demonstration materials |
| `individual_learning/` | Individual learning evidence |

## 6. Reproducibility

Install project dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter lab
```

The main final notebook is:

`notebooks/04_final/final_group_notebook.ipynb`

To reproduce the results, the original dataset and processed files must be placed in their expected project directories.

The analysis depends on the validated dataset, saved group-aware split, shared preprocessing implementation, and model evaluation files.

The notebooks should be executed in their documented order, with paths resolved relative to the notebook directories.

Exact dependency versions and a dataset fingerprint should be recorded before submission to strengthen reproducibility.

## 7. Supporting Documentation

- `docs/data_dictionary.md`
- `docs/logs/decision_log.md`
- `docs/logs/eda_insight_log.md`
- `docs/logs/preprocessing_feature_log.md`
- `docs/logs/model_comparison.md`
- `docs/recommendation/final_recommendation.md`
- `docs/ai_use_declaration.md`

## 8. Limitations and Responsible AI

The model uses historical hotel booking data, and performance on future periods or other hotels has not been independently established.

Duplicate booking identities cannot be verified, and results are sensitive to duplicate handling.

Country and customer-related features require careful interpretation and fairness assessment.

Predictions should support human decision-making rather than automatically cancel reservations, penalize customers, or determine overbooking decisions.

## 9. Project Status

**Completed:** Business framing, data understanding, EDA, preprocessing, model development, hyperparameter tuning, model comparison, threshold analysis, held-out test evaluation, feature interpretation, and duplicate sensitivity analysis.

**Final submission preparation:** Complete the final report, three-minute YouTube demonstration, reproducibility details, and AI-use records. Each member must also prepare their individual A4 Personal Learning Journey report.

## 10. AI Use

AI-assisted development and documentation should be transparently reported in `docs/ai_use_declaration.md`, including how outputs were reviewed and verified by group members.