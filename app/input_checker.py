import re
from datetime import datetime


def nameInput(type_name='name'):
    while True:
        name = input(f'Enter contact {type_name}: ').lower()
        if check_name(name):
            return name
        print('You entered an empty string. Try again.')


def phoneInput(type_name='phone'):
    while True:
        phone = input(f'Enter {type_name}: ')
        if not phone:
            return []
        if len(phone.split()) > 3:
            print("Too much phone numbers (max 3)!")
            continue
        check_flag = True
        for data in phone.split():
            if not check_phone(data):
                print(
                    f'Phone number {data} must contain no more than 12 digits. Try again.')
                check_flag = False
        if check_flag:
            return phone.split()


def emailInput(type_email='email'):
    while True:
        email = input(f'Enter {type_email}: ')
        if check_email(email) or email == "":
            return email
        print('Wrong email format. Please enter correct email.')


def birthdayInput(type_birthday='birthday'):
    while True:
        birthday = input(f'Enter {type_birthday}: ')
        if check_birthday(birthday) or birthday == "":
            return birthday
        print('Wrong birthday format. Please enter birthday in format: DD.MM.YYYY')


def addressInput(address=None):
    while True:
        address = input(f'Enter address: ')
        if check_address(address) or address == "":
            return address
        print("You didn't enter an address.")


def daysnumberInput():
    number = input(f'Enter number of the days to birthday: ')
    if check_daysnumber(number):
        return int(number)
    print('Wrong format. Please enter number.')

# Notes functions
def titleInput(title_type='title'):
    while True:
        title = input(f'Enter {title_type}: ')
        if check_title(title):
            return title
        print("Wrong title format.")


def keywordsInput(kwords_type='keywords'):
    while True:
        keywords = input(f'Enter {kwords_type}(max 3) separated by space: ')
        if check_keywords(keywords):
            return keywords.split()
        print("Wrong keywords format.")


def notedataInput(notedata_type='note data'):
    while True:
        notedata = input(f'Enter {notedata_type}(max 120 chars): ')
        if check_notedata(notedata):
            return notedata
        print(
            "Wrong notedata format.\n\
                Data length must be between [1:120] characters!")


def tagsInput(tag='tag'):
    while True:
        tags = input(f"Enter {tag}: ")
        if bool(tags):
            return tags
        print("Wrong input!")


def categoryInput():
    while True:
        print("1: Title;\n2: Keywords;\n3: Note data;")
        category = input(
            f"Select the digit of the category that you want to sort by: ")
        if category in '123':
            return category
        print("Wrong digit!")

# input checkers
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
    return number.isdigit()


def check_phone(phone):
    return not bool([symbol for symbol in phone if not (symbol.isdigit() or symbol in ['+', '(', ')'])]) \
           and len(phone) < 19

# notes input check

def check_title(title):
    return bool(title)


def check_keywords(keywords):
    return 0 < len(keywords.split()) <= 3


def check_notedata(notedata):
    return 0 < len(notedata) <= 120
