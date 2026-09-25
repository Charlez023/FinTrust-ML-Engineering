# Week 2 Model Evaluation

A baseline Logistic Regression model was developed to predict whether a transaction requires risk review. Logistic Regression was selected as the initial model because it provides a simple and interpretable baseline for the classification task.

The data was divided into training and testing sets using an 80/20 split. Stratification was used to maintain the target class distribution in both sets. This resulted in 9,600 training records and 2,400 testing records.

The preprocessing and model were combined into a scikit-learn pipeline. Numerical features were imputed and scaled, while categorical features were imputed and one-hot encoded. The model also used balanced class weights to account for the imbalance in the target variable.

The baseline model achieved 61% overall accuracy on the test set. For the `Yes` class, which represents transactions requiring risk review, the model achieved 65% recall, 28% precision, and an F1-score of 0.40.

The confusion matrix showed 305 correctly identified `Yes` transactions and 165 `Yes` transactions that were missed. It also showed 766 transactions that were predicted as `Yes` when their actual label was `No`.

The results show that the model can identify a portion of transactions requiring risk review, but it also produces a relatively high number of false positives. The baseline therefore provides a starting point for further model development rather than a final solution.

Because the target variable is imbalanced, the evaluation focused on class-specific precision, recall, and F1-score rather than relying only on accuracy. Further work could explore additional features, alternative models, and further evaluation to determine whether performance can be improved.