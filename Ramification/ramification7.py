# Дано целое положительное число из четырёх.
# Число может является палиндромом, то есть читаться
# одинакого слева направо и справа налево
# Напечатайте "Да", если число является палиндромом и "Нет", если не является.
a = input()
if a[:] == a[ : : -1]:
   print('Да')
else:
    print('Нет')
