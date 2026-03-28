from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], key: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей, у которых ключ соответствует значению"""
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == key:
            new_list_dict.append(item)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, Any]], sort_list: bool = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует списки словарей по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x.get("date", ""), reverse=sort_list)
    return sorted_list


test = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

result = filter_by_state(test)

print(sort_by_date(result))
