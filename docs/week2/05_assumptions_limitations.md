# Week 2 Assumptions and Limitations

## Assumptions

The Week 2 implementation assumes that `Customer_ID` is the correct key for connecting customer and transaction records.

It is also assumed that the `Risk_Review_Flag` provided in the transaction dataset is the intended target for the initial classification task and that the existing `Yes` and `No` labels can be used for supervised learning.

The missing `Device_Type` and `Location` values are assumed to be missing data rather than indicators of a particular risk condition. They are therefore handled during preprocessing.

The initial model assumes that the available customer and transaction features contain enough information to provide a useful baseline for predicting risk review requirements.

## Limitations

The current Logistic Regression model is only a baseline and should not be treated as a production banking risk system. Its evaluation results show that there is room for improvement, particularly for the `Yes` class.

The model produced 65% recall and 28% precision for the `Yes` class. This means that some transactions requiring review were correctly identified, but the model also generated a relatively high number of false positives.

The available datasets are synthetic and limited to the information provided for this educational project. The results may therefore not represent performance on real banking data.

The current automated tests cover basic data and preprocessing behaviour but do not provide complete coverage of the prediction workflow.

The current implementation also does not include a deployed API, monitoring system, model version management process, or production data pipeline.

Further development would be required before the workflow could be considered suitable for a real-world banking environment.