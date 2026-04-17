import os

import pytest

from src.decorators import log


# 1. Тест вывода в консоль
def test_log_to_console(capsys):
    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert "add. Result: 3" in captured.out


def test_log_to_file():
    test_file = "test_log.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    @log(filename=test_file)
    def multiply(x, y):
        return x * y

    multiply(2, 5)

    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "multiply. Result: 10" in content
    os.remove(test_file)  # Чистим за собой


def test_log_error(capsys):
    @log()
    def divide(x, y):
        return x / y

    result = divide(10, 0)
    captured = capsys.readouterr()

    assert result is None
    assert "Ошибка в функции divide: ZeroDivisionError" in captured.out
    assert "inputs: (10, 0)" in captured.out
