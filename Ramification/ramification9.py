# Даны два целых числа - координаты клетки на шахматной доске.
# Первое число от 1 до 8 обозначает
# вертикаль снизу вверх, второе - горизонталь слева направо.
# Напечатайте слово "Белая", если клетка на данных координатах
# белая и "Чёрная", если клетка чёрная.1*1 чёрная.
a = int(input())
b = int(input())
if a % 2 ==0 and b % 2 ==0:
    print('Белая')
else:
    print('Чёрная')
