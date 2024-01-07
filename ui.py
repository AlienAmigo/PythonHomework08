from logger import *


def interface():
  with open('phonebook.txt', 'a', encoding='utf-8'):
    pass

  command = '-1'

  while command != '4':
    print('Возможные варианты взаимодействия:\n' +
          bcolors.OKGREEN + '1. ' + bcolors.ENDC + 'Добавить контакт ➕ \n' +
          bcolors.OKGREEN + '2. ' + bcolors.ENDC + 'Вывести на экран 📋 \n' +
          bcolors.OKGREEN + '3. ' + bcolors.ENDC + 'Поиск контакта 🔎 \n' +
          bcolors.OKGREEN + '4. ' + bcolors.ENDC + 'Выход из программы 🚪 \n'
          )

    command = input('Введите номер действия: ')

    while command.strip() not in ('1', '2', '3', '4'):
      print(bcolors.FAIL + 'Некорректные данные, нужно ввести число (1-4) ', bcolors.ENDC)
      command = input('Введите номер действия: ')

    match command:
      case '1':
        add_contact()
      case '2':
        show_info()
      case '3':
        search_contact()
      case '4':
        print(bcolors.OKGREEN + 'Good Luck!'+bcolors.ENDC, '👍')
