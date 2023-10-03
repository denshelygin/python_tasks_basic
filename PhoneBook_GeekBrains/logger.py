def log_to_file(contact):

    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}, {contact[1]}, {contact[2]}, {contact[3]}\n')

def reading_file(param):
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if param in line:
                    print(line)



def reading_all():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line)
