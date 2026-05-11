import json
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def financial_transactions(json_file):
    """Функция, которая принимает json-файл с финансовыми транзакциями в словарь"""
    logger.debug("Проверка файла")
    if not os.path.exists(json_file):
        logger.debug("Файл не найден")
        return []
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            transaction = json.load(file)
            if isinstance(transaction, list):
                logger.info("Данные успешно прочитаны, формат - список")
                return transaction
            else:
                logger.error("Ошибка: JSON содержит не список")
                return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []


transactions = financial_transactions("../data/operations.json")
