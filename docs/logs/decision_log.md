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

---

## D04 - Data Cleaning and Duplicate Handling Strategy

**Phase:** Data Understanding and Preprocessing  
**Owners involved:** Group 76

### Question

How should missing values, invalid records, and exact duplicate bookings be handled without unnecessarily removing potentially valid observations?

### Options considered

1. Remove all records containing missing values or duplicates.
2. Apply targeted cleaning while retaining exact duplicate records.
3. Retain all records without addressing identified data-quality issues.

### Evidence

The original Hotel Booking Demand dataset contained **119,390 records and 32 columns**.

Data quality assessment identified:

- 31,994 exact duplicate rows beyond their first occurrences.
- Four missing values in `children`.
- 488 missing values in `country`.
- 180 records containing zero total guests.
- One negative ADR value.

The published dataset does not contain a unique reservation identifier that can establish whether identical records represent separate genuine bookings or accidental duplication.

### Final decision

Apply targeted cleaning and retain exact duplicate records in the primary dataset.

The cleaning decisions were:

- Replace missing `children` values with zero.
- Replace missing `country` values with `"Unknown"`.
- Remove 180 zero-guest records.
- Retain exact duplicate rows because their identities cannot be verified.
- Retain the negative ADR record in the validated dataset because ADR is excluded from modelling.
- Retain `agent` and `company` in the validated dataset but exclude them from model inputs.

**Outcome:** The validated dataset contains 119,210 records and 32 columns.

### Duplicate Sensitivity Experiment

A supplementary experiment was conducted to investigate whether removing exact duplicate records changes model performance.

Two Random Forest approaches were evaluated:

**Approach A:** Retain all records within each training fold.

**Approach B:** Remove exact duplicate records using all 32 columns within each training fold.

Both approaches used identical five-fold group-aware validation splits, the same model configuration, and a fixed classification threshold of 0.40. Validation records were unchanged, and the held-out test set was not used.

### Experimental results

| Metric | Keep Duplicates | Remove Duplicates |
|---|---:|---:|
| Precision | 0.7220 | 0.7745 |
| Recall | 0.7453 | 0.6076 |
| F1-score | 0.7333 | 0.6805 |
| PR-AUC | 0.8420 | 0.8223 |

Removing duplicates increased precision but reduced recall, F1-score, and PR-AUC on the original validation distribution.

### Why selected

Retaining duplicates preserves the recorded booking distribution without assuming that identical records are erroneous.

The sensitivity experiment demonstrated that duplicate handling materially affects model predictions. However, it cannot establish whether the identical records represent genuine separate bookings or extraction errors.

The comparison also used a threshold originally selected for the duplicate-retaining model, meaning the classification metrics do not represent separately optimized thresholds for both approaches.

### Rejected options and reasons

**Removing all exact duplicates:**  
Not selected for the primary workflow because the dataset lacks identifiers needed to verify which repeated records are errors. Removing all repeated records could discard legitimate booking observations and change the recorded cancellation distribution.

**Keeping invalid records without cleaning:**  
Rejected because missing values and zero-guest bookings required appropriate data-quality treatment.

### Final decision after sensitivity analysis

**Retain exact duplicate records in the primary modelling workflow**, while documenting the uncertainty surrounding their identities and the observed sensitivity of model performance to duplicate handling.

The supplementary experiment does not replace the final selected model or its original held-out test evaluation.

### Files affected

- `notebooks/02_preprocessing/m1_cleaning.ipynb`
- `notebooks/04_final/duplicate_sensitivity.ipynb`
- `data/processed/hotel_bookings_validated_phase3.csv`
- `docs/logs/preprocessing_feature_log.md`

---

## D05 - Leakage Prevention, Feature Selection and Validation Strategy

**Phase:** Preprocessing and Validation  
**Owners involved:** Group 76

### Question

How can the models predict booking cancellation risk using appropriate information while minimizing data leakage and producing reliable evaluation results?

### Options considered

1. Use all available dataset columns as model inputs.
2. Select features based on their availability at booking confirmation and apply conventional random splitting.
3. Select approved booking-time features and use group-aware data splitting and cross-validation.

### Evidence

The objective is to estimate cancellation risk immediately after booking confirmation.

Some dataset attributes contain information that becomes available after booking confirmation or directly reveals the final reservation outcome.

Furthermore, the dataset contains repeated feature combinations that could introduce overlap between training and evaluation partitions under conventional random splitting.

### Final decision

Use **21 approved model features**, consisting of 13 numerical and 8 categorical variables.

The following ten columns were excluded from model inputs:

- `reservation_status`
- `reservation_status_date`
- `assigned_room_type`
- `booking_changes`
- `deposit_type`
- `agent`
- `company`
- `adr`
- `required_car_parking_spaces`
- `total_of_special_requests`

The first two columns directly reveal reservation outcome information. The remaining exclusions reflect prediction-time availability uncertainty, potential leakage concerns, or modelling-scope decisions.

The target variable `is_canceled` was kept separate from model inputs.

### Validation strategy

An approximately 80/20 group-aware holdout split was established:

| Dataset | Records |
|---|---:|
| Training | 95,334 |
| Held-out test | 23,876 |

Identical combinations of the approved input features were assigned to groups using feature hashes.

Five-fold `StratifiedGroupKFold` cross-validation was used during model evaluation.

The shared preprocessing pipeline was fitted within training folds rather than before cross-validation.

### Why selected

This approach reduces the risk of information leakage, limits overlap between identical model-input combinations, and provides consistent evaluation conditions for all candidate models.

The held-out test set was reserved for evaluation after the final model and classification threshold had been selected.

### Rejected options and reasons

**Using all available columns:**  
Rejected because some variables directly reveal outcomes or may not be known when the cancellation-risk prediction is required.

**Conventional random splitting without grouping:**  
Not selected because repeated input combinations could appear across training and evaluation partitions.

### Limitations

Group-aware validation does not establish future-period generalization because the split is not strictly chronological.

### Files affected

- `notebooks/02_preprocessing/m2_encoding_scaling.ipynb`
- `notebooks/02_preprocessing/m3_leakage_validation.ipynb`
- `src/preprocessing/pipeline.py`
- `results/splits/group_holdout_indices.npz`

---

## D06 - Model Development and Hyperparameter Tuning

**Phase:** Model Development and Evaluation  
**Owners involved:** Group 76

### Question

Which classification models should be evaluated, and how should hyperparameters be selected to support a fair comparison?

### Options considered

1. Use a single classification algorithm.
2. Compare multiple models using only their default configurations.
3. Evaluate a baseline and alternative classifiers, perform limited hyperparameter tuning, and compare performance using consistent validation methods.

### Evidence

Different classification models may perform differently when identifying bookings at risk of cancellation.

The business problem requires attention to cancellation recall, precision, and the balance between missed cancellations and false alerts.

### Final decision

Evaluate five classification approaches:

1. Dummy Classifier
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. Gradient Boosting

Use the shared preprocessing pipeline and group-aware validation strategy for all models.

Hyperparameter tuning was performed using three-fold group-aware cross-validation, with **PR-AUC as the optimization metric**.

The selected configurations were subsequently compared using five-fold cross-validation.

### Model tuning outcomes

| Model | Preferred Configuration | F1-score | PR-AUC |
|---|---|---:|---:|
| Dummy Classifier | Prior baseline | 0.0000 | 0.3698 |
| Logistic Regression | Original | 0.6622 | 0.7906 |
| Decision Tree | Tuned | 0.7135 | 0.8177 |
| Random Forest | Tuned | 0.6301 | 0.8420 |
| Gradient Boosting | Original | 0.6463 | 0.8177 |

### Key findings

**Logistic Regression:**  
The tuning process selected the original configuration with `C=1` and `class_weight=None`.

**Decision Tree:**  
The tuned configuration improved recall and F1-score at the default classification threshold.

**Random Forest:**  
The tuned configuration achieved the highest PR-AUC among the evaluated models, although recall was relatively low at the default threshold.

**Gradient Boosting:**  
The original configuration with 100 estimators performed better than the best configuration identified in the limited tuning search.

### Why selected

Comparing multiple classification algorithms provides evidence for choosing a model based on predictive performance and operational requirements rather than relying on a single algorithm.

PR-AUC was emphasized because the objective involves identifying cancellations while accounting for prediction precision.

### Rejected options and reasons

**Using only one model:**  
Rejected because it would not provide sufficient evidence for model comparison and selection.

**Selecting the model using accuracy alone:**  
Rejected because accuracy does not adequately describe the trade-off between missed cancellations and false alerts.

### Files affected

- `notebooks/03_modelling/m1_baseline_logistic.ipynb`
- `notebooks/03_modelling/m2_decision_tree.ipynb`
- `notebooks/03_modelling/m3_random_forest.ipynb`
- `notebooks/03_modelling/m4_gradient_boosting.ipynb`
- `results/metrics/`
- `docs/logs/model_comparison.md`

---

## D07 - Final Model and Classification Threshold Selection

**Phase:** Final Model Selection and Evaluation  
**Owners involved:** Group 76

### Question

Which model and classification threshold provide the most suitable balance between cancellation detection and false cancellation alerts?

### Options considered

1. Tuned Decision Tree using the default threshold.
2. Tuned Random Forest using the default threshold.
3. Compare threshold-adjusted Random Forest and Decision Tree models using development-data predictions.

### Evidence

Initial cross-validation showed that the tuned Decision Tree achieved the highest default-threshold F1-score and recall.

However, the tuned Random Forest achieved the highest PR-AUC, indicating stronger overall precision–recall ranking performance.

The Random Forest's relatively low recall at the default threshold suggested that threshold adjustment could improve cancellation detection.

### Threshold analysis

Out-of-fold cancellation probabilities were generated using five-fold group-aware cross-validation on the training dataset.

Several classification thresholds were evaluated without accessing the held-out test set.

| Model | Selected Threshold | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Random Forest (Tuned) | 0.40 | 0.7225 | 0.7452 | 0.7337 |
| Decision Tree (Tuned) | 0.45 | 0.6284 | 0.8291 | 0.7149 |

The Random Forest achieved the highest observed F1-score among the evaluated threshold-adjusted configurations.

The Decision Tree achieved higher recall, but the Random Forest provided higher precision and F1-score at the selected thresholds.

### Final decision

Select the **tuned Random Forest classifier with a classification threshold of 0.40**.

The final configuration is:

- `n_estimators = 100`
- `max_depth = 15`
- `min_samples_leaf = 5`
- `class_weight = None`
- `random_state = 42`
- `threshold = 0.40`

### Why selected

The tuned Random Forest achieved the highest cross-validation PR-AUC of 0.8420.

Threshold adjustment improved its observed F1-score from approximately 0.6301 at the default threshold to 0.7337 at threshold 0.40, based on pooled out-of-fold development predictions.

This provided a more suitable balance between precision and recall for cancellation-risk decision support.

The threshold was fixed before final test evaluation.

### Independent test evaluation

The selected model was fitted using all 95,334 training records and evaluated on 23,876 held-out test records.

| Metric | Final Test Result |
|---|---:|
| Accuracy | 0.7939 |
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| ROC-AUC | 0.8857 |
| PR-AUC | 0.8434 |

### Final confusion matrix

| Outcome | Count |
|---|---:|
| True Negatives | 12,280 |
| False Positives | 2,678 |
| False Negatives | 2,242 |
| True Positives | 6,676 |

The model correctly identified 6,676 cancellations while missing 2,242 cancellations.

It also generated 2,678 false cancellation alerts, highlighting the importance of human review before operational actions are taken.

### Business recommendation

Use predicted cancellation risk to support reservation monitoring, occupancy planning, and operational resource allocation.

High-risk predictions may help prioritize appropriate reservation follow-up, but they should not independently trigger booking cancellations, customer penalties, or overbooking decisions.

### Limitations

The selected classification threshold was optimized for F1-score rather than measured financial costs.

Further validation using future-period booking data, fairness assessment, and operational cost analysis would be necessary before deployment.

### Files affected

- `notebooks/04_final/final_group_notebook.ipynb`
- `results/metrics/final_random_forest_test_results.csv`
- `docs/logs/model_comparison.md`
- `docs/recommendation/final_recommendation.md`

---

## Overall Decision Summary

| Decision | Final Direction |
|---|---|
| D01 - Decision Lens | Cancellation risk |
| D02 - ML Task | Binary classification |
| D03 - Workflow | Structured end-to-end ML workflow |
| D04 - Data Cleaning | Targeted cleaning and retention of exact duplicates, supported by sensitivity analysis |
| D05 - Validation | Approved 21 features and group-aware splitting |
| D06 - Model Development | Baseline and four classification algorithms with hyperparameter tuning |
| D07 - Final Model | Tuned Random Forest with threshold 0.40 |

The final project decisions were based on the business objective, dataset characteristics, controlled model evaluation, and the results of additional experiments.

The completed workflow supports cancellation-risk prediction as a decision-support application while acknowledging limitations involving duplicate records, model generalization, prediction errors, and responsible AI.