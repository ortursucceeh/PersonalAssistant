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
        notedata = input(f'Enter {notedata_type}: ')
        if check_notedata(notedata):
            return notedata
        print("Wrong notedata format.")


def check_title(title):
    return bool(title)


def check_keywords(keywords):
    return 0 < len(keywords.split()) <= 3


def check_notedata(notedata):
    return 0 < len(notedata) <= 255
