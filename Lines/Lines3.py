# Дана строка, которая может содержать букву f.
# Напечатайте позицию первого и последнего вхождения f.
# Если буква f встречается только один раз, то
# выведите позицию один раз. Если буква f не встречается, напечатайте -1.
# Позиции букв в слове считайте с 0. Например, в слове hello буква h находится в позиции 0,
# буква e - в позиции 1, буква o - в позиции 4.
a = input()
if a.count('f') == 1:
    print(a.find('f'))
else:
    print(-1)


