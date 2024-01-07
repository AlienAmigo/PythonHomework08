from config import *
from date_create import *


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
