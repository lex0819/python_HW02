# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.

n = int(input('enter n which more than 2: '))

i = 0
while ( item := 2 ** i ) < n:
    print(f"{i} {item}")
    i += 1