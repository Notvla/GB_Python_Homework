# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Ошибка ввода')
elif n == 1:
    print('X > 0 и Y > 0')
elif n == 2:
    print('X < 0 и Y > 0')
elif n == 3:
    print('X < 0 и Y < 0')
elif n == 4:
    print('X > 0 и Y < 0')