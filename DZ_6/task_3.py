# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.



def sequence_list():

    """Функция принимает число формируетсписок из членов последовательности"""

    seq_lst = (list((-3)**i for i in range(int(input('введите n: ')))))
    return seq_lst


 


