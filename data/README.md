# Hotel Booking Demand Dataset

## 1. Dataset Information

**Dataset:** Hotel Booking Demand  
**Source:** [Kaggle — Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

**Original research:** António, N., de Almeida, A., & Nunes, L. (2019). *Hotel booking demand datasets*. Data in Brief, 22, 41–49.

The dataset contains reservation records from a City Hotel and a Resort Hotel.

| Property | Value |
|---|---|
| Original records | 119,390 |
| Original columns | 32 |
| Target variable | `is_canceled` |
| ML task | Binary classification |

## 2. Dataset Files

| File | Purpose |
|---|---|
| `data/raw/hotel_bookings.csv` | Original dataset |
| `data/processed/hotel_bookings_validated_phase3.csv` | Validated dataset used for modelling |

The original dataset is preserved separately from the processed dataset.

## 3. Data Cleaning

The validated dataset contains **119,210 records and 32 columns**.

The main cleaning decisions were:

- Replace missing `children` values with zero.
- Label missing `country` values as `"Unknown"`.
- Remove 180 records with zero total guests.
- Retain exact duplicate records because their reservation identities cannot be verified.

The original dataset contains 31,994 exact duplicate rows beyond their first occurrences.

A supplementary experiment investigated the effect of removing duplicates during model training. The results are documented in:

`notebooks/04_final/duplicate_sensitivity.ipynb`

## 4. Model Inputs

The modelling workflow uses 21 approved booking features to predict `is_canceled`.

Features that directly reveal the outcome or have uncertain availability at booking confirmation were excluded.

The feature selection and preprocessing decisions are documented in:

`docs/logs/preprocessing_feature_log.md`

## 5. Data Splitting

The validated dataset was divided using a group-aware holdout strategy.

| Dataset | Records |
|---|---:|
| Training | 95,334 |
| Held-out test | 23,876 |

The saved split indices are stored in:

`results/splits/group_holdout_indices.npz`

## 6. Reproducibility

The raw dataset should remain unchanged.

Cleaning and preprocessing decisions are recorded in the project notebooks, and the shared preprocessing implementation is maintained in:

`src/preprocessing/pipeline.py`

Dataset files should only be committed to the repository in accordance with the group's data-management policy.

The source dataset version and file checksum should be recorded when preparing the final reproducibility evidence.

## 7. Dataset Integrity Verification

SHA-256 fingerprints were recorded to support dataset integrity and reproducibility.

| Dataset | SHA-256 |
|---|---|
| Original (`hotel_bookings.csv`) | `D10CDEB07DE9309007F528D6499A2C0467AE7A6B287B80FFD759E11E61801639` |
| Processed (`hotel_bookings_validated_phase3.csv`) | `22032F7AB607AF9791001848A9FFD3F2AC85137B073D0F77E3186A02A668724A` |

The original dataset contains 119,390 records, while the validated dataset contains 119,210 records after targeted cleaning.

These fingerprints identify the exact dataset files used for the Group 76 machine learning experiments. Other group members can verify file consistency by computing SHA-256 hashes and comparing them with the recorded values.