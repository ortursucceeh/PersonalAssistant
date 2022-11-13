import re
from datetime import datetime


def nameInput(type_name='name'):
    while True:
        name = input(f'Enter {type_name}: ')
        if check_name(name):
            return name
        print('Wrong name!')


def emailInput(type_email='email'):
    while True:
        email = input(f'Enter {type_email}: ')
        if check_email(email):
            return email
        print('Wrong email format. Please enter correct e-mail.')


def birthdayInput(type_birthday='birthday'):
    while True:
        birthday = input(f'Enter {type_birthday}: ')
        if check_birthday(birthday):
            return birthday
        print('Wrong birhtday format. Please enter birthday in format: DD.MM.YYYY')


def addressInput(address=None):
    while True:
        address = input(f'Enter address: ')
        if check_address(address):
            return address
        print("You didn't enter an address.")


def daysnumberInput(type_number='number'):
    number = input(f'Enter number of the days before birthady: ')
    if check_daysnumber(number):
        return number
    print('Wrong format. Please enter number.')


# return True\False
def check_name(name):
    return bool(name)


def check_address(address):
    return bool(address)


def check_email(email):
    if re.fullmatch(r'[a-zA-Z]+[a-zA-Z0-9_.]+@[a-zA-Z]+[.][a-zA-Z]{2,}', email):
        return email


def check_birthday(birthday):
    try:
        birthday = datetime.strptime(birthday, '%d.%m.%Y')
        return True
    except:
        return False


def check_daysnumber(number):
    if number.isdigit(): 
        return int(number)