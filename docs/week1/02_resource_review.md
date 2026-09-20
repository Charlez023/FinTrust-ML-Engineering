# FinTrust ML Engineering — Resource Review

## 1. Purpose

I reviewed the available FinTrust resources to understand the project, the available data, and their relevance to the ML Engineering track.

## 2. Customer Dataset

`FinTrust_Customer_Data.csv` contains 1,500 customer records and 12 columns. It includes information such as customer ID, age, gender, customer segment, account type, tenure, income, preferred channel, and account status.

The dataset has no missing values or duplicate rows. `Customer_ID` will be used to connect customer records with transactions. `Customer_Name` is not needed as a model feature.

`Monthly_Income` is stored as text and may need to be converted if it is used for modelling.

## 3. Transaction Dataset

`FinTrust_Transaction_Data.csv` contains 12,000 transaction records and 11 columns. It includes transaction details such as amount, type, channel, device, location, status, and risk-review flag.

There are no duplicate rows. However, 96 records have missing `Device_Type` values and 96 have missing `Location` values.

`Transaction_DateTime` is stored as text and will need to be converted before time-based analysis or features can be created.

`Risk_Review_Flag` is a possible target for the future classification model.

## 4. Data Dictionary

`FinTrust_Data_Dictionary.xlsx` was reviewed to understand the meaning and expected values of the dataset fields. It will be useful when carrying out data validation, preprocessing, and feature selection.

## 5. Project Brief and Roadmap

The `FinTrust_Project_Brief.pdf` provides the main project context, while the `FinTrust_4_Week_Master_Roadmap_Readable.pdf` shows the planned progression of the project.

Week 1 focuses on understanding and planning, with later weeks covering analysis, development, integration, testing, and presentation.

## 6. Financial Knowledge Base

`Fintrust_Financial_Knowledge_Base.docx` contains financial information mainly related to the customer-support and Generative AI parts of the project. It is not a main source for the transaction prediction workflow but may be relevant when the different project components are connected.

## 7. Key Findings and Limitations

The main limitation is that the datasets and `Risk_Review_Flag` are synthetic and intended for educational use.

The main MLE dependencies identified are reliable customer and transaction data, clear field definitions, a suitable target, consistent preprocessing, a trained model, and proper testing.