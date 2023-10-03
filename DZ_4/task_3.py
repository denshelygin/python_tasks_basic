# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4
from typing import List

def change_list(lst: List[str], accept: str) -> str:

    file_list = ''
    for student in lst:
        if student.count(accept):
            student = student.upper()
        string = student + '\n'
        file_list += string
    return(file_list)
   
with open('Pr/1.txt', 'r' ,encoding='utf-8') as file_list:
    lines_list = file_list.read().split('\n')

lst_new = change_list(lines_list, accept = '5')

with open('Pr/1.txt', 'a' ,encoding='utf-8') as file_list:
    file_list.write(lst_new)