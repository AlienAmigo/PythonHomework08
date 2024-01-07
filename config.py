class config:
  DATA_FILE = 'phonebook.txt'


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


main_menu = [
    'Добавить контакт ➕',
    'Вывести на экран 📋',
    'Поиск контакта 🔎',
    'Перенос контакта 📩',
    'Выход из программы 🚪'
]

search_menu = [
    'По фамилии',
    'По имени',
    'По отчеству',
    'По номеру',
    'По адресу'
]


def show_title(title: str):
  print(f'\n{bcolors.WARNING}{title}{bcolors.ENDC}')


def show_error(text: str):
  print(f'⚠️  {bcolors.FAIL}{text}{bcolors.ENDC}')
