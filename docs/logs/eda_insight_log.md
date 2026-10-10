# EDA Insight Log — Group 76

## 1. Purpose

This document records the key findings from Exploratory Data Analysis (EDA) conducted for the Hotel Booking Cancellation Risk Prediction project.

EDA was performed to understand the dataset structure, identify data-quality issues, investigate cancellation patterns, and support feature selection and model development.

Initial dataset understanding, data-quality assessment, and numerical EDA were conducted using the original dataset. Categorical and time-based EDA was subsequently conducted using the validated training subset.

## 2. Dataset Overview

**Original dataset:** `data/raw/hotel_bookings.csv`

**Validated dataset:** `data/processed/hotel_bookings_validated_phase3.csv`

| Dataset | Records | Features/Columns |
|---|---:|---:|
| Original dataset | 119,390 | 32 |
| Validated dataset | 119,210 | 32 |
| Training subset | 95,334 | 32 |

The target variable is `is_canceled`, where `0` indicates a non-cancelled booking and `1` indicates a cancelled booking.

**Evidence:** `notebooks/01_eda/m1_dataset_structure_eda.ipynb`

## 3. Insight 1 — Target Class Distribution

### Evidence

The original dataset contained:

| Booking Outcome | Records | Percentage |
|---|---:|---:|
| Not cancelled | 75,166 | 62.96% |
| Cancelled | 44,224 | 37.04% |

The validated training subset contained 60,053 non-cancelled bookings (62.99%) and 35,281 cancelled bookings (37.01%).

**Source:** `notebooks/01_eda/m2_data_quality_target.ipynb`

**Figure:** `results/eda/m2_target_distribution.png`

### Observation and Interpretation

Non-cancelled bookings form the majority class, indicating moderate class imbalance. However, cancelled bookings represent a substantial proportion of the dataset.

### ML Implication

Evaluation should not rely on accuracy alone. Precision, recall, F1-score, ROC-AUC, and PR-AUC were selected to provide a more informative assessment of cancellation prediction.

---

## 4. Insight 2 — Cancellation Rates Differ by Hotel Type

### Evidence

Analysis of the validated training subset produced:

| Hotel Type | Bookings | Cancellation Rate |
|---|---:|---:|
| City Hotel | 63,400 | 41.6% |
| Resort Hotel | 31,934 | 28.0% |

**Source:** `notebooks/01_eda/m4_categorical_time_eda.ipynb`

**Figure:** `results/eda/m4_hotel_type_cancellation.png`

### Observation and Interpretation

City Hotel bookings recorded a higher cancellation rate than Resort Hotel bookings. Hotel type is therefore associated with differences in historical cancellation behaviour.

### ML Implication

The `hotel` feature was retained as a potential predictor because the two hotel categories exhibit different cancellation patterns.

---

## 5. Insight 3 — Market Segment Is Associated with Cancellation Risk

### Evidence

The training subset showed the following cancellation rates:

| Market Segment | Bookings | Cancellation Rate |
|---|---:|---:|
| Groups | 16,078 | 61.1% |
| Online TA | 45,165 | 36.9% |
| Offline TA/TO | 19,075 | 33.6% |
| Corporate | 4,161 | 18.1% |
| Direct | 10,086 | 15.3% |

**Source:** `notebooks/01_eda/m4_categorical_time_eda.ipynb`

**Figure:** `results/eda/m4_market_segment_cancellation.png`

### Observation and Interpretation

Group bookings recorded the highest cancellation rate among the major market segments examined.

Direct and Corporate bookings showed comparatively lower cancellation rates.

These differences suggest that the type of booking and reservation channel are associated with cancellation behaviour.

### ML Implication

`market_segment` was retained as an input feature because it provides information about booking characteristics relevant to cancellation-risk prediction.

These relationships are observational and do not establish causation.

---

## 6. Insight 4 — Cancellation Patterns Vary by Arrival Month

### Evidence

Selected cancellation rates from the training subset were:

| Arrival Month | Cancellation Rate |
|---|---:|
| April | 40.1% |
| May | 40.4% |
| June | 41.5% |
| November | 30.4% |

August recorded the highest monthly booking volume, with 11,159 bookings.

**Source:** `notebooks/01_eda/m4_categorical_time_eda.ipynb`

**Figure:** `results/eda/m4_arrival_month_cancellation.png`

### Observation and Interpretation

Cancellation rates varied across arrival months. June recorded the highest cancellation rate in the training subset, while November recorded the lowest.

Booking volumes also differed across months, indicating variations in historical demand.

### ML Implication

Arrival date features were retained because they may capture useful seasonal booking patterns.

However, historical monthly associations do not necessarily generalize to future periods.

---

## 7. Insight 5 — Lead Time Is Associated with Cancellation

### Evidence

Numerical EDA on the original dataset identified differences in lead time between cancelled and non-cancelled bookings.

| Booking Outcome | Median Lead Time |
|---|---:|
| Not cancelled | 45 days |
| Cancelled | 113 days |

Cancellation rates also varied by lead-time interval:

| Lead Time | Cancellation Rate |
|---|---:|
| 0–7 days | 9.63% |
| 8–30 days | 27.86% |
| 31–90 days | 37.70% |
| 91–180 days | 44.71% |
| 181–365 days | 55.45% |
| More than 365 days | 67.66% |

**Source:** `notebooks/01_eda/m3_numeric_eda.ipynb`

**Figure:** `results/eda/m3_lead_time_cancellation_rate.png`

### Observation and Interpretation

Bookings made further in advance had higher historical cancellation rates.

Cancelled bookings also had substantially longer median lead times than non-cancelled bookings.

### ML Implication

`lead_time` was retained as an important candidate feature because it is available at booking confirmation and demonstrates a meaningful association with cancellation.

This relationship is predictive rather than causal.

---

## 8. Insight 6 — Previous Cancellations and Booking History

### Evidence

The original dataset showed the following relationship between previous cancellations and the target:

| Previous Cancellations | Bookings | Cancellation Rate |
|---|---:|---:|
| 0 | 112,906 | 33.91% |
| 1 | 6,051 | 94.43% |
| 2 | 116 | 32.76% |
| 3 or more | 317 | 59.94% |

**Source:** `notebooks/01_eda/m3_numeric_eda.ipynb`

### Observation and Interpretation

Bookings associated with exactly one previous cancellation showed a particularly high cancellation rate.

However, rates were not consistently increasing across all categories, and categories with higher previous cancellation counts contained relatively few observations.

### ML Implication

`previous_cancellations` was retained because booking history may provide useful predictive information.

The non-monotonic pattern and unequal group sizes require careful interpretation.

---

## 9. Key Data Quality Findings

Data-quality assessment identified the following issues in the original dataset:

| Issue | Evidence |
|---|---:|
| Missing `company` values | 112,593 |
| Missing `agent` values | 16,340 |
| Missing `country` values | 488 |
| Missing `children` values | 4 |
| Exact duplicate rows | 31,994 |
| Zero-guest records | 180 |

One negative ADR value was also identified.

**Source:** `notebooks/01_eda/m2_data_quality_target.ipynb`

### Preprocessing Decisions

Targeted cleaning was performed to address missing values and invalid zero-guest bookings.

Exact duplicate records were retained in the primary workflow because unique reservation identifiers were unavailable to verify their identities.

A supplementary duplicate sensitivity experiment later demonstrated that removing exact duplicates during training changed the model's performance.

**Supporting evidence:**

- `docs/logs/preprocessing_feature_log.md`
- `notebooks/04_final/duplicate_sensitivity.ipynb`

### Leakage Considerations

The `reservation_status` variable directly corresponded to final reservation outcomes in the original dataset and was excluded from predictive modelling.

Other variables with uncertain availability at booking confirmation were reviewed during feature selection.

**Source:** `notebooks/01_eda/m2_data_quality_target.ipynb`

**Supporting notebook:** `notebooks/02_preprocessing/m3_leakage_validation.ipynb`

---

## 10. EDA Evidence Summary

| EDA Area | Responsible Notebook | Supporting Figure |
|---|---|---|
| Dataset structure | `m1_dataset_structure_eda.ipynb` | Tables and printed results |
| Target distribution | `m2_data_quality_target.ipynb` | `m2_target_distribution.png` |
| Lead-time patterns | `m3_numeric_eda.ipynb` | `m3_lead_time_cancellation_rate.png` |
| Market segment | `m4_categorical_time_eda.ipynb` | `m4_market_segment_cancellation.png` |
| Arrival month | `m4_categorical_time_eda.ipynb` | `m4_arrival_month_cancellation.png` |
| Hotel type | `m4_categorical_time_eda.ipynb` | `m4_hotel_type_cancellation.png` |

All listed chart filenames refer to the `results/eda/` directory.

The original notebooks contain the underlying calculations and additional analysis outputs.

## 11. Overall EDA Conclusion

Exploratory data analysis identified meaningful historical associations between booking cancellation and several characteristics, including hotel type, market segment, arrival month, lead time, and previous cancellation history.

These findings supported the selection of relevant features and the development of classification models for the cancellation-risk task.

Data-quality analysis also identified missing values, duplicate records, and possible leakage-related variables that required attention during preprocessing.

The class distribution justified evaluating models using precision, recall, F1-score, and PR-AUC in addition to accuracy.

Initial raw-data EDA was descriptive, while subsequent categorical and time-based analysis used the training subset. Consequently, not all exploratory findings were derived exclusively from training data.

The findings represent historical associations rather than causal relationships, and further validation would be required to establish their applicability to future hotel bookings.