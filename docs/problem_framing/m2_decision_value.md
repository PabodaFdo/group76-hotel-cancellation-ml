# Member 2 — Decision Need and Business Value

**Owner:** IT24103767

## Decision Need

Hotel revenue management and operations teams need a way to identify bookings that may have a higher risk of cancellation before the final booking outcome is known.

The purpose of the proposed machine-learning model is to support this decision by providing cancellation-risk information for individual bookings. This information can help hotel decision-makers distinguish between relatively lower-risk and higher-risk reservations and consider that uncertainty when making operational and revenue-planning decisions.

The prediction is intended to support decisions such as:

- Prioritizing bookings that may require closer monitoring
- Supporting occupancy and revenue forecasting
- Informing reasonable overbooking and room-allocation planning
- Supporting customer communication or retention efforts where appropriate
- Improving staffing and resource planning when cancellation risk may affect expected occupancy

The model should not automatically cancel, reject, penalize, or otherwise make decisions about customers. The predicted risk should be treated as additional information for human decision-makers.

## Intended Decision Timing

The cancellation-risk prediction should after a reservation is created but before its final outcome is known.

At the selected prediction point, the model should only use information that would genuinely be available to the hotel at that time.

This timing is important because information recorded only after a cancellation or after the final reservation outcome could create data leakage and produce unrealistic model performance.

The exact set of features available at prediction time will therefore be reviewed during the later leakage and preprocessing stage before the final model is trained.

## Potential Business Value

### Booking Reliability

Cancellation-risk predictions can give hotel teams a clearer view of the uncertainty associated with future reservations. Instead of treating every booking as equally reliable, the hotel can consider differences in estimated cancellation risk when planning expected occupancy.

### Revenue Planning

Risk information can support more realistic forecasting of expected room demand and revenue. When a large number of future bookings are estimated to have higher cancellation risk, revenue managers can consider this uncertainty when reviewing forecasts and planning inventory.

### Operational Planning

Changes in expected occupancy can affect housekeeping, staffing, room preparation, and other hotel resources.Cancellation-risk information may therefore help operations teams make better-informed planning decisions.

### Customer Management

Bookings with relatively higher predicted cancellation risk could be considered for appropriate customer-management actions, such as confirmation reminders or other reasonable engagement strategies. These actions should be applied carefully and should not assume that a high-risk booking will definitely be cancelled.

### Decision Prioritization

A cancellation-risk probability can also help decision-makers rank or prioritize bookings instead of relying only on a simple cancelled/not-cancelled prediction. This can make the model more useful when hotel staff need to focus attention on a smaller number of relatively higher-risk bookings.


## Evidence / Reasoning
1. *Alignment with the Business Scenario:*  
   The assignment scenario states that the hotel aims to improve booking reliability, revenue planning, and customer management. Cancellation-risk information directly supports these decision areas.

2. *Clear Decision-Support Role:*  
   The project is not intended to automate hotel management decisions. Instead, the model provides predictive information that can be considered together with operational knowledge, business policies, and human judgement.

3. *Connection to the ML Output:*  
   The proposed binary classification task produces a predicted cancellation outcome and, where supported by the selected model, a cancellation-risk probability. These outputs can be translated into practical risk information for hotel decision-makers.

4. *Importance of Prediction Timing:*  
   For the prediction to be useful in practice, it must be based only on information available before the final cancellation outcome is known. This creates a clear requirement for later feature-availability and leakage review.

5. *Practical Business Relevance:*  
   Cancellation risk is relevant to several connected hotel decisions, including occupancy forecasting, revenue planning, resource allocation, and customer management. Using one focused prediction task therefore has potential value across multiple business functions without turning them into separate machine-learning objectives.

6. *Responsible Use:*  
   A predicted high cancellation risk represents uncertainty rather than certainty. Final decisions should remain under human oversight, and predictions should not be used as the sole basis for unfair or automatic treatment of customers.


