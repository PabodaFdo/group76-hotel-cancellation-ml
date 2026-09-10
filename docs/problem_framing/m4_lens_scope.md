# Member 4 — Lens, Scope, Constraints and Risks

**Owner:** IT24104068

## 1. Primary Decision Lens

The primary decision lens selected for Group 76 is hotel booking cancellation risk.

Hotel booking cancellations can create uncertainty for hotel management in areas
such as booking reliability, revenue planning and customer management. Therefore,
using historical booking information to identify bookings with a higher likelihood
of cancellation could support better planning and decision-making.

The project will focus on investigating whether machine-learning models can
predict cancellation risk using the available Hotel Booking Demand dataset.

 2. Why Cancellation Risk is the Primary Lens

Cancellation risk was selected as the primary lens because it provides one clear
and focused machine-learning problem that is directly connected to the business
scenario.

Customer segmentation and general operational planning are also relevant to the
hotel context, but they will not be treated as separate primary objectives.
Instead, they may be discussed as possible business uses or implications of the
cancellation-risk predictions.

Keeping one main objective helps the project remain coherent and makes the model
comparison and evaluation more meaningful.

3. Project Scope

The scope of the project is to develop and compare machine-learning classification
models that can identify bookings with a higher risk of cancellation.

The intended model output is a predicted cancellation class and, where appropriate,
a cancellation-risk probability.

The model is intended to support hotel management decisions. It is not intended to:

- build a complete hotel reservation software system
- automatically reject or cancel customer bookings
- guarantee that a cancellation can be prevented
- guarantee improved revenue
- prove that any individual booking feature causes cancellation

 4. Early Constraints and Risks

4.1 Data Leakage

A major risk is data leakage. Some variables may contain information that would
only be available after the booking outcome is already known.

For each predictor, the group should ask whether the hotel would genuinely know
that information at the time the cancellation-risk prediction is required.
Variables that contain future information should be removed or carefully justified.

4.2 Class Imbalance

The cancellation and non-cancellation classes may not occur in equal proportions.
The actual class distribution must be examined before deciding whether an
imbalance treatment is necessary.

Any treatment for imbalance should be based on evidence from the dataset rather
than applied automatically.

 4.3 Data Quality

The dataset may contain missing values, duplicate records, unusual values,
inconsistent categories or other quality issues.

These issues must first be identified during data understanding and EDA, and the
group should justify how they are handled during preprocessing.

4.4 Changing Behaviour

The dataset represents historical booking behaviour. Customer behaviour, tourism
patterns or hotel policies may change over time, so future data may not always
follow the same patterns as the historical dataset.

Therefore, the model should not be treated as permanently accurate without
monitoring and future re-evaluation.

 5. What Project Success Means

Project success should not be defined only by achieving high classification
accuracy.

The group should also consider:

- precision
- recall
- F1-score
- ROC-AUC where appropriate
- false-positive and false-negative errors
- validation performance
- evidence of overfitting or underfitting
- interpretability
- leakage prevention
- reproducibility
- usefulness to hotel decision-makers

The final model should therefore be selected using both machine-learning evidence
and business relevance rather than automatically choosing the model with the
highest accuracy.

 6. Summary

The project will use cancellation risk as its single primary decision lens.
The goal is to develop a defensible machine-learning classification approach that
can support hotel management with cancellation-risk information while recognising
data limitations, prediction errors and responsible-use constraints.
