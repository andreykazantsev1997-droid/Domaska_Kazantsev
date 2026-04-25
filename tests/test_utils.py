import json
from unittest.mock import patch, mock_open
from src.utils import financial_transactions

@patch("os.path.exists")  # Добавляем этот патч
def test_financial_transactions_success(mock_exists):
    mock_exists.return_value = True
    test_data = [{"id": 1, "state": "EXECUTED"}]
    json_data = json.dumps(test_data)
    with patch("builtins.open", mock_open(read_data=json_data)):
        result = financial_transactions("fake_path.json")
        assert result == test_data


def test_financial_transactions_not_list():
    json_data = json.dumps({"key": "value"})
    with patch("builtins.open", mock_open(read_data=json_data)):
        result = financial_transactions("fake_path.json")
        assert result == []


def test_financial_transactions_file_not_found():
    with patch("os.path.exists") as mock_exists:
        mock_exists.return_value = False
        result = financial_transactions("non_existent.json")
        assert result == []


def test_financial_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data="not a json")):
        result = financial_transactions("bad.json")
        assert result == []