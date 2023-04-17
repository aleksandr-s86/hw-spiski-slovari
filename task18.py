"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random

size = (int(input("Введите размер списка : ")))
my_list = [random.randint(0,10) for _ in range(size)] 

print(my_list)
num = (int(input('Введите искомое число : ')))
min = abs(num-my_list[0])
index=0
for i in range(1,size):
    count=abs(num-my_list[i])
    if count<min:
        min = count
        index = i
print(f'Число {num}, наиболее близко в списке к числу {my_list[index]}')