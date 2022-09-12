# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    # Пример:
    # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random as r

n = int(input("Задайте длину списка чисел -> "))

def create_list(length: int, min_value: int, max_value: int):
    result = []
    for i in range(0, n):
        result.append(r.randint(min_value, max_value))
    return result

def find_odd_position_sum(input_list: list):
    result_list = []
    sum = 0
    for i in range(1, len(input_list), 2):
        result_list.append(input_list[i])
        sum += input_list[i]
    print(f'На нечетных позициях элементы: {result_list}, сумма равна: {sum}')

number_list = create_list(n, 0, 10)
print(number_list)
find_odd_position_sum(number_list)
