# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
    # Пример:
    # [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random as r

n = int(input("Задайте длину списка чисел -> "))

def create_list(length: int, min_value: int, max_value: int):
    result = []
    for i in range(0, length):
        result.append(round((r.random()*(max_value - min_value) + min_value), 2))
    return result

def fraction_parts_diff(input_list: list):
    temp_list = []

    for i in input_list:
        temp_list.append(i % 1)
        
    # print(temp_list)
    return round((max(temp_list) - min(temp_list)), 2)

number_list = create_list(n, 0, 10)
print(f'Исходный список: {number_list}')
print(f'Разница дробных частей: {fraction_parts_diff(number_list)}')