import csv

def creating():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        fieldnames = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный']
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writeheader()