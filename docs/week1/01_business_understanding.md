# FinTrust ML Engineering — Business Understanding

## 1. Business Problem

FinTrust has customer and transaction data that can be used to support banking and risk-related activities. My focus in the ML Engineering track is to understand how this data can be prepared and used in a reliable ML workflow.

The project is educational and uses synthetic data.

## 2. ML Use Case

One possible use case is predicting whether a transaction should be flagged for risk review.

The ML Engineering work will focus on the workflow around this use case, including data preparation, feature preparation, testing, model integration, and inference. Model development will be handled later.

## 3. Expected Inputs

The workflow will use customer and transaction data. The two datasets can be connected using `Customer_ID`.

The data includes information such as customer segment, account type, customer tenure, transaction type, transaction amount, transaction channel, and transaction status.

## 4. Expected Output

The main output will be a prediction showing whether a transaction should be flagged for risk review. The final output format will be decided during implementation.

## 5. Scope Limitation

The `Risk_Review_Flag` is a synthetic label created for this educational project. It should not be treated as a real fraud decision or used for actual financial decisions.