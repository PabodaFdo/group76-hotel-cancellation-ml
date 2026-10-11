# Member 2 — Business Actions

**Owner:** IT24103767

## 1. Business Objective

The objective is to support hotel revenue management and operations teams in identifying bookings with a higher likelihood of cancellation.

Early identification of potential cancellations can help hotels improve reservation monitoring, occupancy planning, and resource allocation.

## 2. Recommended Business Actions

### Reservation Follow-Up

Bookings classified as higher cancellation risk can be prioritized for appropriate reservation confirmation reminders and customer follow-up.

The selected Random Forest model uses a classification threshold of 0.40 to identify bookings requiring additional attention.

### Revenue and Occupancy Planning

Hotel revenue managers can use aggregated cancellation-risk predictions to support occupancy forecasts and anticipate possible room availability changes.

This information can complement existing reservation data when developing pricing and inventory strategies.

### Operational Resource Allocation

Operations managers can consider predicted cancellation patterns when planning housekeeping schedules, staffing requirements, and other hotel resources.

Risk predictions should support operational planning rather than directly determine staffing or room allocation decisions.

## 3. Supporting Model Evidence

The selected Random Forest model achieved the following results on 23,876 held-out test bookings:

| Metric | Result |
|---|---:|
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| PR-AUC | 0.8434 |

The model correctly identified 6,676 actual cancellations while generating 2,678 false cancellation alerts and missing 2,242 cancellations.

These results demonstrate useful cancellation-detection capability, but predictions are not always correct.

## 4. Implementation Considerations

Predictions should be incorporated into an appropriate reservation-monitoring process with human oversight.

Hotel staff should review risk alerts before taking action. High-risk predictions should not automatically trigger reservation cancellation, penalties, or overbooking.

The effectiveness of recommended actions should be evaluated using business outcomes such as reservation confirmation rates, occupancy forecasting accuracy, and operational costs.

## 5. Recommendation

Use the selected Random Forest model as a decision-support tool for proactive reservation monitoring and hotel operational planning.

A controlled pilot with recent booking data is recommended before implementation. This would allow hotel management to assess the practical value of predictions, the cost of false alerts, and the suitability of the selected threshold.