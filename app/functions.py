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


def user_mistake(command):
    posssibilty = difflib.get_close_matches(
        command, handler.keys(), n=3, cutoff=0.55)
    if posssibilty:
        letters = ['1', '2', '3']
        print("-!- Looks like you make a mistake! -!-")
        for i in range(len(posssibilty)):
            print(f"Type '{letters[i]}' if you mean '{posssibilty[i]}'")
        new_user_input = input("Enter Digit: ").capitalize().strip()
        while new_user_input not in letters:
            new_user_input = input(
                "Enter One of the digits above to choose function: ").capitalize().strip()
        return posssibilty[letters.index(new_user_input)]


def start_func():
    global contacts
    global notes
    if os.path.exists(r"app\saved_data\contact_book.pickle") and \
            os.path.getsize(r"app\saved_data\contact_book.pickle"):
        with open(r"app\saved_data\contact_book.pickle", "rb") as file:
            contacts = Book()
            load_contacts = pickle.load(file)
            for key, value in load_contacts.items():
                contacts.data[key] = value
    else:
        contacts = Book()

    if os.path.exists(r"app\saved_data\notes.pickle") and \
            os.path.getsize(r"app\saved_data\notes.pickle") != 0:
        with open(r"app\saved_data\notes.pickle", "rb") as file:
            notes = Notes()
            load_notes = pickle.load(file)
            for key, value in load_notes.items():
                notes.data[key] = value
    else:
        notes = Notes()
    return contacts, notes


def exit_func():
    with open(r'app\saved_data\contact_book.pickle', 'wb') as file:
        pickle.dump(contacts.data, file)
    with open(r'app\saved_data\notes.pickle', 'wb') as file:
        pickle.dump(notes.data, file)
    print("See you next time! All contacts and notes were saved locally.")
    quit()


def show_commands():
    print("All commands:")
    keysList = list(handler.keys())
    contact_func = keysList[:16]
    notes_func = keysList[17:]
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
    with open('documentation.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print('\n\n\n')
        print(''.join(data))


def hello_func():
    print('Hello! How can I help you?')


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


contacts, notes = start_func()


handler = {
    'add_contact': contacts.add_contact,
    'change_contact': contacts.change_contact,
    'remove_contact': contacts.remove_contact,
    'show_contact': contacts.show_contact,
    'show_all_contacts': contacts.show_all,
    'change_name': contacts.change_name,
    'add_phone': contacts.add_phone,
    'change_phone': contacts.change_phone,
    'remove_phone': contacts.remove_phone,
    'add_email': contacts.add_email,
    'change_email': contacts.change_email,
    'remove_email': contacts.remove_email,
    'add_birthday': contacts.add_birthday,
    'show_birthdays_after': contacts.show_birthdays_after,
    'add_address': contacts.add_address,
    'change_address': contacts.change_address,
    'remove_address': contacts.remove_address,
    'add_note': notes.add_note,
    'change_note': notes.change_note,
    'remove_note': notes.remove_note,
    'show_note': notes.show_note,
    'show_all_notes': notes.show_all,
    'sort_notes_by': notes.sort_notes_by,
    'show_notes_with_tag': notes.show_notes_with_tag,
    'change_title': notes.change_title,
    'add_keywords': notes.add_keywords,
    'change_keywords': notes.change_keywords,
    'remove_keywords': notes.remove_keywords,
    'add_notedata': notes.add_notedata,
    'change_notedata': notes.change_notedata,
    'remove_notedata': notes.remove_notedata,
    'show_commands': show_commands,
    'filter_folder': filter_folder,
    'show_doc': show_doc
}
