import re


def NameInput(type_name='name'):
    while True:
        name = input(f'Enter {type_name}: ')
        if check_name(name):
            return name
        print('Wrong name')


def EmailInput(type_email='email'):
    while True:
        email = input(f'Enter {type_email}: ')
        if re.match(email).group():
            return email
        print('Wrong email format. ')


# return True\False
def check_name(name):
    return bool(name)
