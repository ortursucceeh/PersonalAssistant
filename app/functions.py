import difflib
import os
import pickle
from Book import Book, ContactRecord, Name
from Notes import Notes, NoteRecord
from prettytable import PrettyTable
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
    posssibilty = difflib.get_close_matches(command, handler.keys(), n=3, cutoff=0.55)
    if posssibilty:
        letters=['A','B','C']
        print("Looks like you make a mistake.")
        for i in range(len(posssibilty)):
            print(f"Type '{letters[i]}' if you mean '{posssibilty[i]}'")
        new_user_input=input("Enter Letter:")
        input_update=new_user_input.capitalize().strip()
        if input_update in letters:
            return posssibilty[letters.index(input_update)]
        else:
            return
def start_func():
    w_t1="Welcome dear User. "
    w_t2="Our small application works with your contact list and notes. " 
    w_t3="Type one of below self-explanatory command to start work with it."
    table1 = PrettyTable()
    table1.field_names=[w_t1+w_t2+w_t3]
    table1.align = "r"
    keysList = list(handler.keys())
    keysList+=exit_words+hello_words
    table=PrettyTable()
    field_names = ["1","2","3","4","5","6"]
    y=0
    for i in field_names:
        table.add_column(i,keysList[y:y+6])
        y+=6
    print(table1)
    print(table)
    if os.path.exists("contact_book.pickle") and \
            os.path.getsize("contact_book.pickle")!=0:
        with open("contact_book.pickle","rb") as file:
            contacts = pickle.load(file)
    else:
        contacts = Book()
    if os.path.exists("notes.pickle") and \
            os.path.getsize("notes.pickle")!=0:
        with open("notes.pickle","rb") as file:
            contacts = pickle.load(file)
    else:
        notes = Notes()
    return contacts,notes

def exit_func():
    print('exit')
    quit()


def hello_func():
    print('Hello! How can I help you?')
