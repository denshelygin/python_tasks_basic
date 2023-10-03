#4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
url_list = ['https://yandex.ru/internet',
            'https://gb.ru/lessons/284812',
            'https://pythonist.ru/kogda-ispolzovat-list-comprehension-v-python/',
            'https://rp5.ru/Погода_в_Санкт-Петербурге',
            'https://www.dns-shop.ru/',
            'https://www.ozon.ru/']

def domen_names(url_list:str) -> str:

    """Функция принимает на вход список из url адресов и сотавляет список доменных имен сайтов."""

    dom_lst = []
    for i in range(len(url_list)):
        count = url_list[i].partition('//')[-1]
        count = count.partition(('/'))[0]
        dom_lst.append(count)
    return dom_lst

