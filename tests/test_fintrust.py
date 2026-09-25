import pandas as pd

from src.preprocessing.preprocess import prepare_data


CUSTOMER_FILE = "data/raw/FinTrust_Customer_Data.csv"
TRANSACTION_FILE = "data/raw/FinTrust_Transaction_Data.csv"


def load_test_data():
    customers = pd.read_csv(CUSTOMER_FILE)
    transactions = pd.read_csv(TRANSACTION_FILE)

    return customers, transactions


def test_customer_data_is_not_empty():
    customers, _ = load_test_data()

    assert len(customers) > 0


def test_transaction_data_is_not_empty():
    _, transactions = load_test_data()

    assert len(transactions) > 0


def test_customer_ids_are_complete():
    customers, _ = load_test_data()

    assert customers["Customer_ID"].isnull().sum() == 0


def test_transaction_customer_ids_are_complete():
    _, transactions = load_test_data()

    assert transactions["Customer_ID"].isnull().sum() == 0


def test_preprocessing_produces_expected_rows():
    customers, transactions = load_test_data()

    X_processed, y, preprocessor = prepare_data(
        customers,
        transactions
    )

    assert X_processed.shape[0] == len(transactions)
    assert len(y) == len(transactions)