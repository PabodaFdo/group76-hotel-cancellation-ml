# Member 1 — Phase 3: Preprocessing & Cleaning Log

**Owner:** IT24101668 (Member 1)  
**Dataset:** `hotel_bookings.csv`  
**Target:** `is_canceled`

## Purpose

This phase converts the raw dataset into a cleaner, leakage-aware dataset for the group's modelling work. The same target definition and preprocessing decisions should be used by all model members.

## Initial data

- Original rows: 119,390
- Original columns: 32
- Exact duplicate rows identified: 31,994

## Cleaning decisions

### 1. Remove exact duplicate rows

**Finding:** 31,994 exact duplicate rows were identified.

**Decision:** Remove exact duplicate rows using `drop_duplicates()`.

**Reason:** Exact duplicates repeat the same complete booking record and can distort class frequencies and model evaluation.

**Result after duplicate removal:** 87,396 rows.

### 2. Remove target-leakage fields

Removed:

- `reservation_status`
- `reservation_status_date`

**Reason:** These fields describe the final reservation outcome/status and can reveal information that would not be available at the intended prediction point. Keeping them could cause target leakage.

### 3. Remove high-missingness identifier fields

Removed:

- `company`
- `agent`

**Reason:** `company` has very high missingness (94.306%) and both fields are identifier-like rather than ordinary continuous measurements. Removing them avoids high-missingness/high-cardinality complications in the common modelling dataset.

**Important:** This should be confirmed by the group because it is a modelling-feature decision, not merely a mechanical cleaning step.

### 4. Handle missing `children`

- Missing values before cleaning: 4
- Decision: replace missing values with `0`.

**Reason:** `children` is a count variable and zero is a natural interpretation for a missing count in this dataset. This decision should be stated explicitly in the report.

### 5. Handle missing `country`

- Missing values before cleaning: 488
- Decision: replace missing values with `"Unknown"`.

**Reason:** `country` is categorical. Using an explicit category preserves the booking records without inventing a specific country.

### 6. Handle invalid negative ADR

- Negative `adr` records: 1
- Decision: treat the negative value as invalid, replace it with missing, then impute the hotel-specific median ADR.

**Reason:** ADR represents an average daily rate and a negative rate is not meaningful. The row is retained because the remaining booking information is usable.

### 7. Handle zero-guest records

- Records with `adults + children + babies = 0`: 166
- Decision: remove these records.

**Reason:** A booking with zero adults, children and babies is not a valid guest booking for this modelling problem. These records are treated as invalid data rather than imputing a guest count.

## Final local cleaned dataset

- Rows: 87,230
- Columns: 28
- Remaining missing values: 0

## Final feature exclusions

The following columns are excluded from the common modelling dataset:

```text
reservation_status
reservation_status_date
company
agent
```

## Important group agreement

Before all model members use the processed dataset, the group should confirm the treatment of:

1. `company`
2. `agent`
3. zero-guest records
4. negative `adr`

Once agreed, these decisions should remain consistent across all model notebooks.

## Handoff to modelling

The cleaned dataset should be treated as the common starting point for subsequent modelling. Model members should **not independently repeat or alter these cleaning decisions** without documenting a group-approved change.
