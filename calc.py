import math #импорт библиотеки math

def add(x, y): #сложение Х с У
    return x + y
def subtract(x, y): #вычитание У из Х
    return x - y
def multiply(x, y): #умножение Х на У
    return x * y
def divide(x, y): #деление Х на У
    if y != 0: #проверка на равенство 0, если у == 0, то ошибка
        return x / y
    else:
        return "Делить на ноль нельзя!"
def sqrt(x): #квадратный корень числа Х
    return math.sqrt(x)
def procent(x, y): #вычисление процента У из Х
    return (x * y) / 100
def stepen(x, y): #возведение числа Х в степень У
    return x**y

#предложение выбора операции
print('Список доступных оперций:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Квадратный корень')
print('6. Процент')
print('7. Возведение в степень')
print()

#ввод выборанной операции
choice = input('Введи номер операции: ')

if choice == '1':
    num1 = float(input('Введи первое число: '))
    num2 = float(input('Введи второе число: '))
    print(f"Результат сложения: {add(num1, num2)}")
elif choice == '2':
    num1 = float(input('Введи первое число: '))
    num2 = float(input('Введи второе число: '))
    print(f"Результат вычитания: {subtract(num1, num2)}")
elif choice == '3':
    num1 = float(input('Введи первое число: '))
    num2 = float(input('Введи второе число: '))
    print(f"Результат умножения: {multiply(num1, num2)}")
elif choice == '4':
    num1 = float(input('Введи первое число: '))
    num2 = float(input('Введи второе число: '))
    print(f"Результат деления: {divide(num1, num2)}")
elif choice == '5':
    num1 = float(input('Введи число: '))
    print(f"Результат вычисления квадратного корня: {sqrt(num1)}")
elif choice == '6':
    num1 = float(input('Введи число из которого вычитается процент: '))
    num2 = float(input('Введи процент: '))
    print(f"Результат вычисления процента: {procent(num1, num2)}%")
elif choice == '7':
    num1 = float(input('Введи возводимое в степень число: '))
    num2 = float(input('Введи степень : '))
    print(f'Результат возведения в степень: {stepen(num1, num2)}')
else:
    print("Ввведнный выбор не корректен")