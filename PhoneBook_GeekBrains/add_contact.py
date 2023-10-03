def add_contact():
    """ Добавляет ФИО, номер телефона и комментарий в список 
    Return: list"""
    contact = []
    name = input('Введите имя: ')
    contact.append(name.title())
    lastname = input('Введите фамилию: ')
    contact.append(lastname.title())
    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)
    any_info = input('Комментарий: ')
    contact.append(any_info.title())
    print('Абонент записан: ', *contact)
    return contact

