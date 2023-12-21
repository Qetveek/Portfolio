#Простой калькулятор, который выполняет основные арифметические операции (сложение, вычитание, умножение, деление).
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

x = float(input("Пожалуйста, введите первое число: "))
operator = input("Выберите операцию +, -, *, /: ")
y = float(input("Пожалуйста, введите второе число: "))

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

print(f"Результат: {result:.2f}")

