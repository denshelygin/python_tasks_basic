# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_index(lst):
    sum = 0
    for i in range (len(lst)):
        if i % 2 !=0 :
            sum += lst[i]    
    print(lst)
    print(f"Сумма равна: {sum}")

lst = [9, 2, 11, 5, 3, 5, 9, 3]
sum_index(lst)