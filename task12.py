# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

numbers_sum = int(input('Enter sum: '))
numbers_mult = int(input('Enter mult: '))

iterration = numbers_sum if numbers_sum < 1000 else 1000

#resolve with flag
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


#resolve with for...in...else
for i in range(1, iterration):
    for j in range(1, iterration):
        if i + j == numbers_sum and i * j == numbers_mult:
            print(f" first number is {i} and second number is {j}") # аншли числа
            break #прервали внутр цикл, else не выполниться, перейдет на след строку, а она тоже break для внешнего цикла
    else: #если break не было, 
        continue #то переход на след i внешнего цикла
    break #если был break внутри, то выкинет сюда, на break снаружи и внешний цикл тоже прервется, внешний else не сработает
else: #если break снаружи не было,
    print("Numbers are not exist") #то таких чисел нет

#resolve one cycle run
for i in range(1, 1000):
    if ((j := numbers_sum - i) == numbers_mult // i) and (numbers_mult % i == 0):
        print(f" first number is {i} and second number is {j}")
        break
else:
    print("Numbers are not exist")
