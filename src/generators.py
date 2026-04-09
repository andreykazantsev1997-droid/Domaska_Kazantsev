

def filter_by_currency(transactions: list[dict], currency_name: str ):
    """Функция, которая возвращает список транзакций, которые имеют заданное название валюты"""
    for transaction in transactions:
        currency = transaction.get('operationAmount',{}).get('currency',{}).get('name',{} == currency_name)
        if currency == currency_name:
            yield transaction

transactions = [{ "id": 939719570,"state": "EXECUTED","date": "2018-06-30T02:08:58.425572","operationAmount": {"amount": "9824.07","currency": {"name": "RUB","code": "RUB"}},
                  "description": "Перевод организации","from": "Счет 75106830613657916952","to": "Счет 11776614605963066702"},
                {"id": 142264268,"state": "EXECUTED","date": "2019-04-04T23:20:05.206878","operationAmount": {"amount": "79114.93","currency": {"name": "USD","code": "USD"}},
                 "description": "Перевод со счета на счет","from": "Счет 19708645243227258542","to": "Счет 75651667383060284188"},
                {"id": 141164268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "7114.93", "currency": {"name": "BYN", "code": "BYN"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708135243227258542",
                 "to": "Счет 756516655553060284188"},
                {"id": 141114268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "7114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708135243227258542",
                 "to": "Счет 756516655553060284188"},
                {"id": 111264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
                 "operationAmount": {"amount": "71114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708115243227258542",
                 "to": "Счет 756516655511160284188"},
                ]

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]):
    """Функция-генератор, которая принимает список словарей и возвращает описание операций"""
    for transaction in transactions:
        yield transaction.get("description", "Данные отсутствуют")

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

def card_number_generator(start: int, end: int) -> str:
    """Функция-генератор, которая выдает номера карт в заданном диапазоне"""
    for number in range(start, end + 1):
        card_str = f"{number:016}"
        formatted_card = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted_card

for card_number in card_number_generator(1, 5):
    print(card_number)

