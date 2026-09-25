# Week 2 Data Findings

The Week 2 implementation started with a review of the customer and transaction datasets to confirm their structure and identify issues that could affect the ML workflow.

The customer dataset contains 1,500 records and 12 columns. It contains customer information such as age, gender, city, customer segment, account type, tenure, digital engagement, income band, preferred channel, and account status. The dataset had no missing values and no duplicate rows.

The transaction dataset contains 12,000 records and 11 columns. It includes transaction details such as transaction type, amount, channel, device type, location, international transaction status, transaction status, and the `Risk_Review_Flag` target.

The transaction dataset had no duplicate rows and the important `Customer_ID` and `Risk_Review_Flag` fields were complete. However, `Device_Type` and `Location` each contained 96 missing values. These missing values were handled during preprocessing rather than treated as validation failures.

The `Monthly_Income` field in the customer dataset is stored as text and represents income bands rather than exact numeric income values. This means it was treated as a categorical feature during preprocessing.

The `Transaction_DateTime` field required conversion to datetime format. Two additional features, transaction hour and transaction day, were created from this field to provide information that could be used by the model.

The target variable, `Risk_Review_Flag`, contains two classes. There were 9,648 transactions labelled `No` and 2,352 labelled `Yes`. This means that approximately 80.4% of transactions were labelled `No` and 19.6% were labelled `Yes`.

The target distribution is therefore imbalanced. Because of this, accuracy alone was not considered sufficient for evaluating the baseline model. Precision, recall, F1-score, and the confusion matrix were included in the evaluation.

These findings informed the preprocessing and model development decisions made during Week 2.