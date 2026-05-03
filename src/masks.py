import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая маскирует цифры, кроме первых 6 цифр и последние 4 цифры банковской карты"""
    card = number_card.replace(" ", "")
    if number_card == "":
        logger.error("Ошибка: передан пустой номер карты")
        raise ValueError("Номер карты не введен")
    unmasked_numbers = card[:6]
    unmasked_numbers_2 = card[-4:]
    masked_numbers = f"{unmasked_numbers}******{unmasked_numbers_2}"
    logger.info("Маскировка номера карты выполнена успешно")
    return f"{masked_numbers[:4]} {masked_numbers[4:6]}** **** {masked_numbers[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция, которая показывает последние 6 цифр номера счета, где видны только последние 4 цифры,
    а перед ними две звездочки"""
    logger.debug(f"Начало маскировки счета: {number_account}")
    save_numbers = number_account[-4:]
    masked_numbers = f"**{save_numbers[-4:]}"
    logger.info("Маскировка номера счета выполнена успешно")
    return masked_numbers


# card_number = str(input())
# account_number = str(input())
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))

if __name__ == "__main__":
    get_mask_card_number("1234567812345678")
    get_mask_account("73654108430135874305")
