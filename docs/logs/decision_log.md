# Decision Log

This log records the main decisions made during the Group 76 Machine Learning project. Each decision includes the alternatives considered, supporting reasoning, and the final agreed direction.

---

## D01 - Selection of Primary Decision Lens

**Date:** 2026-09-08  
**Phase:** Phase 1 - Business Problem Framing  
**Owners involved:** Group 76

### Question

Which decision lens should be used as the primary focus of the Hotel Booking Demand project?

### Options considered

1. Cancellation risk
2. Booking/customer segmentation
3. Operational planning support

### Evidence

The assigned Tourism and Hospitality scenario focuses on improving booking reliability, revenue planning, and customer management.

The assignment descriptor identifies cancellation risk, booking/customer segmentation, and operational planning support as possible decision lenses for the Hotel Booking Demand dataset.

Cancellation risk provides a focused problem that can be translated into a clear predictive machine-learning task.

### Final decision

**Cancellation risk** was selected as the primary decision lens.

### Why selected

Cancellation risk directly addresses uncertainty in hotel bookings and supports the project's goal of improving booking reliability.

It also provides a clear connection between the business problem and a classification-based machine-learning task.

### Rejected options and reasons

**Booking/customer segmentation:**  
Not selected as the primary lens because it represents a different analytical objective and would reduce the focus of the project.

**Operational planning support:**  
Not selected as a separate primary lens because operational planning can instead be treated as a business use of the cancellation-risk predictions.

### Files affected

- `docs/problem_framing/m1_stakeholder_problem.md`
- `docs/problem_framing/m2_decision_value.md`
- `docs/problem_framing/m3_ml_task_output.md`
- `docs/problem_framing/m4_lens_scope.md`
- `docs/problem_framing/final_problem_framing.md`

---

## D02 - Selection of Machine Learning Task and Output

**Date:** 2026-09-08  
**Phase:** Phase 1 - Business Problem Framing  
**Owners involved:** Group 76

### Question

What machine-learning task should be used to address the selected cancellation-risk lens?

### Options considered

1. Binary classification
2. Customer segmentation
3. General descriptive analysis

### Evidence

The project aims to distinguish between bookings that are cancelled and bookings that are not cancelled.

The selected target variable is `is_canceled`, which represents the final cancellation outcome for each booking.

The required technical output therefore contains two possible classes.

### Final decision

The project will use **binary classification**.

### Unit of analysis

One hotel booking.

### Target

`is_canceled`

- `0` = booking not cancelled
- `1` = booking cancelled

### Expected output

The primary output will be a predicted cancellation class.

Where supported by the selected model, a cancellation-risk probability will also be produced to provide more informative decision support.

### Why selected

Binary classification directly matches the two possible cancellation outcomes and supports the selected cancellation-risk business lens.

### Rejected options and reasons

**Customer segmentation:**  
Rejected because it groups similar bookings or customers rather than directly predicting cancellation outcome.

**General descriptive analysis:**  
Useful during EDA, but it does not provide the predictive output required for the selected business problem.

### Files affected

- `docs/problem_framing/m3_ml_task_output.md`
- `docs/problem_framing/final_problem_framing.md`

---

## D03 - Selection of Project Workflow

**Date:** 2026-09-08  
**Phase:** Phase 1 - Business Problem Framing  
**Owners involved:** Group 76

### Question

What workflow should be followed to ensure that the project moves logically from the business problem to an evidence-based recommendation?

### Options considered

1. Begin directly with model training
2. Perform data analysis and then select models without formal business framing
3. Use a structured workflow from business framing through data understanding, preprocessing, modelling, evaluation, interpretation, and recommendation

### Evidence

The assignment requires evidence of business problem framing, workflow reasoning, data understanding, preprocessing decisions, model comparison, evaluation, recommendations, limitations, and responsible AI.

Starting with modelling before understanding the business problem or dataset could lead to weak justification, inappropriate features, or data leakage.

### Final decision

The group selected a structured end-to-end machine-learning workflow:

1. Business Problem and Stakeholder
2. Selection of Cancellation-Risk Lens
3. Business Question and ML Task Definition
4. Data Understanding
5. Data Quality Assessment and EDA
6. Feature Availability and Leakage Review
7. Preprocessing and Feature Engineering
8. Validation Strategy
9. Baseline Model
10. Alternative Classification Models
11. Model Evaluation and Comparison
12. Final Model Selection
13. Model Interpretation
14. Business Recommendation
15. Limitations and Responsible AI

### Why selected

This workflow maintains a clear connection between the business problem, technical decisions, model evaluation, and final stakeholder recommendation.

It also helps ensure that data-quality and leakage issues are considered before modelling.

### Rejected options and reasons

**Starting directly with modelling:**  
Rejected because the business task, data quality, leakage risks, and preprocessing decisions must be understood first.

**EDA followed immediately by modelling:**  
Rejected because it does not explicitly include feature-availability review, preprocessing justification, validation planning, or decision documentation.

### Files affected

- `docs/workflow/workflow_source.md`
- `docs/workflow/workflow_diagram.png`
- `docs/problem_framing/final_problem_framing.md`