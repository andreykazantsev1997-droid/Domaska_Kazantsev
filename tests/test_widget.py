from unittest import expectedFailure
import pytest

from src.widget import mask_account_card, get_date

def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_account():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

@pytest.mark.parametrize("account_card, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                         ("Счет 64686473678894779589", "Счет **9589"),
                         ("  Visa Classic  6839392329123573  ", "Visa Classic 6839 39** **** 3573")])
def test_get_mask_card_number_varied(account_card, expected):
    assert mask_account_card(account_card) == expected

def test_mask_account_card_invalid():
    with pytest.raises(ValueError, match="Данные не введены"):
        mask_account_card("")
    with pytest.raises(ValueError, match="Номер не найден"):
        mask_account_card("Просто какой-то текст")

@pytest.mark.parametrize("invalid_input", [(""),("1234567890"),("Visa 123"),(None),(12345),])

def test_mask_account_card_invalid_data(invalid_input):
    with pytest.raises((ValueError, TypeError, IndexError)):
         mask_account_card(invalid_input)

@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ("2024-01-01T00:00:00.000000", "01.01.2024"),
    ("2024-02-29T10:00:00.000000", "29.02.2024"),])
def test_get_date_valid(date_string, expected):
    assert get_date(date_string) == expected

def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("11-03-2024")