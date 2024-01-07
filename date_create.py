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
