import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая фильтрует список словарей по наличию в них строки поиска"""
    filter_data = []
    pattern = re.compile(search)
    for item in data:
        description = item.get("description", "")
        if re.search(pattern, description):
            filter_data.append(item)
    return filter_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая подсчитывает количество операций для заданной категории"""
    descriptions = [item.get("description") for item in data if "description" in item]
    count = Counter(descriptions)
    return {category: count[category] for category in categories}
