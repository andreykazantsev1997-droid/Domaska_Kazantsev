from unittest.mock import patch,MagicMock, mock_open
import os
import pytest
import pandas as pd
from src.formats import get_transactions_from_csv
from src.formats import get_transactions_from_excel

def test_get_transactions_from_csv_not_found():
    assert get_transactions_from_csv("non.csv") == []

@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data="id;amount\n1;100")
@patch("csv.DictReader")
def test_get_transactions_from_csv(mock_dict_reader, mock_file, mock_exists):
    mock_exists.return_value = True
    mock_dict_reader.return_value = [{"id": "1", "amount": "100"}]

    result = get_transactions_from_csv("fake_path.csv")

    assert result == [{"id": "1", "amount": "100"}]
    mock_file.assert_called_once_with("fake_path.csv", "r", encoding="utf-8")

@patch("os.path.exists")
@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel, mock_exists):
    mock_exists.return_value = True
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 789, "amount": 500}]
    mock_read_excel.return_value = mock_df
    result = get_transactions_from_excel("any_path.xlsx")
    assert result == [{"id": 789, "amount": 500}]
    mock_read_excel.assert_called_once_with("any_path.xlsx")

def test_get_transactions_from_excel_not_found():
    assert get_transactions_from_excel("missing.xlsx") == []