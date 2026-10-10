# Final Business Recommendation — Group 76

## 1. Business Problem

Hotel booking cancellations create uncertainty in room availability, expected revenue, and operational planning. Hotels need an effective way to identify reservations that may be cancelled so management teams can take appropriate preventive and planning actions.

The project addresses this problem by predicting booking cancellation risk using information available at the time of reservation.

## 2. Recommended Machine Learning Solution

The **tuned Random Forest classifier** was selected as the final model after comparing Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting against a Dummy Classifier baseline.

The selected model uses:

- 100 decision trees
- Maximum tree depth of 15
- Minimum leaf size of 5
- Classification threshold of 0.40

The threshold was selected using out-of-fold training predictions to improve the balance between precision and recall.

## 3. Final Model Performance

The selected model was evaluated on 23,876 held-out test bookings.

| Evaluation Metric | Final Result |
|---|---:|
| Accuracy | 79.39% |
| Precision | 71.37% |
| Recall | 74.86% |
| F1-score | 0.7307 |
| ROC-AUC | 0.8857 |
| PR-AUC | 0.8434 |

The model correctly identified 6,676 cancellations and missed 2,242 cancellations. It also generated 2,678 false cancellation alerts.

These results indicate that the model can identify a substantial proportion of bookings that eventually cancel, while maintaining a reasonable balance between correct alerts and false alarms.

## 4. Recommendations for Hotel Management

### Reservation Risk Monitoring

Use cancellation-risk predictions to support reservation monitoring. Higher-risk bookings can be prioritized for appropriate confirmation reminders or follow-up communication.

### Revenue and Occupancy Planning

Use aggregated cancellation-risk estimates as an additional input when forecasting expected room occupancy and identifying potential revenue uncertainty.

### Operational Resource Planning

Consider predicted cancellation patterns when planning housekeeping, staffing, and other operational resources. Predictions should complement existing booking information and management judgment.

### Human Decision Support

Present cancellation-risk predictions as supporting information rather than automatic decisions. A high-risk prediction should not independently trigger booking cancellation, customer penalties, or overbooking actions.

## 5. Model Interpretation

Feature importance analysis identified country, market segment, lead time, customer type, and previous cancellations as influential model inputs.

These findings suggest that reservation timing, booking characteristics, and historical booking behavior contribute to cancellation-risk predictions.

However, feature importance does not establish causation. In particular, geographic and customer-related patterns should not be used to justify unfair treatment of individual guests.

## 6. Limitations and Responsible AI

The model was trained using historical hotel booking data, and its performance may change with future booking patterns or at different hotels.

Although group-aware validation reduced overlap between identical feature combinations, performance was not independently established using a future-period dataset.

The selected threshold was optimized for F1-score rather than measured financial costs. Therefore, the hotel should evaluate the operational cost of false alerts against the cost of missed cancellations before deployment.

Fairness, data privacy, and changing model performance should also be reviewed regularly. Customer nationality or other sensitive contextual information should not be used for discriminatory decisions.

## 7. Final Recommendation

The tuned Random Forest with a 0.40 classification threshold is recommended as a **decision-support candidate for hotel cancellation-risk management**.

Its held-out test recall of 74.86% and F1-score of 0.7307 demonstrate useful predictive capability for identifying potentially cancelled reservations.

The most appropriate application is to support proactive reservation follow-up, occupancy forecasting, and operational planning, with human oversight.

Before operational deployment, the hotel should conduct further validation using recent booking data, assess financial impacts, and establish appropriate fairness and performance monitoring procedures.