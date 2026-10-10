# Member 3 — Limitations and Risks

**Owner:** IT24103815

## 1. Overview

The project developed a Random Forest classification model to predict hotel booking cancellations using information available at booking confirmation.

Although the selected model demonstrated promising performance, several limitations and operational risks must be considered before practical deployment.

## 2. Dataset Limitations

### Historical Data

The model was developed using historical hotel booking records. Changes in customer behavior, cancellation policies, travel demand, or market conditions may reduce its performance over time.

### Generalization

The dataset represents a limited hotel context. Performance on different hotels, geographic regions, or future booking periods has not been independently established.

### Duplicate Records

Exact duplicate records were retained because no unique booking identifier was available to confirm whether they were erroneous. Although group-aware splitting reduced overlap between identical input patterns, the retained records may still affect observed data distributions.

## 3. Prediction Limitations

The selected Random Forest achieved the following results on the held-out test dataset:

| Metric | Result |
|---|---:|
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| PR-AUC | 0.8434 |

The final confusion matrix identified:

- **2,242 false negatives:** Actual cancellations that the model failed to identify.
- **2,678 false positives:** Bookings incorrectly flagged as likely cancellations.

These errors create different business risks. Missed cancellations may affect occupancy and revenue planning, while false alerts may lead to unnecessary customer follow-up and operational effort.

## 4. Model and Validation Limitations

The project used five-fold StratifiedGroupKFold cross-validation and a group-aware holdout split to reduce overlap between identical feature combinations.

However, this strategy does not fully reproduce real-world forecasting conditions because the evaluation was not based on a strictly chronological train/test split.

The classification threshold of 0.40 was selected to improve F1-score using development-data predictions. It was not optimized using actual financial costs or hotel-specific operational requirements.

Feature importance scores were calculated using Random Forest impurity-based importance. These scores can favor variables with many categories and should not be interpreted as causal relationships.

## 5. Operational and Ethical Risks

### Incorrect Business Decisions

Predictions should not independently trigger booking cancellations, customer penalties, or overbooking decisions. Incorrect predictions could create financial losses and negatively affect customer relationships.

### Fairness

Country and customer-related characteristics were influential in the model. These patterns may reflect dataset-specific characteristics and could create unfair treatment if risk scores are applied without safeguards.

### Data Privacy

Reservation information should be processed with appropriate access controls, data minimization, and compliance with applicable data protection requirements.

### Model Performance Changes

Cancellation patterns may change after deployment. Regular evaluation is necessary to identify performance deterioration and determine whether retraining is required.

## 6. Risk Mitigation Recommendations

- Conduct further validation using recent and representative booking records.
- Evaluate the operational costs of false positives and false negatives before adopting the selected threshold.
- Monitor prediction performance and potential unfair outcomes across relevant customer groups.
- Keep hotel staff involved in consequential reservation decisions.
- Establish appropriate privacy, security, and model maintenance procedures.

## 7. Conclusion

The selected Random Forest demonstrates useful cancellation-risk prediction performance, but its results do not eliminate uncertainty.

The model is best suited for supporting reservation monitoring, occupancy planning, and operational decisions rather than making automatic decisions about individual customers.

Further business validation, fairness assessment, and ongoing performance monitoring are recommended before deployment.