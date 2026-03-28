def filter_by_skate(list_dict: list, key: str = "EXECUTED") -> list:
    """Функция, которая возвращает список словарей, у которых ключ соответствует значению"""
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == key:
            new_list_dict.append(item)
    return new_list_dict


def sort_by_date(list_dict: list, sort_list: bool = True) -> list:
    """Функция, которая сортирует списки словарей по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x.get("date", ""), reverse=sort_list)
    return sorted_list
