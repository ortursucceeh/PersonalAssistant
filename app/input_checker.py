import re
from datetime import datetime


def nameInput(type_name='name'):
    while True:
        name = input(f'Enter {type_name}: ')
        if check_name(name):
            return name
        print('Wrong name')


def emailInput(type_email='email'):
    while True:
        email = input(f'Enter {type_email}: ')
        if check_email(email):
            return email
        print('Wrong email format.')


def birhtdayInput(birthday):
    while True:
        birthday = input(f'Enter birthady: ')
        if check_birthday(birthday):
            return birthday
        print('Wrong birhtday format.')


def addressInput(address=None):
    address = input(f'Enter address: ')
    return address


# return True\False
def check_name(name):
    return bool(name)


def check_email(email):
    if re.fullmatch(r'[a-zA-Z]+[a-zA-Z0-9_.]+@[a-zA-Z]+[.][a-zA-Z]{2,}', email):
        return email
    else:
        raise Exception(f'Please enter correct e-mail address')


def check_birthday(birthday):
    try:
        birthday = datetime.strptime(birthday, '%d-%m-%Y')
    except:
        raise Exception(f'Please enter birthday in format: DD-MM-YYYY')
