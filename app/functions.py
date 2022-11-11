from Book import Book, ContactRecord
from Notes import Notes, NoteRecord
import difflib

handler = {
    'add_contact': Book.add_contact,
    'change_contact': Book.change_contact,
    'remove_contact': Book.remove_contact,
    'show_contact': Book.show_contact,
    'show_all_contacts': Book.show_all,
    'change_name': ContactRecord.change_name,
    'add_phone': ContactRecord.add_phone,
    'change_phone': ContactRecord.change_phone,
    'remove_phone': ContactRecord.remove_phone,
    'add_email': ContactRecord.add_email,
    'change_email': ContactRecord.change_email,
    'remove_email': ContactRecord.remove_email,
    'add_birthday': ContactRecord.add_birthday,
    'add_note': Notes.add_note,
    'change_note': Notes.change_note,
    'remove_note': Notes.remove_note,
    'show_note': Notes.show_note,
    'show_all_notes': Notes.show_all,
    'sort_notes': Notes.sort_notes,
    'show_notes_by': Notes.show_notes_by,
    'change_title': NoteRecord.change_title,
    'add_keyword': NoteRecord.add_keyword,
    'change_keyword': NoteRecord.change_keyword,
    'remove_keyword': NoteRecord.remove_keyword,
    'remove_all_keywords': NoteRecord.remove_all_keywords,
    'add_notedata': NoteRecord.add_notedata,
    'change_notedata': NoteRecord.change_notedata,
    'remove_notedata': NoteRecord.remove_notedata

}

def user_mistake(command):
    pos=difflib.get_close_matches(command, handler.keys(), n=3, cutoff=0.55)
    if pos:
        ph1="Looks like you make mistake."
        ph2="Type 'A'"
        ph3="Type 'B'"
        ph4="Type 'C'"
        ph5="if you mean"
        if len(pos)==3:
            new_input=input(f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\n{ph3} {ph5} '{pos[1]}'.\n{ph4} {ph5} '{pos[2]}'.\nEnter command:").lower()
            if new_input=="a":
                return pos[0]
            elif new_input=="b":
                return pos[1]
            elif new_input=="c":
                return pos[2]
            else:
                return
        if len(pos)==2:
            new_input=input(f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\n{ph3} {ph5} '{pos[1]}'.\nEnter command:").lower().strip()
            if new_input=="a":
                return pos[0]
            elif new_input=="b":
                return pos[1]
            else:
                return
        if len(pos)==1:
            new_input=input(f"{ph1}\n{ph2} {ph5} '{pos[0]}'.\nEnter command:").lower().strip()
            if new_input=="a":
                return pos[0]
            else:
                return
    else:
        return