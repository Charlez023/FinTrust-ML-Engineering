# Week 2 Testing

Automated technical tests were added using pytest to check important parts of the FinTrust ML workflow.

Five tests were implemented. The tests confirm that the customer and transaction datasets are not empty, that customer IDs are complete, that transaction customer IDs are complete, and that the preprocessing workflow produces the expected number of rows.

The tests were executed from the project root using pytest. All five tests passed successfully.

The test result was:

`5 passed in 4.61s`

The successful tests provide basic automated checks for data availability, required identifiers, and preprocessing output. They help detect simple problems before the workflow is used for further model development.

The current tests focus mainly on data and preprocessing behaviour. Additional tests can be added in later stages to cover model loading, prediction outputs, invalid inputs, and other inference behaviour.