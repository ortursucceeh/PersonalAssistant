from Book import Book, ContactRecord
from Notes import Notes, NoteRecord


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
