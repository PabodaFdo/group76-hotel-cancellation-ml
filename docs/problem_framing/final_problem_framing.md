# Final Group Problem Framing

This document presents the agreed problem framing for Group 76 after reviewing and integrating the four individual member contributions.

## Stakeholder

The primary stakeholders are the **hotel revenue management and operations teams**.

These teams are responsible for areas such as occupancy and revenue planning, room allocation, staffing, resource preparation, and the operational management of future reservations. Booking cancellations create uncertainty in these activities because a confirmed reservation may not ultimately result in an occupied room.

Booking-system administrators and hotel management may also use cancellation-risk information to support planning and monitoring, while executive management may benefit indirectly from more informed revenue and operational forecasts.

The project therefore focuses on providing useful cancellation-risk information to hotel decision-makers rather than creating an automated reservation-management system.

## Decision Need

Hotel revenue and operations teams need a way to identify bookings that may have a **higher risk of cancellation before the final booking outcome is known**.

The proposed machine-learning model is intended to provide cancellation-risk information for individual bookings so that hotel decision-makers can consider booking uncertainty when making operational and revenue-planning decisions.

The prediction may support activities such as:

- identifying bookings that may require closer monitoring
- supporting occupancy and revenue forecasting
- informing reasonable room-allocation and overbooking planning
- supporting appropriate customer communication or retention activities
- improving staffing and operational resource planning

The prediction should be generated after a booking has been recorded but before its final cancellation or stay outcome is known.

Only information that would reasonably be available at this prediction point should be used as model input. Variables that reveal the final reservation outcome or become available only after that outcome must be reviewed for possible data leakage.

The model is intended as a **decision-support tool**. It should not automatically cancel, reject, penalize, or otherwise make decisions about customers.

## Primary Lens

The selected primary decision lens is **hotel booking cancellation risk**.

This lens directly supports the business scenario, in which the hotel aims to improve booking reliability, revenue planning, and customer management.

Cancellation risk was selected as the single primary lens because it provides a clear and focused prediction problem with a direct connection between the business need and the machine-learning task.

Customer segmentation and general operational planning are also relevant to the hotel context, but they will not be treated as separate primary objectives. Instead, they may be considered as possible applications or implications of the cancellation-risk predictions.

Keeping one primary lens allows the project to remain coherent and supports meaningful comparison and evaluation of classification models.

## Unit of Analysis

The unit of analysis is **one hotel booking**.

Each row in the Hotel Booking Demand dataset represents an individual booking record containing information related to the reservation, customer characteristics, stay details, and booking conditions.

The machine-learning model will therefore generate a cancellation-risk prediction for each individual booking.

## ML Task

The proposed machine-learning task is **binary classification**.

The objective is to use historical hotel booking information available at the selected prediction point to classify whether an individual booking is likely to be:

- **Cancelled**
- **Not Cancelled**

A baseline and alternative classification models will be developed and compared using a shared preprocessing, validation, and evaluation strategy.

Model evaluation will not rely on accuracy alone. Relevant measures such as precision, recall, F1-score, ROC-AUC where appropriate, confusion-matrix errors, validation performance, interpretability, leakage prevention, and business relevance will also be considered.

## Target / Output

The target variable is:

`is_canceled`

This variable represents the observed cancellation outcome of a booking:

- `1` = booking was cancelled
- `0` = booking was not cancelled

The **primary model output** will be a predicted cancellation class for each booking:

- Cancelled
- Not Cancelled

Where supported by the selected classification model, an **estimated cancellation-risk probability** will also be produced.

The probability can provide additional decision support because it allows bookings to be ranked according to their estimated cancellation risk rather than relying only on a binary class label.

For example, a booking with a relatively high predicted cancellation probability may require greater planning attention than a booking with a very low predicted probability.

A high predicted probability does not mean that a booking will definitely be cancelled. The output represents estimated risk and should be interpreted together with business knowledge and human judgement.

## Rationale

Hotel booking cancellations can create uncertainty in occupancy forecasting, revenue planning, room allocation, staffing, resource preparation, and customer management. A cancellation-risk model provides a way to use historical booking information to estimate this uncertainty before the final reservation outcome is known.

The selected framing is suitable for the project for the following reasons:

1. **Alignment with the business scenario**  
   The hotel aims to improve booking reliability, revenue planning, and customer management. Cancellation-risk prediction directly supports these decision areas.

2. **Clear decision-support purpose**  
   The prediction can help hotel teams distinguish between relatively lower-risk and higher-risk bookings when planning occupancy, revenue, resources, and appropriate customer-management activities.

3. **Clear machine-learning formulation**  
   The business problem can be formulated as a binary classification task using `is_canceled` as the target variable and one hotel booking as the unit of analysis.

4. **Useful model output**  
   A predicted cancellation class provides a clear outcome, while a cancellation-risk probability can provide more detailed information for prioritisation and planning.

5. **Appropriate project scope**  
   The project focuses on prediction and decision support rather than building a complete hotel reservation system, automatically making customer decisions, guaranteeing cancellation prevention, or guaranteeing increased revenue.

6. **Leakage-aware prediction boundary**  
   The model should use only information that would genuinely be available when the hotel requires the prediction. Feature availability will therefore be reviewed before modelling to prevent future information from creating unrealistic model performance.

7. **Evidence-based evaluation**  
   Project success will not be defined only by classification accuracy. Validation performance, precision, recall, F1-score, ROC-AUC where appropriate, false-positive and false-negative errors, interpretability, reproducibility, and business usefulness will also be considered.

8. **Responsible use**  
   Cancellation predictions represent uncertainty rather than certainty. Human oversight should remain part of operational decisions, and predictions should not be used as the sole basis for unfair or automatic treatment of customers.

## Final Agreed Project Definition

**Business question:**  
Can historical booking information available before the final booking outcome identify hotel bookings with a higher risk of cancellation?

**Primary stakeholder:**  
Hotel revenue management and operations teams

**Primary lens:**  
Hotel booking cancellation risk

**Unit of analysis:**  
One hotel booking

**Machine-learning task:**  
Binary classification

**Target:**  
`is_canceled`

**Primary output:**  
Predicted cancellation class

**Additional output:**  
Cancellation-risk probability, where supported

**Business purpose:**  
Support booking reliability, revenue planning, operational planning, and appropriate customer-management decisions.