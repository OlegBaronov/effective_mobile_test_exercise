from os.path import exists
from csv_creating import creating
from file_writing import writing_csv, get_info
from export import from_file
from file_searching import searching_info
from file_change import change
def view():
     print(from_file('Phonebook.csv'))


def record_info():
    info = get_info()
    writing_csv(info)










def choice():
    flag = input(
        'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите \'Запись\', если хотите записать новые данные, \'Изменение\' для измения данных, \'Поиск\' для поиска абонента и \'Просмотр\', если хотите просмотреть справочник в консоли: ')
        if choice_action.lower() == 'запись':
            record_info()
        if choice_action.lower() =='изменение':
            change()
        if choice_action.lower() == 'поиск':
            searching_info()
        if choice_action.lower() == 'просмотр':
            view()
        else:
            flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
            print('Программа завершена.')
