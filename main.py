from src.formats import get_transactions_from_csv, get_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import financial_transactions
from src.widget import get_date, mask_account_card


def main():
    """Основная функция, отвечающая за логику проекта"""
    data = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла\n")
    user_input = input("Пользователь: ").strip()
    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        data = financial_transactions("data/operations.json")
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        data = get_transactions_from_csv("data/transactions.csv")
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл.")
        data = get_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Некорректный выбор")
        return

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию")
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n")
        status_inport = input("Пользователь: ").strip()
        status_upper = status_inport.upper()
        if status_upper in valid_statuses:
            print(f"Операции отфильтрованы по статусу {status_upper}")
            data = filter_by_state(data, state=status_upper)
            break
        else:
            print(f"Статус операции {status_inport} недоступен\n")

    user_sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if user_sort_choice == "да":
        data_order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        is_descending = "убыв" in data_order
        data = sort_by_date(data, reverse=is_descending)

    rub = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if rub == "да":
        data = [
            tx
            for tx in data
            if tx.get("currency_code") == "RUB"
            or tx.get("currency_name") == "руб."
            or tx.get("currency") == "RUB"
            or tx.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    filter_by_word = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    )
    if filter_by_word == "да":
        search_word = input("Введите слово для поиска: ")
        data = process_bank_search(data, search_word)
    print("Распечатываю итоговый список транзакций...\n")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        for tx in data:
            raw_date = tx.get("date")
            formatted_date = get_date(raw_date) if raw_date else "Дата неизвестна"
            print(f"{formatted_date} {tx.get('description', '')}")
            card_from = tx.get("from")
            card_to = tx.get("to")
            is_from_valid = isinstance(card_from, str) and card_from.strip()
            is_to_valid = isinstance(card_to, str) and card_to.strip()
            if is_from_valid:
                masked_from = mask_account_card(card_from)
                masked_to = mask_account_card(card_to) if is_to_valid else "Счет неизвестен"
                print(f"{masked_from} -> {masked_to}")
            elif is_to_valid:
                masked_to = mask_account_card(card_to)
                print(f"{masked_to}")
            amount = tx.get("amount")
            if amount is None and "operationAmount" in tx:
                amount = tx.get("operationAmount", {}).get("amount")
            currency = tx.get("currency_code") or tx.get("currency_name") or tx.get("currency")
            if not currency and "operationAmount" in tx:
                currency = tx.get("operationAmount", {}).get("currency", {}).get("name")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
