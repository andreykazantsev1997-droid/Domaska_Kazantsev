from typing import Any, Union


def filter_by_state(list_dict: list[dict[str, Any]], key: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей, у которых ключ соответствует значению"""
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == key:
            new_list_dict.append(item)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует списки словарей по дате"""
    sorted_by_data = sorted(list_dict, key=lambda x: x.get("date", ""), reverse=reverse)
    return sorted_by_data



# ]
#
# result = filter_by_state(test)
#
# print(sort_by_date(result))
