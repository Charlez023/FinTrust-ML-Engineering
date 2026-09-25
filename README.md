# FinTrust Financial Intelligence & Digital Banking Support Solution

## Machine Learning Engineering Track

This repository contains my work for the AnalystLab Africa FinTrust project. The project focuses on how Machine Learning Engineering can support a digital banking solution using customer and transaction data.

The Week 1 work focused on understanding the project, exploring the available resources and datasets, defining the technical requirements, and planning the ML workflow. Week 2 moved from planning into practical implementation.

## Week 1 Focus

The focus for Week 1 was **Understand → Explore → Define → Plan**.

I reviewed the project requirements and available resources and explored the customer and transaction datasets to understand their structure, contents, and potential issues.

The Week 1 documentation covered the proposed ML workflow, repository structure, technical requirements, testing strategy, technical risks, dependencies, success criteria, and implementation plan.

## Data

The customer dataset contains 1,500 records and 12 columns, while the transaction dataset contains 12,000 records and 11 columns.

The customer dataset had no missing or duplicate rows. The transaction dataset had no duplicate rows, but `Device_Type` and `Location` each contained 96 missing values.

Some fields also required preparation before being used in the ML workflow. For example, `Monthly_Income` is stored as text, while `Transaction_DateTime` requires conversion to a datetime format.

The target variable for the initial model is `Risk_Review_Flag`, which contains `Yes` and `No` values.

## Week 2 Implementation

Week 2 focused on **Analyze → Prepare → Develop → Test/Evaluate → Document**.

A data validation component was implemented in `src/data/validate.py`. It checks that the datasets are not empty, that there are no duplicate records, and that important identifiers and the target field are complete.

A preprocessing workflow was implemented in `src/preprocessing/preprocess.py`. It joins customer and transaction data using `Customer_ID`, creates transaction hour and day features, separates the target from the input features, handles missing values, and converts categorical variables into numerical features using one-hot encoding.

A baseline Logistic Regression model was implemented in `src/models/train.py`. The model uses a preprocessing pipeline with numerical imputation and scaling, categorical imputation and encoding, and balanced class weights.

The transaction target is imbalanced, with 80.4% of transactions labelled `No` and 19.6% labelled `Yes`. Because of this imbalance, evaluation includes precision, recall, F1-score, and a confusion matrix rather than relying only on accuracy.

The model was trained using 9,600 transactions and evaluated on 2,400 transactions. The evaluation produced 65% recall and an F1-score of 0.40 for the `Yes` class. The results provide a baseline for further model development and evaluation.

The trained model pipeline is saved as:

`models/fintrust_risk_model.joblib`

A prediction workflow was also implemented in `src/inference/predict.py`. It loads the saved model and produces a risk-review prediction without retraining the model.

## Testing

Five automated technical tests were implemented using pytest. The tests cover dataset availability, customer ID completeness, transaction customer ID completeness, and preprocessing output size.

All five tests passed successfully:

`5 passed in 4.61s`

## Repository Structure

The repository separates project data, documentation, source code, model artifacts, and tests.

```text
FinTrust ML Engineering/
├── data/
│   ├── processed/
│   └── raw/
├── docs/
│   └── week1/
├── models/
│   └── fintrust_risk_model.joblib
├── notebooks/
├── src/
│   ├── data/
│   │   └── validate.py
│   ├── features/
│   ├── inference/
│   │   └── predict.py
│   ├── models/
│   │   └── train.py
│   └── preprocessing/
│       └── preprocess.py
└── tests/
    └── test_fintrust.py
```

## Dependencies

The main Python dependencies are listed in `requirements.txt` and include pandas, scikit-learn, joblib, pytest, and openpyxl.

## Current Workflow

The implemented workflow is:

**Data → Validation → Preprocessing → Feature Preparation → Model Training → Model Evaluation → Saved Model → Inference → Prediction → Testing**

The current model is a baseline implementation. Its evaluation results will be used to guide further development rather than treating the current model as a final production solution.

The data provided for this project is synthetic and is being used for educational purposes.