# Дано целое двузначное число.
# Напечатайте число, в котором правая и левая цифры поменяны местами
nam = int(input())
f_nam = nam // 10
s_nam = nam % 10
print(s_nam, f_nam, sep="")
