# FinTrust ML Engineering — ML Architecture

## High-Level Architecture

The planned ML workflow for FinTrust will follow a simple flow from raw data to prediction.

```text
Customer & Transaction Data
            ↓
      Data Validation
            ↓
       Preprocessing
            ↓
    Feature Preparation
            ↓
          ML Model
            ↓
        Inference
            ↓
    Prediction Output
            ↓
         Testing
```

The customer and transaction data will first be checked to make sure the required fields, data types, and data quality are acceptable.

The data will then go through preprocessing and feature preparation before being passed to the classification model. The inference component will use the trained model to generate a prediction.

The prediction output may contain the transaction ID, risk-review prediction, and probability where appropriate.

Testing will be carried out across the different components and on the complete workflow.

This is the planned architecture for Week 1. The exact model, final features, and deployment approach will be determined during the later stages of the project.