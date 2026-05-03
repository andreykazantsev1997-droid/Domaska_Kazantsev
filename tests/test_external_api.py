import unittest
from unittest.mock import patch
from src.external_api import get_amount_in_rub

@patch('requests.get')
def test_get_amount_in_rub_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }
    assert get_amount_in_rub(transaction) == 7500.0

def test_get_amount_in_rub_local():
    transaction = {
        "operationAmount": {
            "amount": "500.00",
            "currency": {"code": "RUB"}
        }
    }
    assert get_amount_in_rub(transaction) == 500.0


@patch('requests.get')
def test_get_amount_in_rub_error(mock_get):
    mock_get.side_effect = Exception("Ошибка сети")
    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "EUR"}
        }
    }
    assert get_amount_in_rub(transaction) == 0.0
