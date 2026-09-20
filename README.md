# FinTrust Financial Intelligence & Digital Banking Support Solution

## Machine Learning Engineering Track

This repository contains my Week 1 work for the AnalystLab Africa FinTrust project.

The project focuses on understanding how Machine Learning Engineering can support a digital banking solution using customer and transaction data.

## Week 1 Focus

The focus for Week 1 was **Understand → Explore → Define → Plan**.

I started by understanding the project requirements and the role of the Machine Learning Engineering track. I reviewed the available project resources and explored the customer and transaction datasets to understand their structure, contents, and potential issues.

I then defined the proposed ML workflow, repository structure, technical requirements, testing approach, risks, dependencies, and implementation plan for the coming weeks.

## Data Exploration

The customer dataset contains 1,500 records and 12 columns, while the transaction dataset contains 12,000 records and 11 columns.

The initial exploration showed that the customer dataset had no missing or duplicate rows. The transaction dataset also had no duplicate rows, but `Device_Type` and `Location` each contained 96 missing values.

I also found that some fields will require preparation before they can be used in an ML workflow. For example, `Monthly_Income` is stored as text in the customer data, while `Transaction_DateTime` is also stored as text in the transaction data.

These findings helped me identify data validation and preprocessing as important parts of the implementation rather than treating the datasets as immediately ready for modelling.

## Proposed ML Workflow

The planned workflow for the project is:

**Data → Validation → Preprocessing → Feature Preparation → ML Model → Inference → Prediction Output → Testing**

The exact model and final features will be determined during the modelling stage after the data has been properly prepared and the Data Science work is available for integration.

## Repository

The repository is structured to separate the project data, Week 1 documentation, future notebooks, source code, and tests.

The `data` directory contains the provided project resources, `docs/week1` contains the Week 1 documentation, `src` is reserved for the ML engineering components that will be implemented in later weeks, and `tests` is reserved for automated testing.

## Week 1 Outcome

The main outcome of Week 1 was developing a clearer understanding of the project, the available data, the technical challenges that may arise, and how the ML Engineering workflow will be implemented in the following weeks.

One important lesson from the initial exploration was that building an ML solution is not only about training a model. Data quality, validation, preprocessing, testing, reproducibility, and the way different components connect are also important parts of the process.

The data provided for this project is synthetic and is being used for educational purposes.

## Next Steps

In Week 2, I plan to begin implementing the workflow by working on data loading, validation, preprocessing, feature preparation, and initial automated tests.