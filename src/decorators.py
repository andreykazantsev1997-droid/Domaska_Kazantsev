import functools


def log(filename=None):
    """Декоратор, который логирует выполнение функции."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__}. Result: {result}"
            except Exception as e:
                inputs = f"inputs: {args},{kwargs}"
                log_message = f"Ошибка в функции {func.__name__}: {type(e).__name__}. Сообщение: {inputs}"
                result = None
            if filename:
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                print(log_message.strip())
            return result
        return wrapper
    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

print(my_function(1, 2))