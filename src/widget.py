from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая обрабатывает информацию о картах и о счетах"""
    if not isinstance(account_card, str):
        raise TypeError("Входные данные должны быть строкой")
    if account_card == "":
        raise ValueError("Данные не введены")
    parts = account_card.split()
    if len(parts) < 2:
        raise ValueError("Номер не найден")
    number = parts[-1]
    if not number.isdigit():
        raise ValueError("Номер не найден")
    type_info = " ".join(parts[:-1])
    if len(number) < 16:
        raise ValueError("Номер не найден")
    if "счет" in type_info.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{type_info} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция, которая выводит дату в другом формате"""
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]
    return f"{day}.{month}.{year}"


# card_number = str(input())
# account_number = str(input())
# date = str(input())
#
# print(mask_account_card(card_number))
# print(mask_account_card(account_number))
# print(get_date(date))
