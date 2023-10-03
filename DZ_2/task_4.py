# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
#  Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку,
#   а сам выбывает из круга. 
#   Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. 
#   Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте библиотеку
#    time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, 
#    которые оказались у него в конце игры.

people = int(input('Кол-во человек: '))
dropped = int(input('Число в считалке? '))
print('Значит, выбывает каждый', dropped, 'человек.')
people_list = list(range(1, people + 1))
out = 0
sum = 0
 
for i in range(people - 1):
    print('\nОстались:', people_list)
    money = ((len(people_list))* 2) - 1
    start_count = out % len(people_list)
    out = (start_count + dropped - 1) % len(people_list)
    print('Счёт c:', people_list[start_count])
    print('Вылетает:', people_list[out])
    people_list.remove(people_list[out])
    sum +=money
    print("Добавилось монет:", money)
    print("Монет всего:", sum)

print('\nОстался человек под номером', *people_list, 'с колличеством монет', sum)