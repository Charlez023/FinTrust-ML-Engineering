import pandas as pd


CUSTOMER_FILE = "data/raw/FinTrust_Customer_Data.csv"
TRANSACTION_FILE = "data/raw/FinTrust_Transaction_Data.csv"


def load_data():
    """Load the customer and transaction datasets."""
    customers = pd.read_csv(CUSTOMER_FILE)
    transactions = pd.read_csv(TRANSACTION_FILE)

    return customers, transactions


def validate_data(customers, transactions):
    """Run basic validation checks on both datasets."""
    results = {}

    results["Customer data is not empty"] = len(customers) > 0
    results["Transaction data is not empty"] = len(transactions) > 0

    results["No duplicate customers"] = customers.duplicated().sum() == 0
    results["No duplicate transactions"] = transactions.duplicated().sum() == 0

    results["Customer IDs are complete"] = (
        customers["Customer_ID"].isnull().sum() == 0
    )

    results["Transaction Customer IDs are complete"] = (
        transactions["Customer_ID"].isnull().sum() == 0
    )

    results["Risk Review Flag is complete"] = (
        transactions["Risk_Review_Flag"].isnull().sum() == 0
    )

    return results


if __name__ == "__main__":
    customers, transactions = load_data()
    results = validate_data(customers, transactions)

    print("FinTrust Data Validation Results")
    print("--------------------------------")

    for check, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {check}")