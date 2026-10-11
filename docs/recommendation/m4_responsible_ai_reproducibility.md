# Member 4 — Responsible AI and Reproducibility

**Owner:** IT24104068


## 1. Overview

The Hotel Booking Cancellation Risk Prediction project was developed to support hotel revenue management and operational planning.

Responsible AI considerations and reproducible machine learning practices were incorporated into the project to support reliable evaluation, transparent reporting, and appropriate use of predictions.

## 2. Responsible AI Considerations

### Fairness and Potential Bias

The final Random Forest model identified country, market segment, lead time, customer type, and previous cancellations as influential features.

Country and customer-related variables may reflect historical booking patterns or dataset-specific relationships. Their use could create unfair outcomes if predictions are applied differently to customers based on geographic or demographic characteristics.

The project did not conduct a comprehensive subgroup fairness evaluation. Further fairness testing is recommended before operational deployment.

### Transparency and Interpretability

Random Forest feature importance was used to identify influential booking characteristics.

The results provide insight into model behavior but do not establish causal relationships or indicate whether individual features increase or decrease cancellation risk.

Hotel management should understand these limitations when interpreting model predictions.

### Human Oversight

Cancellation-risk predictions should support hotel staff rather than replace human decision-making.

High-risk predictions may be used to prioritize reservation monitoring or appropriate follow-up communication. They should not automatically trigger booking cancellations, penalties, or discriminatory customer treatment.

### Privacy and Data Protection

Guest reservation information should be handled securely, with appropriate access restrictions and data minimization.

Any operational implementation should comply with applicable privacy and data protection requirements.

## 3. Reproducibility Practices

### Consistent Data Preparation

The project used the validated dataset:

`data/processed/hotel_bookings_validated_phase3.csv`

After data cleaning, the dataset contained 119,210 records.

All classification models used the same 21 approved input features and the target variable `is_canceled`.

### Shared Preprocessing Pipeline

The preprocessing implementation is maintained in:

`src/preprocessing/pipeline.py`

Numerical variables were processed using median imputation and StandardScaler. Categorical variables were processed using most-frequent imputation and OneHotEncoder.

Preprocessing was included within each model pipeline and fitted separately within cross-validation training folds.

### Consistent Training and Validation

The saved data split is maintained in:

`results/splits/group_holdout_indices.npz`

The project used:

- Training dataset: 95,334 records
- Held-out test dataset: 23,876 records
- Five-fold StratifiedGroupKFold cross-validation
- Random state: 42

Identical model-input combinations were grouped to reduce overlap between training and validation/test partitions.

### Experiment Documentation

Separate notebooks document the original model development and hyperparameter tuning for Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting.

Model evaluation results and tuning outcomes are stored in `results/metrics/`.

The final comparison, threshold analysis, model selection, and held-out test evaluation are documented in:

`notebooks/04_final/final_group_notebook.ipynb`

These files provide a reproducible record of the modelling workflow, subject to using compatible software versions and the same dataset.

## 4. Final Model Verification

The tuned Random Forest was selected using development-data model comparison and out-of-fold threshold analysis.

The classification threshold of 0.40 was selected before evaluating the held-out test dataset.

The independent test evaluation achieved:

| Metric | Result |
|---|---:|
| Accuracy | 0.7939 |
| Precision | 0.7137 |
| Recall | 0.7486 |
| F1-score | 0.7307 |
| ROC-AUC | 0.8857 |
| PR-AUC | 0.8434 |

The model and threshold were not adjusted based on the final test results.

## 5. Recommendations for Responsible Deployment

Before operational use, the hotel should:

- Evaluate model performance on recent and representative booking data.
- Assess prediction errors and potential unfair outcomes across relevant customer groups.
- Monitor prediction quality and changes in booking patterns.
- Maintain human oversight of decisions affecting customers.
- Apply appropriate privacy and information security controls.

## 6. Conclusion

The project followed consistent preprocessing, documented modelling experiments, group-aware validation, and an independent final test evaluation.

These practices support reproducibility and transparent evaluation. However, successful offline testing does not establish that the model is ready for unrestricted operational deployment.

Further fairness assessment, business validation, and ongoing monitoring are necessary before using cancellation-risk predictions in hotel operations.