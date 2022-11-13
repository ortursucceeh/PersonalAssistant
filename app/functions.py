import difflib
import os
import pickle
from Book import Book
from Notes import Notes
from constants import exit_words,hello_words
from tabulate import tabulate

contacts = Book()
notes = Notes()

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
    'add_keyword': notes.add_keywords,
    'change_keyword': notes.change_keywords,
    'remove_keyword': notes.remove_keywords,
    'add_notedata': notes.add_notedata,
    'change_notedata': notes.change_notedata,
    'remove_notedata': notes.remove_notedata

}

def user_mistake(command):
    posssibilty = difflib.get_close_matches(command, handler.keys(), n=3, cutoff=0.55)
    if posssibilty:
        letters=['1','2','3']
        print("Looks like you make a mistake.")
        for i in range(len(posssibilty)):
            print(f"Type '{letters[i]}' if you mean '{posssibilty[i]}'")
        new_user_input=input("Enter Digit: ").capitalize().strip()
        while new_user_input not in letters:
            new_user_input=input("Enter One of the Digits Above to Choose Function: ").capitalize().strip()
        return posssibilty[letters.index(new_user_input)]

def show_commands():
    keysList=list(handler.keys())
    contact_func=keysList[0:16]
    notes_func=keysList[17:]
    other_commands=["show_commands", "sort_folder", "show_doc","show_all_contacts","show_all_notes"]
    table_headers=["Contacts Commands","Notes Commands","Hello Comands","Exit Commands","Other Commands"]
    table=[]
    n=0
    for i in contact_func:
        try:
            table.append([i,notes_func[n],exit_words[n],hello_words[n],other_commands[n]])
            n+=1
        except IndexError:
            try:
                table.append([i,notes_func[n]," "," ",other_commands[n]])
                n+=1
            except IndexError:
                try:
                    table.append([i,notes_func[n]])
                    n+=1
                except IndexError:
                    table.append([i])
    print(tabulate(table,headers=table_headers,tablefmt="psql",numalign="center"))

def start_func():
   print('start')
   quit()

def exit_func():
    print('exit')
    quit()


def hello_func():
    print('Hello! How can I help you?')
