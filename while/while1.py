# Дано целое число не меньше 2.
# Напечатайте наименьший целочисленный делитель данного числа больший 1.
a = int(input())
b = 2
while a % b != 0:
    b += 1
print(b)
