import joblib
import pandas as pd


MODEL_FILE = "models/fintrust_risk_model.joblib"


def load_model():
    """Load the trained FinTrust risk prediction model."""
    return joblib.load(MODEL_FILE)


def prepare_transaction(transaction):
    """Prepare a transaction for prediction."""

    transaction = transaction.copy()

    transaction["Transaction_DateTime"] = pd.to_datetime(
        transaction["Transaction_DateTime"]
    )

    transaction["Transaction_Hour"] = (
        transaction["Transaction_DateTime"].dt.hour
    )

    transaction["Transaction_Day"] = (
        transaction["Transaction_DateTime"].dt.dayofweek
    )

    transaction = transaction.drop(
        columns=[
            "Transaction_ID",
            "Customer_ID",
            "Customer_Name",
            "Transaction_DateTime",
        ]
    )

    return transaction


def predict_risk(transaction):
    """Predict whether a transaction requires risk review."""

    model = load_model()
    prepared_transaction = prepare_transaction(transaction)

    prediction = model.predict(prepared_transaction)[0]

    if prediction == 1:
        return "Yes"

    return "No"


if __name__ == "__main__":
    transaction = pd.DataFrame([{
        "Transaction_ID": "TEST001",
        "Customer_ID": "CUST0001",
        "Transaction_DateTime": "2026-09-25 14:30:00",
        "Transaction_Type": "Transfer",
        "Amount_NGN": 150000.0,
        "Channel": "Mobile App",
        "Device_Type": "Android",
        "Location": "Lagos",
        "International_Tra": "No",
        "Transaction_Stat": "Successful",
        "Customer_Name": "Test Customer",
        "Age": 30,
        "Gender": "Male",
        "City": "Lagos",
        "Customer_Segm": "Everyday",
        "Account_Type": "Savings",
        "Tenure_Months": 24,
        "Digital_Engagem": 75.0,
        "Monthly_Income": "100k-249k",
        "Preferred_Chann": "Mobile App",
        "Account_Status": "Active",
    }])

    prediction = predict_risk(transaction)

    print("FinTrust Risk Prediction")
    print("------------------------")
    print("Risk Review:", prediction)