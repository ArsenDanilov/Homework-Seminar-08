def read_data():
    with open('Task.txt', 'r', encoding='utf-8') as file:
        contact_list = list(file.readlines())
    return contact_list


def menu_data(contact_list):
    print('-------------------------------------МЕНЮ КОНТАКТНОГО СПРАВОЧНИКА-------------------------------------')
    print()
    print('\nВывод списка контактов: \n')
    for i in contact_list:
        print(i.strip())
    print('\n Выберите действие для работы со справочником: \n')
    print('1 - добавить контакт')
    print('2 - сделать перезапись справочника')
    print('3 - найти контакт по ФИО или номеру телефона')
    print('4 - изменить информацию о контакте')
    print('5 - удалить контакт')
    print()
    print('------------------------------------------------------------------------------------------------------')

    button = int(input('Выберите номер действия: '))

    if button == 1:
        add_user(contact_list)
    if button == 2:
        write_data(contact_list)
    if button == 3:
        search_data(contact_list)
    if button == 4:
        change_data(contact_list)
    if button == 5:
        delete_data(contact_list)
    # if button < 1 or button > 6:
    #     print('Указанное действие недоступно для выполнения')


def add_user(contact_list):
    with open('Task.txt', 'w', encoding='utf-8') as file:
        contact_list.append(input(str('\nДобавьте ФИО и номер телефона нового контакта: \n').strip))
        print('\nКонтакт успешно добавлен!')


def write_data(contact_list):
    with open('Task.txt', 'w', encoding='utf-8') as file:
        print('\nВыполняется процесс перезаписи данных контактного списка... \n')
        file.writelines(contact_list)
        print('\nДанные успешно перезаписаны!')

def search_data(contact_list):
    search = input('Введите ФИО или номер искомого человека: ')
    for element in contact_list:
        if search in contact_list:
            print('\n' +'Вывод найденного контакта: '+search.strip())
            break
        else:
            print('Нет ни одного совпадения по введённому параметру')
            break

def change_data(new_contact_list):
    
    new_contact_list = contact_list
    new_contact_list.replace(input('Введите старые данные: '), input('Введите новые данные: '))

    with open('Task.txt', 'w', encoding='utf-8') as file:
        file.writelines(contact_list)
        print('Данные успешно перезаписаны!')

def delete_data(contact_list):
    with open('Task.txt', 'w', encoding='utf-8') as file:
        print(f'Вывод контактного списка: \n')
        contact_list.pop(int(input('\nВведите номер контакта в списке, который вы бы хотели удалить: ')))
        file.writelines(contact_list)
        print('Контакт успешно удалён!')

contact_list = read_data()
menu_data(contact_list)
        

    

    


