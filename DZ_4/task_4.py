# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов 
# влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, 
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, 
# которая спрашивает ключ, считывает текст и дешифровывает его.

def get_encript_text():
    
    encryption = ""
    for c in text:
        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
        else:
            encryption += c
        with open('Pr/2.txt', 'w' ,encoding='utf-8') as file_list:
             file_list.write(encryption)
    return(encryption)

shift = int(input('Шаг шифровки: '))
text = input("Сообщение для шифровки: ").upper()
get_encript_text()