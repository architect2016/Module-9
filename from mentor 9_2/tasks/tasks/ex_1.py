"""
Напишіть decorator, який записує в консоль два повідомлення журналу:
: call [номер_виклику_функції]: [ім'я функції][її аргументи]\n
: result: [ім'я функції][результат]\n
"""
import sys


def logger(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        sys.stdout.write(f": call [{counter}]: [{func.__name__}][{args}]\n")
        result = func(*args, **kwargs)
        sys.stdout.write(f": result: [{func.__name__}][{result}]\n")
        return result
    return inner

@logger
def add(x, y):
    return x + y


@logger
def sub(x, y):
    return x - y


print(add(4, 5))
print(add(33, 11))
print(sub(33, 11))
print(add(1, 4))
print(sub(5, 6))
