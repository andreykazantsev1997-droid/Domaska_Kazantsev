from unittest.mock import patch

import pytest

from main import main


@pytest.fixture
def mock_transactions():
    """Тестовый набор данных, содержащий форматы JSON и CSV/Excel."""
    return [
        {
            "date": "2024-01-01T12:00:00",
            "description": "Перевод организации",
            "from": "Visa Classic 1234567812345678",
            "to": "Счет 98765432109876543210",
            "amount": "1000",
            "currency_code": "RUB",
        },
        {
            "date": "2024-01-02T15:00:00",
            "description": "Покупка в магазине",
            "to": "Счет 11112222333344445555",
            "operationAmount": {"amount": "50", "currency": {"name": "USD", "code": "USD"}},
        },
    ]


@patch("main.print")
@patch("main.input")
@patch("main.financial_transactions")
def test_main_json_flow(mock_financial, mock_input, mock_print, mock_transactions):
    mock_financial.return_value = mock_transactions
    mock_input.side_effect = ["1", "EXECUTED", "нет", "да", "нет"]
    main()
    mock_financial.assert_called_once_with("data/operations.json")
    mock_print.assert_any_call("Всего банковских операций в выборке: 1\n")


@patch("main.print")
@patch("main.input")
def test_main_invalid_file_choice(mock_input, mock_print):
    mock_input.side_effect = ["9"]
    main()
    mock_print.assert_any_call("Некорректный выбор")
