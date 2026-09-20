# FinTrust ML Engineering — ML Workflow

## Workflow

Customer Data + Transaction Data

↓

Data Validation

↓

Preprocessing

↓

Feature Preparation

↓

ML Model

↓

Prediction

↓

Output

↓

Testing

## 1. Data

The workflow starts with the FinTrust customer and transaction datasets. The two datasets can be connected using `Customer_ID`.

The customer dataset contains 1,500 records, while the transaction dataset contains 12,000 records.

## 2. Data Validation

The data will be checked to make sure the required columns, data types, and values are correct.

The relationship between customers and transactions will also be checked using `Customer_ID`.

## 3. Preprocessing

The data will be prepared for the model by handling missing values, converting data types, and encoding categorical values where necessary.

The same preprocessing process should be used during training and prediction.

## 4. Feature Preparation

Relevant customer and transaction information will be prepared as features for the model.

Possible features include transaction amount, type, channel, international status, customer segment, and other useful information identified during analysis.

## 5. Model

The prepared features will be given to a classification model. The specific model will be selected during the modelling stage.

## 6. Prediction

The trained model will generate a prediction indicating whether a transaction should be flagged for risk review.

## 7. Output

The output should contain the transaction ID and the prediction. Other information such as a probability or prediction time may also be included.

## 8. Testing

Each stage of the workflow will be tested to identify errors and make sure the complete workflow works correctly.