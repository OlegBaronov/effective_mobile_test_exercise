import csv


def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    surname = input('ВВедите отчество: ')
    info.append(surname)
    name_of_the_organization = input('Введите название организации: ')
    info.append(name_of_the_organization)
    work_phone = ''
    valid = False
    while not valid:
        try:
            work_phone = input('Введите номер рабочего телефона: ')
            if len(work_phone) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                work_phone = int(work_phone)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(work_phone)
    personal_phone = ''
    valid = False
    while not valid:
        try:
            personal_phone = input('Введите номер личного телефона: ')
            if len(personal_phone) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                personal_phone = int(personal_phone)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(personal_phone)
    return info


def writing_csv(info):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        writer = csv.writer(data)
        writer.writerow(info)
    print('Данные сохранены')


