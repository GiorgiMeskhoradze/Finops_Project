import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_db():
    with patch('app.routes.transactions.execute_query') as mock:
        yield mock

def test_health_check():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

def test_get_transactions_found(mock_db):
    mock_db.return_value = [(1, 1, 'deposit', 500.0)]
    res = client.get("/transactions/1")
    assert res.status_code == 200
    assert res.json()["account_id"] == 1

def test_get_transactions_not_found(mock_db):
    mock_db.return_value = []
    res = client.get("/transactions/99")
    assert res.status_code == 404

def test_deposit_success(mock_db):
    mock_db.return_value = []
    res = client.post("/transactions/deposit", json={"account_id": 1, "amount": 500.0})
    assert res.status_code == 200
    assert res.json()["message"] == "Deposit successful"

def test_deposit_invalid_amount(mock_db):
    res = client.post("/transactions/deposit", json={"account_id": 1, "amount": -100.0})
    assert res.status_code == 400

def test_withdraw_success(mock_db):
    mock_db.return_value = [(1000.0,)]
    res = client.post("/transactions/withdraw", json={"account_id": 1, "amount": 200.0})
    assert res.status_code == 200

def test_withdraw_insufficient_funds(mock_db):
    mock_db.return_value = [(100.0,)]
    res = client.post("/transactions/withdraw", json={"account_id": 1, "amount": 500.0})
    assert res.status_code == 400
    assert res.json()["detail"] == "Insufficient funds"

def test_transfer_success(mock_db):
    mock_db.return_value = [(1000.0,)]
    res = client.post("/transactions/transfer", json={
        "from_account_id": 1,
        "to_account_id": 2,
        "amount": 300.0
    })
    assert res.status_code == 200

def test_transfer_insufficient_funds(mock_db):
    mock_db.return_value = [(50.0,)]
    res = client.post("/transactions/transfer", json={
        "from_account_id": 1,
        "to_account_id": 2,
        "amount": 300.0
    })
    assert res.status_code == 400
    assert res.json()["detail"] == "Insufficient funds"