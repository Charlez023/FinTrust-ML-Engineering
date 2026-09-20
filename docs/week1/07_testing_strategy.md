# FinTrust ML Engineering — Initial Testing Strategy

Testing will be used throughout the ML workflow to find problems early and make sure the different parts work correctly.

## 1. Data Validation

I will test that the required columns are present, the data types are suitable, and customer and transaction records can be connected using `Customer_ID`.

## 2. Preprocessing

I will test that missing values, data types, categorical values, and numerical features are handled correctly.

## 3. Feature Preparation

I will check that the expected features are created correctly and that the target variable is not accidentally included as a feature.

## 4. Model

Once a model is developed, I will test that it can be trained, saved, loaded, and used with the expected features.

## 5. Inference

I will test that valid input produces the expected prediction and that invalid or incomplete input is handled properly.

## 6. Integration

After testing the individual parts, I will test the complete workflow to make sure the stages work together:

```text
Data
  ↓
Validation
  ↓
Preprocessing
  ↓
Features
  ↓
Model
  ↓
Prediction
```

Future API or service testing will be added if that part of the project is implemented.