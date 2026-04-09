import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture()
def filter_by_currency_info():
    return ([{"id": 939719570,"state": "EXECUTED","date": "2018-06-30T02:08:58.425572","operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"},
            {"id": 142264268,"state": "EXECUTED","date": "2019-04-04T23:20:05.206878","operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"},
             {"id": 873106923,"state": "EXECUTED", "date": "2019-03-23T01:09:46.296404","operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"},
            {"id": 895315941,"state": "EXECUTED","date": "2018-08-19T04:27:37.904916","operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"},
            {"id": 594226727,"state": "CANCELED","date": "2018-09-12T21:27:25.241689","operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"}])

def test_filter_by_currency_standart(filter_by_currency_info):
    result = list(filter_by_currency(filter_by_currency_info, "USD"))
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941
    for currency in result:
        assert currency["operationAmount"]["currency"]["name"] == "USD"


def test_filter_by_currency_no_results(filter_by_currency_info):
    # Ищем валюту, которой точно нет в списке
    result = list(filter_by_currency(filter_by_currency_info, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions_standard(filter_by_currency_info):
    result = list(transaction_descriptions(filter_by_currency_info))

    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Перевод со счета на счет"
    assert result[3] == "Перевод с карты на карту"
    assert result[4] == "Перевод организации"


def test_transaction_descriptions_full_list(filter_by_currency_info):
    result = list(transaction_descriptions(filter_by_currency_info))

    assert len(result) == 5
    assert all(isinstance(desc, str) for desc in result)


def test_transaction_descriptions_missing_data():
    bad_data = [{"id": 123}]
    gen = transaction_descriptions(bad_data)

    assert next(gen) == "Данные отсутствуют"

def test_card_number_generator_format():
    gen = card_number_generator(1, 1)
    result = next(gen)
    assert len(result) == 19
    assert result == "0000 0000 0000 0001"


def test_card_number_generator_range():
    result = list(card_number_generator(1, 3))

    assert len(result) == 3
    assert result[0] == "0000 0000 0000 0001"
    assert result[1] == "0000 0000 0000 0002"
    assert result[2] == "0000 0000 0000 0003"

def test_card_number_generator_empty_range():
    result = list(card_number_generator(10, 5))
    assert result == []