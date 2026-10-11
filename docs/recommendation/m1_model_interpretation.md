# Member 1 — Model Interpretation

**Owner:** IT24101668

## Final Model

The tuned Random Forest classifier was selected as the final model for hotel booking cancellation-risk prediction, using a classification threshold of 0.40.

The model achieved an F1-score of 0.7307, recall of 0.7486, and PR-AUC of 0.8434 on the held-out test dataset.

## Important Predictive Relationships

Feature importance analysis identified the following influential booking characteristics:

| Feature | Importance |
|---|---:|
| Country | 0.2500 |
| Market Segment | 0.1615 |
| Lead Time | 0.1575 |
| Customer Type | 0.0941 |
| Previous Cancellations | 0.0856 |

These features contribute to the model's ability to distinguish bookings with different cancellation risks.

## Interpretation

Lead time represents how far in advance a reservation is made, while previous cancellations provide information about historical booking behavior.

Market segment and customer type describe booking characteristics that help the model distinguish cancellation-risk patterns.

Country was highly influential in the fitted model. However, this may partly reflect dataset-specific geographic patterns and the large number of encoded country categories.

## Evidence

The interpretation is based on the final Random Forest model's feature importance scores, extracted after fitting the preprocessing and classification pipeline on the complete training dataset.

The model was independently evaluated on 23,876 held-out test bookings, correctly identifying 6,676 cancellations.

## Caution Against Causal Claims

Feature importance measures contribution to model predictions, not causal influence or the direction of an effect.

Therefore, the findings do not establish that a particular country, market segment, or booking characteristic causes cancellations.

Country-related predictions require particular caution to avoid unfair customer treatment. The results should support hotel operational planning rather than discriminatory decisions.