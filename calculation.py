#A simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division).
import sys

import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Ошибка: На ноль делить нельзя")
        sys.exit()
    else:
        return x / y

while True:
    try:
        x = float(input("Пожалуйста, введите первое число: "))
        y = float(input("Пожалуйста, введите второе число: "))
    except ValueError:
        print("Ошибка: Введите корректное числовое значение.")
        sys.exit()

    operator = input("Выберите операцию +, -, *, /: ")
    if operator not in ['+', '-', '*', '/']:
        print("Ошибка: Некорректный оператор")
        sys.exit()

    if operator == "+":
        result = add(x, y)
    elif operator == "-":
        result = subtract(x, y)
    elif operator == "*":
        result = multiply(x, y)
    elif operator == "/": 
        result = divide(x, y)

    precision = int(input("Введите количество знаков после запятой: "))
    print(f"Результат: {result:.{precision}f}")

    another_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
    if another_calculation.lower() != 'да':
        break

