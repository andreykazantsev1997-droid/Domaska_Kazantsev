import json
import os


def financial_transactions(json_file):
    """Функция, которая принимает json-файл с финансовыми транзакциями в словарь"""
    if not os.path.exists(json_file):
        return []
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            transaction = json.load(file)
            if isinstance(transaction, list):
                return transaction
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


transactions = financial_transactions("../data/operations.json")
