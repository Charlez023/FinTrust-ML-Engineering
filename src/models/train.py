import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


CUSTOMER_FILE = "data/raw/FinTrust_Customer_Data.csv"
TRANSACTION_FILE = "data/raw/FinTrust_Transaction_Data.csv"
MODEL_FILE = "models/fintrust_risk_model.joblib"


def load_data():
    """Load customer and transaction datasets."""
    customers = pd.read_csv(CUSTOMER_FILE)
    transactions = pd.read_csv(TRANSACTION_FILE)

    return customers, transactions


def prepare_data(customers, transactions):
    """Join datasets and prepare features and target."""

    transactions["Transaction_DateTime"] = pd.to_datetime(
        transactions["Transaction_DateTime"]
    )

    transactions["Transaction_Hour"] = (
        transactions["Transaction_DateTime"].dt.hour
    )

    transactions["Transaction_Day"] = (
        transactions["Transaction_DateTime"].dt.dayofweek
    )

    data = transactions.merge(
        customers,
        on="Customer_ID",
        how="left"
    )

    y = data["Risk_Review_Flag"].map({
        "No": 0,
        "Yes": 1
    })

    X = data.drop(
        columns=[
            "Risk_Review_Flag",
            "Transaction_ID",
            "Customer_ID",
            "Customer_Name",
            "Transaction_DateTime",
        ]
    )

    return X, y


def build_pipeline(X):
    """Build the preprocessing and model pipeline."""

    categorical_columns = X.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()

    numerical_columns = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ]
    )

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

    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced",
                    random_state=42
                )
            ),
        ]
    )

    return model_pipeline


if __name__ == "__main__":
    customers, transactions = load_data()

    X, y = prepare_data(
        customers,
        transactions
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model_pipeline = build_pipeline(X_train)

    model_pipeline.fit(
        X_train,
        y_train
    )

    joblib.dump(
        model_pipeline,
        MODEL_FILE
    )

    print("Model saved successfully.")

    predictions = model_pipeline.predict(X_test)

    print("Model training completed successfully.")
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))