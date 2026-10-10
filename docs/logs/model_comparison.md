# Model Comparison — Group 76

## Evaluation Strategy

Five classification approaches were evaluated for hotel booking cancellation prediction: Dummy Classifier, Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting.

Models were compared using five-fold StratifiedGroupKFold cross-validation on the training data. Hyperparameter tuning was conducted using group-aware cross-validation, with PR-AUC as the tuning metric.

The held-out test set was reserved for evaluating the selected final model.

## Cross-Validation Results

| Model | Precision | Recall | F1-score | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|
| Dummy Classifier | 0.0000 | 0.0000 | 0.0000 | 0.5000 | 0.3698 |
| Logistic Regression | 0.7541 | 0.5909 | 0.6622 | 0.8421 | 0.7906 |
| Decision Tree (Tuned) | 0.6514 | 0.7907 | 0.7135 | 0.8704 | 0.8177 |
| Random Forest (Tuned) | 0.8891 | 0.4881 | 0.6301 | 0.8845 | 0.8420 |
| Gradient Boosting (Original) | 0.8213 | 0.5331 | 0.6463 | 0.8655 | 0.8177 |

The tuned Decision Tree achieved the highest default-threshold F1-score and recall. The tuned Random Forest achieved the highest PR-AUC and ROC-AUC.

## Threshold Analysis and Model Selection

Out-of-fold probability predictions were used to evaluate classification thresholds without accessing the held-out test set.

| Model | Selected Threshold | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Random Forest (Tuned) | 0.40 | 0.7225 | 0.7452 | 0.7337 |
| Decision Tree (Tuned) | 0.45 | 0.6284 | 0.8291 | 0.7149 |

Random Forest at threshold 0.40 achieved the highest F1-score among these evaluated configurations, while maintaining higher precision than the Decision Tree.

**Final selection:** Tuned Random Forest with a classification threshold of 0.40.

## Independent Test Evaluation

The selected model was trained on the complete training dataset and evaluated once on 23,876 held-out test bookings.

| Metric | Test Result |
|---|---:|
| Accuracy | 0.7939 |
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| ROC-AUC | 0.8857 |
| PR-AUC | 0.8434 |

The model correctly identified 6,676 cancellations and missed 2,242 cancellations. It also generated 2,678 false cancellation alerts.

## Final Decision

The tuned Random Forest was selected because of its strong PR-AUC and improved F1-score following threshold adjustment.

The independent test performance was close to the development-data results, supporting the selected model's generalization to the held-out sample.

Predictions are intended to support reservation follow-up, hotel revenue planning, and operational decisions. The model should not be used to automatically cancel reservations or make decisions without human oversight.

The final threshold was selected based on development-data F1-score. Business costs, fairness, and performance on future bookings require additional validation before deployment.