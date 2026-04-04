from typing import Union

def get_mask_card_number(number_card: str) -> str:
    """Функция, которая маскирует цифры, кроме первых 6 цифр и последние 4 цифры банковской карты"""
    card = number_card.replace(" ","")
    if number_card == "":
        raise ValueError("Номер карты не введен")
    unmasked_numbers = card[:6]
    unmasked_numbers_2 = card[-4:]
    masked_numbers = f"{unmasked_numbers}******{unmasked_numbers_2}"
    return f"{masked_numbers[:4]} {masked_numbers[4:6]}** **** {masked_numbers[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция, которая показывает последние 6 цифр номера счета, где видны только последние 4 цифры,
    а перед ними две звездочки"""
    save_numbers = number_account[-4:]
    masked_numbers = f"**{save_numbers[-4:]}"
    return masked_numbers


# card_number = str(input())
# account_number = str(input())
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))