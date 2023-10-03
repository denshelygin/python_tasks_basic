# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

real_num = float(input('Введите вещественное число: '))                      
if float(real_num) < 0:                         
        real_num = float(real_num) * (-1)
while real_num != int(real_num):
    real_num *= 10
sum_num = 0
while real_num > 0:
    sum_num += real_num % 10
    real_num //= 10
print(sum_num)