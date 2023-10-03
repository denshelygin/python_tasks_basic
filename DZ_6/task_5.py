# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, 
# первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]


from random import randint

def list_of_tuples():

    """Функция принимает на вход список из случайных чисел и список индексов и 
     обьеденяет их в кортежи и удаляет кортежи у которых индекс и число совпадают"""

    numbers = [randint(0, 20) for i in range(10)]
    indexs = [n for n in range(10)]
    sum_zip = list(zip(indexs,numbers))
    print(sum_zip)
    for indexs, numbers in sum_zip:
        if indexs == numbers:
            sum_zip.pop(indexs)
    return(sum_zip)

print(list_of_tuples())

