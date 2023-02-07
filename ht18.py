# Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

import random

num = int(input('Введите длину списка: '))

list = list()
for i in range(num):
        list.append(random.randint(0,10))
print(list)

num1 = int(input('Введите число: '))
x = 0
list_1 = []

for i in range(num):
    x = num1 - list[i]
    list_1.append(abs(x))

min = list_1[0]
index = 0
for i in range(num):
    if list_1[i] < min:
        min = list_1[i]
        index = i
print (f'Ближайшее число к введенному - {list[index]}')
