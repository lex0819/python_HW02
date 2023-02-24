# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

numbers_sum = int(input('Enter sum: '))
numbers_mult = int(input('Enter mult: '))

iterration = numbers_sum if numbers_sum < 1000 else 1000
flag = False

for i in range(1, iterration):
    flag = False #not found
    for j in range(1, iterration):
        if i + j == numbers_sum and i * j == numbers_mult:
            print(f" first number is {i} and second number is {j}")
            flag = True #numbers are found
            break
    if flag:
        break

if flag == False:
    print("Numbers are not exist")