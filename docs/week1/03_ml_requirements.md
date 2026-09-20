# FinTrust ML Engineering — Technical Requirements

## 1. Input Requirements

The ML workflow will use customer and transaction data that has been checked and prepared. The required fields should be available, have suitable data types, and contain reasonable values.

Customer and transaction records should be connectable using `Customer_ID`.

## 2. Output Requirements

The main output will be a risk-review prediction for a transaction. The output should identify the transaction and show the model's prediction. A probability may also be included if available.

## 3. Preprocessing Requirements

The data will need to be prepared before modelling. This may include handling missing values, converting data types, encoding categorical values, and creating features.

The preprocessing steps should be reusable so the same process can be used during training and prediction.

## 4. Python Dependencies

Python will be used for the ML work. The main libraries planned are Pandas, NumPy, Scikit-learn, Joblib, and Pytest.

The project dependencies should be recorded in `requirements.txt`.

## 5. Testing Requirements

Testing should cover data validation, preprocessing, features, model inputs, predictions, and the overall workflow.

## 6. Version Control Requirements

Git and GitHub will be used to track project changes. The repository should contain the relevant documentation, source code, tests, and dependency information.

The `.gitignore` file will be used to prevent unnecessary or sensitive files from being committed.

## 7. Future API Requirements

The model may later be connected to an API or another service. This is a future requirement and is not part of the Week 1 implementation.