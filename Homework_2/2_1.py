# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

x = input('Введите число ')
def summa(x):
    if float(x) < 0:
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number
print(f'Сумма чисел равна {summa(x)}')