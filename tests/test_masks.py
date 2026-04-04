import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("1234567892123", "1234 56** **** 2123"),
    ],
)
def test_get_mask_card_number_varied(number_card: str, expected: str) -> None:
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
        assert str(exc_info.value) == "Номер карты не введен"


@pytest.mark.parametrize(
    "number_account, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("7365410843013587", "**3587"),
        ("3587", "**3587"),
    ],
)
def test_get_mask_account_varied(number_account: str, expected: str) -> None:
    assert get_mask_account(number_account) == expected
