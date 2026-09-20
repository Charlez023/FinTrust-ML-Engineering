# FinTrust ML Engineering — MLE Objectives

## 1. Primary Objective

The main objective is to plan a reliable ML workflow that can use validated FinTrust customer and transaction data to produce risk-review predictions.

At this stage, the focus is on understanding how the different ML components will work together and how they can be developed and tested later.

## 2. Data Objective

The data should be checked before it is used in the ML workflow. This includes checking the required columns, data types, missing values, duplicates, and whether the values are reasonable.

The relationship between customer and transaction records should also be checked. `Customer_ID` will be important because it connects the customer data with the transaction data.

## 3. Preprocessing Objective

The project should have clear and reusable steps for preparing the data before modelling.

The same preprocessing process should be used during training and prediction so that the model receives data in the expected format.

## 4. Feature Objective

Customer and transaction information will be used to create features for the ML model.

Possible features include transaction amount, transaction type, transaction channel, device type, location, transaction status, customer segment, account type, customer tenure, and time-related information.

The final features will be decided after further data analysis and modelling work.

## 5. Model Integration Objective

The workflow should provide a clear way for prepared features to be passed to a trained classification model.

The preprocessing and model components should work together so that preprocessing does not have to be repeated manually whenever a prediction is made.

## 6. Inference Objective

The inference process should be able to receive valid input data, apply the required preprocessing, load the trained model, and return a structured prediction.

The output may include the transaction ID, the risk-review prediction, and a probability if the model provides one.

## 7. Testing Objective

The main parts of the ML workflow should be tested to make sure they work correctly.

Testing will cover data validation, preprocessing, feature preparation, model loading, predictions, output structure, and the complete workflow.

## 8. Reproducibility Objective

The project should be organised so that another developer can understand and reproduce the ML workflow using the repository, source code, dependencies, and documentation.

Git and documented dependencies will help keep track of changes and make the project easier to reproduce.

## 9. Maintainability Objective

The ML workflow should be divided into separate components rather than putting everything into one script.

Data processing, feature preparation, modelling, and inference should be kept separate so they can be developed and tested more easily.

## 10. Integration Objective

The ML component should be designed so it can connect with the other parts of the FinTrust project as development continues.

## 11. Week 1 Boundary

Week 1 focuses on understanding the project, defining requirements, planning the ML workflow, setting up the repository, identifying technical risks, and planning the testing process.

Model training, production deployment, and a complete API implementation will be handled in later stages of the project.