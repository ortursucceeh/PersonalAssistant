from collections import UserDict
from console_output import show_in_console


class Notes(UserDict):

    # note handling
    def add_note(self, title, keywords, notedata):
        title = Title(title)
        if str(title) not in self.data:
            record = NoteRecord(title,
                                Keywords(keywords),
                                Notedata(notedata))
            self.data[str(title)] = record
            return f"[+] Note '{title}' with keywords '{keywords}' was added!"
        return f"-!- Note with title '{title}' is already in Notes -!-"

    def change_note(self, old_title, new_title, new_keywords, new_notedata):
        old_title = Title(old_title)
        if str(old_title) in self.data:
            new_record = NoteRecord(
                Title(new_title), Keywords(new_keywords), Notedata(new_notedata))
            del self.data[str(old_title)]
            self.data[str(new_title)] = new_record
            return f"[+] Note '{old_title}' was changed to new note with title '{new_title}'!"
        return f"-!- Note with title '{old_title}' doesn't exist! -!-"

    def remove_note(self, title):
        title = Title(title)
        if str(title) in self.data:
            del self.data[str(title)]
            return f"[+] Note '{title}' was removed!"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    #output in console
    def show_note(self, title):
        title = Title(title)
        if str(title) not in self.data:
            return f"-!- Note with title '{title}' doesn't exist! -!-"
        header = ('Title', 'Keywords', 'Data')
        data = ((self.data[str(title)].title,
                self.data[str(title)].keywords,
                self.data[str(title)].notedata),)
        show_in_console(data, header)

    def show_all(self):
        data = [[str(i.title), str(i.keywords), str(i.notedata)]
                for i in self.data.values()]
        header = ('Title', 'Keywords', 'Data')
        show_in_console(data, header)

    def show_notes_with_tag(self, tag):
        data = [[str(rec.title), str(rec.keywords), str(rec.notedata)]
                for rec in self.data.values()
                if tag in str(rec.keywords)]
        header = ('Title', 'Keywords', 'Data')
        if data:
            show_in_console(data, header)
        else:
            return f'You have no notes with tag "{tag}"'

    # sort_func
    def sort_notes_by(self, category):
        if category == '1':
            def key(x): return str(x[1].title)
        elif category == '2':
            def key(x): return str(x[1].keywords)
        else:
            def key(x): return str(x[1].notedata)
        self.data = dict(sorted(self.data.items(), key=key))
        return "[+] Notes were sorted!"

    # title handling
    def change_title(self, old_title, new_title):
        old_title = Title(old_title)
        new_title = Title(new_title)
        if str(old_title) in self.data:
            old_record = self.data[str(old_title)]
            old_record.title = new_title
            self.data[str(new_title)] = old_record
            del self.data[str(old_title)]
            return f"[+] Note title '{old_title}' was changed to new '{new_title}'!"
        return f"-!- Note with title '{old_title}' doesn't exist! -!-"

    # keywords handling
    def add_keywords(self, title, keywords):
        title = Title(title)
        if str(title) in self.data:
            len_kwords = len(self.data[str(title)].keywords)
            if len_kwords < 3:
                if len(keywords) > 3 - len_kwords:
                    return '-!- Too much keywords! -!-'
                self.data[str(title)].keywords = self.data[str(
                    title)].keywords + keywords
                return f"[+] New keywords {keywords} were added to {title}!"
            return f'-!- Note {title} already has maximum count of keywords! -!-'
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def change_keywords(self, title, new_keywords):
        title = Title(title)
        if str(title) in self.data:
            if len(new_keywords) > 3:
                return '-!- Too much keywords! -!-'
            self.data[str(title)].keywords = Keywords(new_keywords)
            return f"[+] Note {title} keywords was changed to {str(new_keywords)}"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def remove_keywords(self, title):
        title = Title(title)
        if str(title) in self.data:
            self.data[str(title)].keywords = Keywords([])
            return '[+] Keywords were removed!'
        return f'You have do not have note with this title'

    # notedata handling
    def add_notedata(self, title, new_notedata):
        title = Title(title)
        if str(title) in self.data:
            if not self.data[str(title)].notedata:
                self.data[str(title)].notedata = Notedata(new_notedata)
                return f"[+] Note data was added to note '{title}'!"
            return f"-!- Note {title} has note data! -!-\nYou can change it by entering change_notedata."
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def change_notedata(self, title, new_notedata):
        title = Title(title)
        if str(title) in self.data:
            if self.data[str(title)].notedata:
                self.data[str(title)].notedata = Notedata(new_notedata)
                return f"[+] Note data was changed!"
            return f"-!- Note {title} has no note data! -!-\nYou can add it by entering add_notedata."
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def remove_notedata(self, title):
        title = Title(title)
        if str(title) in self.data:
            if self.data[str(title)].notedata:
                self.data[str(title)].notedata = Notedata(None)
                return f"[+] Note data was removed!"
            return f"-!- Note {title} has no note data. -!-"
        return f"-!- Note with title '{title}' doesn't exist! -!-"


class NoteRecord:
    def __init__(self, title, keywords=None, notedata=None):
        self.title = title
        self.keywords = keywords if keywords else None
        self.notedata = notedata if notedata else None


class NoteField:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Title(NoteField):
    def __str__(self):
        return self.value.capitalize()


class Keywords(NoteField):
    def __str__(self):
        return ', '.join(self.value) if self.value else '-'

    def __add__(self, other: list):
        return __class__(self.value + other)

    def __len__(self):
        return len(self.value)


class Notedata(NoteField):
    def __str__(self):
        return self.value if self.value else '-'
