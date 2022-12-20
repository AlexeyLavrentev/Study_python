# Создать телефонный справочник с возможностью импорта и экспорта данных .
# Что должен уметь справочник?
# *  Добавить новый контакт
# * Поиск контакта по имени
# *Пример информации в справочнике:*
# Исаев Владислав Иванович || +3456789087565
# Наиль Н. || +45678987654

from input_contacts import *
from output_contacts import *


def start():
    choice = None
    while choice != 0:
        print_menu()
        choice = int(input('Ваш выбор: '))
        if choice == 1:
            read()
        elif choice == 2:
            search_contact(contact())
        elif choice == 3:
            write(add_contact())
        elif choice == 4:
            delete(contact())
        elif 0:
            exit()