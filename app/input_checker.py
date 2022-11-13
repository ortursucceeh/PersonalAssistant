import re


def name_input(type_name='name'):
    while True:
        name = input(f'Enter contact {type_name}: ').lower()
        if check_name(name):
            return name.capitalize()
        print('You entered an empty string. Try again.')


def phone_input(type_name='phone'):
    while True:
        phone = input(f'Enter {type_name} like "+38XXXXXXXXXX": ')
        if not phone:
            return []
        if len(phone.split()) > 3:
            print('Too much phone numbers, must be max 3')
            continue
        check_flag = True
        for data in phone.split():
            if not check_phone(data):
                print(f'Phone number {data} does not match "+38XXXXXXXXXX". Try again.')
                check_flag = False
        if check_flag:
            return phone.split()


def EmailInput(type_email='email'):
    while True:
        email = input(f'Enter {type_email}: ')
        if re.match(email).group():
            return email
        print('Wrong email format. ')


# return True\False
def check_name(name):
    return bool(name)


def check_phone(phone):
    return bool(re.findall(r'[+38]\d{12}', phone)) and len(phone) == 13


