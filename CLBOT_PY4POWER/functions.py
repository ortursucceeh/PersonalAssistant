import difflib
import shutil
import os
import pickle
from book import Book
from notes import Notes
from pathlib import Path
from constants import exit_words, hello_words
from console_output import show_in_console
from string import punctuation as punct
from constants import TRANS, EXTENSIONS, IGNORE_FOLDERS
from input_checker import *


current_directory = os.path.dirname(os.path.realpath(__file__))
saving_folder = os.path.join(current_directory, "saved_data")
document=os.path.join(os.path.dirname(current_directory),"PY4POWER_Logo_and_documentation","documentation.txt")

def hello_func():
    print('''Hello! I am your personal assistant CLBOT. How can I help you?
I can handle your contacts and notes. 
I can filter files by categories in any folder on your computer too. 
Would you like to look over my full documentation? Then enter the command "show_doc".''')


def start_func():
    global contacts
    global notes
    if os.path.exists(os.path.join(saving_folder, "contact_book.pickle")) and \
            os.path.getsize(os.path.join(saving_folder, "contact_book.pickle")):
        with open(os.path.join(saving_folder, "contact_book.pickle"), "rb") as file:
            contacts = Book()
            load_contacts = pickle.load(file)
            for key, value in load_contacts.items():
                contacts.data[key] = value
    else:
        contacts = Book()

    if os.path.exists(os.path.join(saving_folder, "notes.pickle")) and \
            os.path.getsize(os.path.join(saving_folder, "notes.pickle")) != 0:
        with open(os.path.join(saving_folder, "notes.pickle"), "rb") as file:
            notes = Notes()
            load_notes = pickle.load(file)
            for key, value in load_notes.items():
                notes.data[key] = value
    else:
        notes = Notes()
    return contacts, notes


contacts, notes = start_func()


def user_mistake(command):
    posssibilty = difflib.get_close_matches(
        command, handler.keys(), n=3, cutoff=0.55)
    if posssibilty:
        choices = ['1', '2', '3', '']
        print("-!- Looks like you made a mistake! -!-")
        for i in range(len(posssibilty)):
            print(f"\tEnter [{choices[i]}] if you mean '{posssibilty[i]}'")
        print("\tOr do not enter anything to skip.")
        new_input = input(">>> Enter digit: ").strip()
        while new_input not in choices:
            if not new_input:
                return None
            new_input = input(
                ">>> Enter one of the digits above to choose function: ").strip()
        try:
            return posssibilty[choices.index(new_input)]
        except IndexError:
            print('-!- Wrong digit! -!-')


def exit_func():
    if not os.path.exists(saving_folder):
        os.makedirs(saving_folder)
    with open(os.path.join(saving_folder, "contact_book.pickle"), 'wb') as file:
        pickle.dump(contacts.data, file)
    with open(os.path.join(saving_folder, "notes.pickle"), 'wb') as file:
        pickle.dump(notes.data, file)

    print('*' * 61)
    
    print(
        f"Yours contacts and notes were saved in such directory:\n{saving_folder}")
    print("See you next time!")
    print('*' * 61)
    quit()


def show_commands():
    """Func which shows all commands"""
    print("All commands:")
    keysList = list(handler.keys())
    contact_func = keysList[:16]
    notes_func = keysList[16:-3]
    other_commands = ["show_commands", "sort_folder",
                      "show_doc", "show_all_contacts", "show_all_notes", 'filter_folder']
    table_headers = ["Contacts Commands", "Notes Commands",
                     "Exit Commands", "Hello Comands", "Other Commands"]
    table = []
    n = 0
    for func in contact_func:
        try:
            table.append([func, notes_func[n], exit_words[n],
                         hello_words[n], other_commands[n]])
            n += 1
        except IndexError:
            try:
                table.append(
                    [func, notes_func[n], " ", " ", other_commands[n]])
                n += 1
            except IndexError:
                try:
                    table.append([func, notes_func[n]])
                    n += 1
                except IndexError:
                    table.append([func])
    show_in_console(table, table_headers, "psql")


def show_doc():
    with open(document, 'r', encoding='utf-8') as file:
        data = file.readlines()
        print('\n\n\n')
        print(''.join(data))

# func which return new_filename path


def normalize(main_path, file_name):
    name, ext = file_name.stem, file_name.suffix
    name = name.translate(TRANS)
    for ch in name:
        if ch in punct:
            name = name.replace(ch, "_")

    new_filename = f"{name}{ext}"
    return main_path.joinpath(new_filename)


def filter_folder():
    while True:
        main_path = Path(input('Enter an absolute way to folder: '))
        if not (os.path.exists(main_path) and Path(main_path).is_dir()):
            print('-!- Path incorrect! -!-')
        else:
            break
    # create an files iterator
    all_files = main_path.iterdir()

    for item in all_files:

        # rename file
        file = normalize(main_path, item)
        if not os.path.exists(file):
            os.rename(item, file)

        # find a key (which folder we will create) by suffix
        for key, value in EXTENSIONS.items():

            # check if our file is file
            if file.is_file:

                # find what type file is
                if file.suffix[1:].upper() in value:

                    # find a path where will be a new folder
                    new_folder_path = main_path.joinpath(key)

                    # if folder is not exist - create it
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    # create a new path where file will be after moving
                    file_newpath = new_folder_path.joinpath(
                        file.name)

                    # if archive - unpack him in the separate folder
                    if key == "archives":
                        extract_folder_path = new_folder_path.joinpath(
                            file.stem)

                        # if folder is not exist - create it
                        if not os.path.exists(extract_folder_path):
                            os.makedirs(extract_folder_path)

                        # unpack archive
                        shutil.unpack_archive(
                            file, extract_folder_path)

                    # move file
                    shutil.move(file, file_newpath)

            # check if file is folder which is not in IGRONE_FOLDERS
            if file.is_dir() and file.name not in IGNORE_FOLDERS:

                # if folder is empty - delete him
                if not os.listdir(file):
                    shutil.rmtree(file)

                # if not empty - recursively call our function again
                else:
                    filter_folder(file)
    return f'Folder {main_path.stem} was successfully filtered!'


handler = {
    'add_contact': (contacts.add_contact, (name_input, phones_input,
                                           email_input, birthday_input, address_input),
                    ('name', "phone numbers (max 3) separated by space", 'email',
                    'birthday', 'address')),
    'change_contact': (contacts.change_contact, (name_input, name_input, phones_input,
                                                 email_input, birthday_input, address_input),
                       ('contact`s name to change', 'new name', 'new phone numbers (max 3) separated by space',
                        'new email', 'new birthday', 'new address')),
    'remove_contact': (contacts.remove_contact, (name_input,), ('name',)),
    'show_contact': (contacts.show_contact, (name_input,), ('name',)),
    'show_all_contacts': (contacts.show_all,),
    'change_name': (contacts.change_name, (name_input, name_input),
                    ('name which you want to change', 'new name')),
    'add_phone': (contacts.add_phone, (name_input, phones_input),
                  ('contact`s name for which you want add phones', 'new phones numbers (max 3 in contact)')),
    'change_phone': (contacts.change_phone, (name_input, phones_input, phones_input),
                     ('name', 'phone number which you want to change', 'new phone number')),
    'remove_phone': (contacts.remove_phone, (name_input, phones_input),
                     ('name', 'phone number for remove')),
    'add_email': (contacts.add_email, (name_input, email_input),
                  ('the name for which you want to add email', 'the email to add')),
    'change_email': (contacts.change_email, (name_input, email_input),
                     ('the name for which you want to change email', 'the new email')),
    'remove_email': (contacts.remove_email, (name_input,),
                     ('the name for which you want to remove email',)),
    'add_birthday': (contacts.add_birthday, (name_input, birthday_input),
                     ('the name for which you want to add birthday', 'the birthday date to add')),
    'show_birthdays_after': (contacts.show_birthdays_after, (daysnumber_input,),
                             ('days to birthday')),
    'change_address': (contacts.change_address, (name_input, address_input),
                       ('the name for which you want to change address', 'the new address')),
    'remove_address': (contacts.remove_address, (name_input,),
                       ('the name for which you want to remove address',)),

    # notes handling
    'add_note': (notes.add_note, (title_input, keywords_input, notedata_input),
                 ('the title', 'the keywords (max 3)', 'the note data')),
    'change_note': (notes.change_note, (title_input, title_input, keywords_input, notedata_input),
                    ('the note title which you want to change',
                     'the new title', 'the new keywords', 'the new note data')),
    'remove_note': (notes.remove_note, (title_input,),
                    ('the note title which you want to remove',)),
    'show_note': (notes.show_note, (title_input,),
                  ('the title',)),
    'sort_notes_by': (notes.sort_notes_by, (category_input,),
                      ('the category',)),
    'show_notes_with_tag': (notes.show_notes_with_tag, (tag_input,),
                            ('the keyword',)),
    'change_title': (notes.change_title, (title_input, title_input),
                     ('the note title which you want to change', 'the new note title')),
    'add_keywords': (notes.add_keywords, (title_input, keywords_input),
                     ('the note title for which you want to add keywords', 'the keywords')),
    'change_keywords': (notes.change_keywords, (title_input, keywords_input),
                        ('the note title for which you want to change the keywords', 'the new keywords')),
    'remove_keywords': (notes.remove_keywords, (title_input,),
                        ('the note title for which you want to remove keywords', )),
    'add_notedata': (notes.add_notedata, (title_input, notedata_input),
                     ('the note title for which you want to add note data', 'the note data')),
    'change_notedata': (notes.change_notedata, (title_input, notedata_input),
                        ('the note title for which you want to change note data', 'the new note data')),
    'remove_notedata': (notes.remove_notedata, (title_input,),
                        ('the note title for which you want to remove note data',)),
    'show_all_notes': (notes.show_all,),
    'show_commands': (show_commands,),
    'filter_folder': (filter_folder,),
    'show_doc': (show_doc,)
}
