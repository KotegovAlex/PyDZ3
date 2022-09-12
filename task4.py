# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    # Пример:
    # 45 -> 101101
    # 3 -> 11
    # 2 -> 10

# Вариант 1:

# bin_number = bin(int(input('Введите десятичное число -> ')))
# print(bin_number[2:])

# # Вариант 2:

dec_number = int(input('Введите десятичное число -> '))

def dec_to_bin(dec_num:int):
    temp = dec_num
    result = ''
    while temp > 2:
        result = result + str(temp % 2)
        temp = temp // 2
    else:
        result = result + '1'

    result = result[::-1]
    return result

print(f'Десятичное {dec_number} равно двоичному {dec_to_bin(dec_number)}')