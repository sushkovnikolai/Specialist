# Даны два целых числа отличные от числа 0.
# Напечатайте "Да", если хотя бы одно число является положительным и "Нет", если оба числа
# отрицательные.
a =int(input())
b =int(input())
if a or b > 0:
    print('Да')
else:
    print('Нет')
