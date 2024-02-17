import csv
from file_searching import search_name
def search(key,value):
    with open('Phonebook.csv', 'r', encoding='utf-8') as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=",")
        for row in file_reader:
            if row[key].lower() == value.lower():
                return(row)

def change():
    print('Введите данные абонента, данные которого Вы хотите изменить ')
    name = search_name()
    if type(name) == list:
        new_key = input("Введите данные которые требуется заменить('Фамилия' ,'Имя', 'отчество','Название организации', 'Телефон рабочий', 'Телефон личный'): ")
        new_value = input("Введите новые данные: ")
        with open('Phonebook.csv', encoding='utf-8') as f:
            file_reader = csv.DictReader(f)
            list_data = []
            for row in file_reader:
                list_data.append(row)
        name = name[0]
        for data in list_data:
            if data == name:
                data[new_key] = new_value
                print(data)
                print(name)



        with open('Phonebook.csv', 'w', encoding='utf-8') as data:
            fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_data)
            print('Данные абонента изменены')
    else:
        print(name)