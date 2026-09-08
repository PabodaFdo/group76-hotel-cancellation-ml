# Member 3 – ML Task, Unit of Analysis, Target and Output
**Owner:** IT24103815
## Unit of Analysis

The unit of analysis for this project is a single hotel booking. Each row in the Hotel Booking Demand dataset represents one booking record containing information related to the reservation, customer characteristics, stay details, and booking conditions.

Therefore, the machine-learning model will generate a cancellation-risk prediction for each individual booking.

## Machine Learning Task

The proposed machine-learning task is binary classification.

The objective is to use historical booking information to classify whether a hotel booking is likely to be cancelled or not cancelled. This task directly supports the selected cancellation-risk business lens because the required outcome contains two possible classes.

## Target Variable

The Hotel Booking Demand dataset contains the target variable:

`is_canceled`

This variable represents the observed cancellation outcome of a booking.

- `1` represents a cancelled booking.
- `0` represents a booking that was not cancelled.

The target will be separated from the predictor variables before model training and evaluation.

## Expected Model Output

The main model output will be a predicted cancellation class for each booking:

- Cancelled
- Not Cancelled

Where supported by the selected classification model, a cancellation-risk probability will also be produced. The probability provides more useful decision support than a class label alone because bookings can be ranked according to their estimated cancellation risk.

For example, a booking with a higher predicted cancellation probability may require greater attention during planning than a booking with a very low predicted risk.

## Link to the Business Decision

The technical prediction is intended to support hotel management, revenue planning, and operational decision-making.

Identifying bookings with higher cancellation risk before the final booking outcome is known can help decision-makers better understand booking reliability and plan resources and revenue with greater awareness of uncertainty.

The model is intended as a decision-support tool rather than an automatic decision-making system. A high predicted risk does not mean that a booking will definitely be cancelled.

## Prediction Boundary

Only information that would reasonably be available when the hotel needs to estimate cancellation risk should be considered as model input.

Variables that reveal the final reservation outcome or become available only after that outcome could create data leakage and must be reviewed before modelling. The final predictor set will therefore be confirmed during the preprocessing and leakage-audit stage.

## Proposed Technical Definition

**Input:** Historical booking information available at the selected prediction point.

**Target:** `is_canceled`

**Task:** Binary classification

**Unit of analysis:** One hotel booking

**Primary output:** Predicted cancellation class

**Additional output:** Cancellation-risk probability, where supported

**Business use:** Support booking reliability, revenue planning, and customer-management decisions.