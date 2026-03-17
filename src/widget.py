from masks import get_mask_account, get_mask_card_number


def mask_account_card(arg: str) -> str:
    """Функция, которая обрабатывает информацию о картах и о счетах"""
    parts = arg.split()
    number = parts[-1]
    type_info = " ".join(parts[:-1])
    if "счет" in type_info.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{type_info} {masked_number}"


def get_date(date: str) -> str:
    """Функция, которая выводит дату в другом формате"""
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}.{month}.{year}"


card_number = str(input())
account_number = str(input())
date = str(input())

print(mask_account_card(card_number))
print(mask_account_card(account_number))
print(get_date(date))
