# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # Пример:
    # для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число k -> '))

def negafibonacci(k:int):
    pos_f = [0, 1, 1]
    neg_f = []
    
    for i in range(3, k + 1):
        pos_f.append(pos_f[i - 1] + pos_f[i - 2])
        
    for j in range(1, k + 1):
        neg_f.append((-1)**(j+1)*pos_f[j])
    
    neg_f = neg_f[::-1]
    neg_f.extend(pos_f)
    return neg_f

print(negafibonacci(k))