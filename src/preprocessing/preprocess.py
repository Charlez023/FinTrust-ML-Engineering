import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


CUSTOMER_FILE = "data/raw/FinTrust_Customer_Data.csv"
TRANSACTION_FILE = "data/raw/FinTrust_Transaction_Data.csv"


def load_data():
    """Load customer and transaction datasets."""
    customers = pd.read_csv(CUSTOMER_FILE)
    transactions = pd.read_csv(TRANSACTION_FILE)

    return customers, transactions


def prepare_data(customers, transactions):
    """Join datasets and prepare features and target."""

    # Convert transaction date/time
    transactions["Transaction_DateTime"] = pd.to_datetime(
        transactions["Transaction_DateTime"]
    )

    transactions["Transaction_Hour"] = (
        transactions["Transaction_DateTime"].dt.hour
    )

    transactions["Transaction_Day"] = (
        transactions["Transaction_DateTime"].dt.dayofweek
    )

    # Join customer information to transactions
    data = transactions.merge(
        customers,
        on="Customer_ID",
        how="left"
    )

    # Separate target
    y = data["Risk_Review_Flag"].map({"No": 0, "Yes": 1})

    # Remove fields that should not be model features
    X = data.drop(
        columns=[
            "Risk_Review_Flag",
            "Transaction_ID",
            "Customer_ID",
            "Customer_Name",
            "Transaction_DateTime",
        ]
    )

    # Identify categorical and numerical columns
    categorical_columns = X.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()

    numerical_columns = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    # Numerical preprocessing
    numerical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median"))
        ]
    )

    # Categorical preprocessing
    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                )
            ),
        ]
    )

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            ),
        ]
    )

    X_processed = preprocessor.fit_transform(X)

    return X_processed, y, preprocessor


if __name__ == "__main__":
    customers, transactions = load_data()

    X_processed, y, preprocessor = prepare_data(
        customers,
        transactions
    )

    print("Preprocessing completed successfully.")
    print("Processed feature shape:", X_processed.shape)
    print("Target shape:", y.shape)
    print("Missing target values:", y.isnull().sum())