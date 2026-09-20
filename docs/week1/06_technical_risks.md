# FinTrust ML Engineering — Technical Risks

During the Week 1 review, I identified some risks that may affect the ML workflow.

## 1. Missing Data

The transaction dataset has 96 missing `Device_Type` values and 96 missing `Location` values. These will need to be handled before modelling.

## 2. Incorrect Data Types

`Monthly_Income` and `Transaction_DateTime` are currently stored as text. They may need to be converted before they are used for analysis or modelling.

## 3. Invalid Values

Unexpected numerical or categorical values could cause problems during preprocessing. Data validation will be needed to identify these issues.

## 4. Training and Inference Differences

Using different preprocessing steps during training and prediction could lead to incorrect results. The same preprocessing process should be used in both cases.

## 5. Model Input Mismatch

The model will require a specific set of features. Changes to these features could cause errors during prediction, so the feature set should be documented.

## 6. Dependencies and Reproducibility

Different Python or library versions could cause the project to behave differently. Dependencies should be documented and the project should be tracked with Git.

## 7. Model Loading

The future inference workflow will need to load the trained model and preprocessing components correctly. This should be tested before the model is used for prediction.

## 8. Integration

The ML component may need to connect with other parts of the FinTrust project. Testing the individual components and their connections will help identify integration problems.

## 9. Synthetic Data

The FinTrust data is synthetic and intended for educational use. Any future model results should therefore be interpreted within the limits of the project data.