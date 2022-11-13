import difflib
import os
import pickle
from Book import Book, ContactRecord, Name
from Notes import Notes, NoteRecord

contacts = Book()
notes = Notes()

handler = {
    'add_contact': contacts.add_contact,
    'change_contact': contacts.change_contact,
    'remove_contact': contacts.remove_contact,
    'show_contact': contacts.show_contact,
    'show_all_contacts': contacts.show_all,
    # 'change_name': contacts.change_name,
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
    'sort_notes': notes.sort_notes,
    'show_notes_by': notes.show_notes_by,
    'change_title': notes.change_title,
    'add_keyword': notes.add_keyword,
    'change_keyword': notes.change_keyword,
    'remove_keyword': notes.remove_keyword,
    'remove_all_keywords': notes.remove_all_keywords,
    'add_notedata': notes.add_notedata,
    'change_notedata': notes.change_notedata,
    'remove_notedata': notes.remove_notedata

}


def user_mistake(command):
    pos = difflib.get_close_matches(command, handler.keys(), n=3, cutoff=0.55)
    if pos:
        ph1 = "Looks like you make mistake."
        ph2 = "Type 'A'"
        ph3 = "Type 'B'"
        ph4 = "Type 'C'"
        ph5 = "if you mean"
        if len(pos) == 3:
            new_input = input(
                f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\n{ph3} {ph5} '{pos[1]}'.\n{ph4} {ph5} '{pos[2]}'.\nEnter command:").lower()
            if new_input == "a":
                return pos[0]
            elif new_input == "b":
                return pos[1]
            elif new_input == "c":
                return pos[2]
            else:
                return
        if len(pos) == 2:
            new_input = input(
                f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\n{ph3} {ph5} '{pos[1]}'.\nEnter command:").lower().strip()
            if new_input == "a":
                return pos[0]
            elif new_input == "b":
                return pos[1]
            else:
                return
        if len(pos) == 1:
            new_input = input(
                f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\nEnter command:").lower().strip()
            if new_input == "a":
                return pos[0]
            else:
                return
    else:
        return


def exit_func():
    print('exit')
    quit()


def hello_func():
    print('Hello! How can I help you?')
