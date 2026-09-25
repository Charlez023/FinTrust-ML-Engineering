# Week 2 Overview

## Analyze, Prepare, Develop, Test/Evaluate, and Document

Week 2 focused on moving the FinTrust Machine Learning Engineering work from planning into practical implementation. Building on the Week 1 architecture and requirements, I worked with the provided customer and transaction datasets and implemented the main components of the planned ML workflow.

The first step was data validation. A validation component was created to confirm that the datasets are available, contain records, have no duplicate rows, and have complete customer identifiers and target values. The validation checks passed successfully.

I then implemented a preprocessing workflow that joins the customer and transaction datasets using `Customer_ID`. The workflow converts transaction timestamps into usable time features, separates the target variable, handles missing values, and converts categorical data into numerical features.

A baseline Logistic Regression model was developed using a scikit-learn pipeline. The pipeline combines preprocessing with model training and uses balanced class weights because the target variable is imbalanced. The data was split into training and testing sets, and the model was evaluated using precision, recall, F1-score, and a confusion matrix.

A prediction workflow was also implemented. It loads the saved model and produces a risk-review prediction for a transaction without retraining the model.

Technical tests were added using pytest to check important parts of the data and preprocessing workflow. All five implemented tests passed successfully.

The Week 2 implementation provides a working baseline ML workflow from data validation through preprocessing, model training, evaluation, and inference. The model results are treated as a baseline for further improvement rather than as a final production solution.

The Week 2 work also highlighted areas that require further attention, including model performance, class imbalance, missing transaction fields, and continued testing before any production use.