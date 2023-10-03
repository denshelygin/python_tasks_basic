# 5- Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

point_ax = float(input('Введите координаты точки a по оси x:'))
point_ay = float(input('Введите координаты точки a по оси y:'))
point_bx = float(input('Введите координаты точки b по оси x:'))
point_by = float(input('Введите координаты точки b по оси y:'))
import math
distans = math.sqrt((point_ax - point_bx)**2+(point_ay - point_by)**2)
print (round(distans, 3)) 
