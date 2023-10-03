# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


def non_repeating_elements():

    """ Принимает строку и 
    эту строку возвращает уже 
    без слова исключения"""

    split_line = stroka.split()
    newlist = []
    for i in split_line:
        if i != word_delite in split_line:
            newlist.append(i)
    newlist = " ".join(newlist)
    print("Начальная строка:", (stroka))
    print("Строка без слова исключения:", (newlist))

stroka = "Пугать ты галок пугай"
word_delite = 'галок'
non_repeating_elements()
