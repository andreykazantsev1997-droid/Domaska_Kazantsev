from unittest import expectedFailure
import pytest

from src.widget import mask_account_card

def test_mask_account_card_card():
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