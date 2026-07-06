import csv
import os

import pandas as pd


def get_transactions_from_csv(file_path):
    """Функция, которая считывает финансовые операции из csv и возвращает список словарей"""
    transactions = []
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(dict(row))
    return transactions


# print(get_transactions_from_csv("../data/transactions.csv"))


def get_transactions_from_excel(file_path):
    """Функция, которая считывает финансовые операции из Excel и возвращает список словарей"""
    if not os.path.exists(file_path):
        return []
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient="records")
    return transactions


# print(get_transactions_from_excel("../data/transactions_excel.xlsx"))
