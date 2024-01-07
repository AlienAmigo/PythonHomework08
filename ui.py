from config import *
from logger import *


def create_menu_list():
  return '\n'.join([f'{bcolors.OKGREEN}{nn}.{bcolors.ENDC} {el}' for nn, el in enumerate(main_menu, 1)])


def interface():
  with open(config.DATA_FILE, 'a', encoding='utf-8'):
    pass

  command = '-1'

  while command != '5':
    print(f'\n{bcolors.BOLD}> Возможные варианты взаимодействия:{bcolors.ENDC}\n{create_menu_list()}\n')

    command = input('Введите номер действия: ')

    while command.strip() not in str(tuple(range(1, len(main_menu) + 1))):
      show_error(
          f'Некорректные данные, нужно ввести число (1-{len(main_menu)})')
      command = input('Введите номер действия: ')

    match command:
      case '1':
        add_contact()
      case '2':
        show_info()
      case '3':
        search_contact()
      case '4':
        transfer_contact()
      case '5':
        print(bcolors.OKGREEN + 'Good Luck!'+bcolors.ENDC, '👍')
