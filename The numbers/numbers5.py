# Дано целое число из трёх цифр.
# Напечатайте сумму цифр у числа.
nam = int(input())
f_nam = nam //100
s_nam = (nam // 10) % 10
th_num = nam % 10
result = f_nam + s_nam + th_num
print(result)
