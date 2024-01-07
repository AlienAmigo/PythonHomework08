# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1) Создать телефонный справочник:    +++
# - Открыть файл в режиме добавления (a)    +++
# 2) Добавить контакт:
# - Запросить информацию у пользователя   +++
# - Подготовить данные в необходимом формате   +++
# - Открыть файл в режиме добавления (a)
# - Добавить контакт в файл
# 3) Вывести данные из файла на экран:
# - Открыть файл в режиме чтения (r)
# - Вывести информацию на экран
# 4) Поиск данных:
# - Запросить вариант поиска
# - Запросить данные поиска
# - Открыть файл в режиме чтения (r)
# - Осуществить поиск по файлу
# - Вывести нужную информацию на экран
# 5) Реализовать UI:
# - Вывести варианты меню   +++
# - Получение запроса пользователя   +++
# - Реализация запроса пользователя   +++
# - Выход из программы   +++

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def input_name():
  return input('Введите имя: ')


def input_surname():
  return input('Введите фамилию: ')


def input_patronymic():
  return input('Введите отчество: ')


def input_phone():
  return input('Введите номер телефона: ')


def input_address():
  return input('Введите адрес: ')


def create_contact():
  surname = input_surname()
  name = input_name()
  patronymic = input_patronymic()
  phone = input_phone()
  address = input_address()

  return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def add_contact():
  contact = create_contact()
  with open('phonebook.txt', 'a', encoding='utf-8') as file:
    file.write(contact)


def show_info():
  with open('phonebook.txt', 'r', encoding='utf-8') as file:
    contacts_list = file.read().strip().split('\n\n')
    # print(file.read().strip())
    for nn, contact in enumerate(contacts_list, 1):
      print(nn, contact)
    # print(*enumerate(contacts_list, 1))


def search_contact():

  print('Возможные варианты поиска:\n' +
        bcolors.OKBLUE + '1. ' + bcolors.ENDC + 'По фамилии\n' +
        bcolors.OKBLUE + '2. ' + bcolors.ENDC + 'По имени\n' +
        bcolors.OKBLUE + '3. ' + bcolors.ENDC + 'По адресу\n' +
        bcolors.OKBLUE + '4. ' + bcolors.ENDC + 'По номеру телефона\n' +
        bcolors.OKBLUE + '5. ' + bcolors.ENDC + 'По адресу\n'
        )
  var_search = input('Выберите вариант поиска: ')

  while var_search.strip() not in ('1', '2', '3', '4', '5'):
    print(bcolors.FAIL + 'Некорректные данные, нужно ввести число (1-5): ', bcolors.ENDC)
    var_search = input('Выберите вариант поиска: ')

  index_var = int(var_search) - 1
  search = input('Введите данные для поиска: ')
  with open('phonebook.txt', 'r', encoding='utf-8') as file:
    contacts_list = file.read().strip().split('\n\n')

  for contact_str in contacts_list:
    contact_lst = contact_str.replace('\n', ' ').split()
    if search in contact_lst[index_var]:
      print(contact_str)


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


interface()
