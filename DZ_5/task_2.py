# 2-Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, 
# лучше выделите в отдельные функции бота и умного бота.

import random

def igrok_vs_igrok():
    name1 = input("Введите имя первого игрока: ", )
    name2 = input("Введите имя второго игрока: ", )
    count = 0
    number_of_candies = 2021
    first_run = random.randint(1, 2)
    if first_run == 1:
        run1 = name1
        run2 = name2
        print("Ходит :", name1)
    else:
        run1 = name2
        run2 = name1
        print("Ходит :", name2)
    while number_of_candies > 0:
        if count == 0:
            step = int(input(f'\n{"Введите количество конфет не более 28:"} {run1} = '))
            number_of_candies = number_of_candies - step
            print(number_of_candies)
        if number_of_candies > 0:
            print(f'\nКонфет  еще {number_of_candies}')
            count = 1
        else:
            print('Конфеты закончились')
        if count == 1:
            step = int(input(f'\n{"Введите количество конфет не более 28:"}, {run2} = '))
            number_of_candies = number_of_candies - step
            print(number_of_candies)
        if number_of_candies > 0:
            print(f'\nКонфет  еще {number_of_candies}')
            count = 0
        else:
            print('Конфеты закончились')
    if count == 1:
        print(f' Выиграл{run2}')
    if count == 0:
        print(f' Выиграл{run1}')

igrok_vs_igrok()



