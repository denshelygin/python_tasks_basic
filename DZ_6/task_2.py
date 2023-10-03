#2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import math
lst = [6, 3, 4, 9, 5, 7, 6, 9, 3, 5, 4, 7, 8, 9]

def com_index(lst:str) ->int:

    """Функция принимает список из целых чисел и выводит призведение пар чисел в списке"""
    
    mult_of_numbers = list(map(lambda i:(lst[i]*lst[-(i+1)]), [i for i in range(math.ceil(len(lst)/2))]))
    return mult_of_numbers

print(com_index(lst))
