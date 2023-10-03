# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from random import randint

def list_of_tuples():

    """Функция принимает на вход список из случайных чисел и список индексов и 
     обьеденяет их в кортежи и оставляет кортежи где сумма кортежа кратна 5"""

    numbers = [randint(0, 20) for i in range(10)]
    indexs = [n for n in range(20)]
    sum_zip = list(zip(indexs,numbers))
    print(sum_zip)
    for indexs, numbers in sum_zip:
        if (indexs + numbers) % 5 == 0:
            sum_zip = sum_zip.pop(indexs)
            return(sum_zip)

print(list_of_tuples())