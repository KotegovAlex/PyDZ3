# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    # Пример:
    # [2, 3, 4, 5, 6] => [12, 15, 16];
    # [2, 3, 5, 6] => [12, 15]

import random as r

n = int(input("Задайте длину списка чисел -> "))

def create_list(length: int, min_value: int, max_value: int):
    result = []
    for i in range(0, n):
        result.append(r.randint(min_value, max_value))
    return result

def number_pair_composition(input_list: list):
    result_list = []
    i = 0
    j = len(input_list) - 1

    while i <= j:
        result_list.append(input_list[i] * input_list[j])
        i += 1
        j -= 1
    
    return result_list


number_list = create_list(n, 0, 10)
print(number_list)
print(number_pair_composition(number_list))