import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_in_rub(transaction):
    """Функция, которая принимает транзакцию и конвертирует её сумму в рубли"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        try:
            response = requests.get(url, headers=headers)
            transactions = response.json()
            return float(transactions["result"])
        except Exception:
            return 0.0
    return 0.0


# if __name__ == "__main__":
#     test_transaction = {
#         "operationAmount": {
#             "amount": "100.00",
#             "currency": {"code": "USD"}
#         }
#     }
#
#     print(get_amount_in_rub(test_transaction))
