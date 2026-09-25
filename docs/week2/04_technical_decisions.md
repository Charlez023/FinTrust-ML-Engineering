# Week 2 Technical Decisions

Several technical decisions were made during the Week 2 implementation based on the structure of the available data and the requirements of the ML workflow.

The customer and transaction datasets were joined using `Customer_ID`. This allows transaction records to use relevant customer information as model features while keeping the transaction as the main unit of prediction.

`Risk_Review_Flag` was selected as the target variable because it directly represents whether a transaction requires risk review. The values `No` and `Yes` were converted to `0` and `1` for model training.

Fields such as `Transaction_ID`, `Customer_ID`, and `Customer_Name` were excluded from the model features. These fields are identifiers or personal information and are not required for the prediction itself. `Transaction_DateTime` was also excluded after useful time-based features were created from it.

Missing numerical values were handled using median imputation, while missing categorical values were handled using the most frequent value. Categorical features were converted using one-hot encoding with unknown categories ignored so that new categories do not cause the preprocessing workflow to fail.

Numerical features were scaled using `StandardScaler` before Logistic Regression. A scikit-learn pipeline was used to keep preprocessing and model training together and to ensure that the same transformations are applied during prediction.

The model used balanced class weights because the target variable is imbalanced. This was chosen to give greater consideration to the less frequent `Yes` class during training.

The model was saved as a complete pipeline using `joblib`. This allows the preprocessing steps and trained model to be loaded together during inference rather than rebuilding the preprocessing process separately.

These decisions were made to create a simple and consistent baseline workflow that can be tested and improved in later stages.
