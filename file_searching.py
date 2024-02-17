import pandas as pd
from pathlib import Path
import csv
def search(key,value):
    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=",")
        result_search = []
        for row in file_reader:
            if row[key].lower() == value.lower():
                result_search.append(row)
    if len(result_search) != 0:
        return result_search
    else:
        return f'Абонент не найден'

def search_name():
    last_name = input('Введите фамилию: ').title()
    first_name = input('Введите имя: ').title()
    surname = input('Введите отчество: ').title()

    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=",")
        result_search = []
        for row in file_reader:
            if row['Фамилия'].lower() == last_name.lower() and row['Имя'].lower() == first_name.lower() and row[
                'Отчество'].lower() == surname.lower():
                result_search.append(row)
    if len(result_search) != 0:
        return result_search
    else:
        return f'Абонент не найден'

def searching_info():
    flag_search = input('Для поика по Ф.И.О нажмите \'1\' для поиска названию организации нажмите \'2\' для поска по номеру рабочего телефона нажмите \'3\' для поиска по номеру личного телефона нажмите \'4\'')
    if flag_search == '1':
        print(search_name())

    if flag_search == '2':
        company_name = input('Введите название организации: ').title()
        key = 'Название организации'
        value = company_name
        print(search(key, value))

    if flag_search == '3':
        work_phone = input('Введите номер рабочего телефона: ')
        key = 'Телефон рабочий'
        value = work_phone
        print(search(key, value))

    if flag_search == '4':
        personal_phone = input('Введите номер личного телефона: ')
        key = 'Телефон личный'
        value = personal_phone
        print(search(key, value))