def find():
    """ Ищет контакт по одному из  выбранных параметров """
    print('По какому параметру ищем контакт: \n\
            1 - Имя;\n\
            2 - Фамилия;\n\
            3 - Номер;\n\
            4 - Комментарий.\n')
    a = int(input('Введите номер поиска: '))
    if a == 1:
        contact = input('Введите имя: ').title()
    if a == 2:
        contact = input('Введите фамилию: ').title()
    if a == 3:
        contact = input('Введите номер: ')
    if a == 4:
        contact = input('Введите комментарий: ').title()

    print('Будем искать по: ', contact)
    return contact