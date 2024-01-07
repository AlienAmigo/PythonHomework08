from config import *
from data_create import *


def add_contact():
  show_title('Добавить контакт:')
  contact = create_contact()
  with open(config.DATA_FILE, 'a', encoding='utf-8') as file:
    file.write(contact)


def show_info():
  show_title('Список контактов:')
  with open(config.DATA_FILE, 'r', encoding='utf-8') as file:
    contacts_list = file.read().strip().split('\n\n')
    for nn, contact in enumerate(contacts_list, 1):
      print(bcolors.WARNING + str(nn) + '.' +
            bcolors.ENDC, contact.replace('\n', ' '))


def search_contact():
  show_title('Поиск контакта:')

  def create_searh_menu():
    return '\n'.join([f'{bcolors.OKBLUE}{i}. {bcolors.ENDC}{item}' for i, item in enumerate(search_menu, 1)])

  print('Возможные варианты поиска:\n' + create_searh_menu() + '\n')
  var_search = input('Выберите вариант поиска: ')

  while var_search.strip() not in str(tuple(range(1, len(search_menu) + 1))):
    show_error(
        f'Некорректные данные, нужно ввести число (1-{len(search_menu)}): ')
    var_search = input('Выберите вариант поиска: ')

  index_var = int(var_search) - 1
  search = input('Введите данные для поиска: ')
  with open(config.DATA_FILE, 'r', encoding='utf-8') as file:
    contacts_list = file.read().strip().split('\n\n')

  for contact_str in contacts_list:
    contact_lst = contact_str.replace('\n', ' ').split()
    if search in contact_lst[index_var]:
      print(contact_str)


def transfer_contact():
  show_title('Перенос контакта: ')
  show_info()
  with open(config.DATA_FILE, 'r', encoding='utf-8') as file:
    contacts_list = file.read().strip().split('\n\n')
    transfer_index = int(input('Введите индекс контакта для перемещения: '))

    if transfer_index in tuple(range(1, len(contacts_list) + 1)):
      target_file = input('Введите имя файла для перемещения контакта: ')
      if target_file != config.DATA_FILE:
        with open(target_file, 'a', encoding='utf-8') as target:
          target.write(contacts_list[transfer_index - 1] + '\n\n')
      else:
        show_error('Нельзя перенести контакт в исходный файл!')
    else:
      show_error(
          f'Контакта с таким индексом ({transfer_index}) не существует!')
