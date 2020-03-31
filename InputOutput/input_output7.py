# Даны две метки времени одного дня. Метка времени состоит из полного количества часов, минут и
# секунд, например: 1 15 23 - один час 15 минут и 23 секунды.
# Первая метка времени произошлараньше второй.
# Напишите код, который вычисляет разницу между двумя метками в секундах.
first_hour = int(input()) * 3600
first_minut = int(input()) * 60
first_second = int(input())
second_hour = int(input()) * 3600
second_minut = int(input()) * 60
second_second = int(input())
result = (second_hour + second_minut + second_second) - (first_hour + first_minut + first_second)
print(result)


