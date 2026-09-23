# Data Dictionary

## 1. Dataset overview
- Rows: **119,390**
- Columns: **32**
- Categorical/object columns: **12**
- Numeric columns: **20**
- Target: **`is_canceled`**

## 2. What one row represents
Each row represents one hotel booking/reservation record.

## 3. Target variable
`is_canceled` is the project target. It is binary: `1` indicates a canceled booking and `0` indicates a booking that was not canceled.

## 4. Dataset structure
| Column | Type | Missing | Missing % | Unique | Role / note |
|---|---|---:|---:|---:|---|
| `hotel` | object | 0 | 0.000% | 2 | PREDICTOR / CANDIDATE FEATURE |
| `is_canceled` | int64 | 0 | 0.000% | 2 | TARGET |
| `lead_time` | int64 | 0 | 0.000% | 479 | PREDICTOR / CANDIDATE FEATURE |
| `arrival_date_year` | int64 | 0 | 0.000% | 3 | PREDICTOR / CANDIDATE FEATURE |
| `arrival_date_month` | object | 0 | 0.000% | 12 | PREDICTOR / CANDIDATE FEATURE |
| `arrival_date_week_number` | int64 | 0 | 0.000% | 53 | PREDICTOR / CANDIDATE FEATURE |
| `arrival_date_day_of_month` | int64 | 0 | 0.000% | 31 | PREDICTOR / CANDIDATE FEATURE |
| `stays_in_weekend_nights` | int64 | 0 | 0.000% | 17 | PREDICTOR / CANDIDATE FEATURE |
| `stays_in_week_nights` | int64 | 0 | 0.000% | 35 | PREDICTOR / CANDIDATE FEATURE |
| `adults` | int64 | 0 | 0.000% | 14 | PREDICTOR / CANDIDATE FEATURE |
| `children` | float64 | 4 | 0.003% | 5 | PREDICTOR / CANDIDATE FEATURE; Missing values present (4 rows); requires a preprocessing decision. |
| `babies` | int64 | 0 | 0.000% | 5 | PREDICTOR / CANDIDATE FEATURE |
| `meal` | object | 0 | 0.000% | 5 | PREDICTOR / CANDIDATE FEATURE |
| `country` | object | 488 | 0.409% | 177 | PREDICTOR / CANDIDATE FEATURE; Missing values present (488 rows); requires a preprocessing decision. |
| `market_segment` | object | 0 | 0.000% | 8 | PREDICTOR / CANDIDATE FEATURE |
| `distribution_channel` | object | 0 | 0.000% | 5 | PREDICTOR / CANDIDATE FEATURE |
| `is_repeated_guest` | int64 | 0 | 0.000% | 2 | PREDICTOR / CANDIDATE FEATURE |
| `previous_cancellations` | int64 | 0 | 0.000% | 15 | PREDICTOR / CANDIDATE FEATURE |
| `previous_bookings_not_canceled` | int64 | 0 | 0.000% | 73 | PREDICTOR / CANDIDATE FEATURE |
| `reserved_room_type` | object | 0 | 0.000% | 10 | PREDICTOR / CANDIDATE FEATURE |
| `assigned_room_type` | object | 0 | 0.000% | 12 | PREDICTOR / CANDIDATE FEATURE |
| `booking_changes` | int64 | 0 | 0.000% | 21 | PREDICTOR / CANDIDATE FEATURE |
| `deposit_type` | object | 0 | 0.000% | 3 | PREDICTOR / CANDIDATE FEATURE |
| `agent` | float64 | 16340 | 13.686% | 333 | PREDICTOR / CANDIDATE FEATURE; High missingness (13.686%); requires a group decision during preprocessing. |
| `company` | float64 | 112593 | 94.307% | 352 | PREDICTOR / CANDIDATE FEATURE; Very high missingness (94.306%); requires a group decision during preprocessing. |
| `days_in_waiting_list` | int64 | 0 | 0.000% | 128 | PREDICTOR / CANDIDATE FEATURE |
| `customer_type` | object | 0 | 0.000% | 4 | PREDICTOR / CANDIDATE FEATURE |
| `adr` | float64 | 0 | 0.000% | 8879 | PREDICTOR / CANDIDATE FEATURE |
| `required_car_parking_spaces` | int64 | 0 | 0.000% | 5 | PREDICTOR / CANDIDATE FEATURE |
| `total_of_special_requests` | int64 | 0 | 0.000% | 6 | PREDICTOR / CANDIDATE FEATURE |
| `reservation_status` | object | 0 | 0.000% | 3 | PREDICTOR / CANDIDATE FEATURE; Potential target leakage: reflects final/post-booking outcome information; exclude from predictive features unless the group explicitly defines a time point where this information is available. |
| `reservation_status_date` | object | 0 | 0.000% | 926 | PREDICTOR / CANDIDATE FEATURE; Potential target leakage: reflects final/post-booking outcome information; exclude from predictive features unless the group explicitly defines a time point where this information is available. |

## 5. Data-quality observations for the next phase
- `children` has **4** missing values.
- `country` has **488** missing values.
- `agent` has **16,340** missing values (13.686%).
- `company` has **112,593** missing values (94.307%).
- No missing values were found in the other columns.
- `reservation_status` and `reservation_status_date` are recorded after the booking outcome is known and therefore should be treated as potential target leakage for a cancellation-risk prediction task.
- `agent` and `company` are identifiers rather than ordinary continuous measurements; their treatment should be agreed during preprocessing.

## 6. Important Phase 2 conclusion
The dataset is suitable for the agreed binary-classification framing because `is_canceled` provides a binary outcome. Before modelling, the group must agree on a leakage-safe feature set and document how missing values and identifier-like fields will be handled.
