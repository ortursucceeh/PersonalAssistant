from collections import UserDict
from input_checker import titleInput, keywordsInput, notedataInput, tagsInput, categoryInput
from console_output import show_in_console


class Notes(UserDict):

    # note handling
    def add_note(self):
        title = Title(titleInput())
        if str(title) not in self.data:
            keywords = Keywords(keywordsInput())
            notedata = Notedata(notedataInput())
            record = NoteRecord(title, keywords, notedata)
            self.data[str(title)] = record
            return f"Note '{title}' with keywords '{str(keywords)}' was added!"
        return f"-!- Note with title '{title}' is already in Notes -!-"

    def change_note(self):
        title = Title(titleInput('note title which you want to change'))
        if str(title) in self.data:
            new_title = Title(titleInput('new title'))
            new_keywords = Keywords(keywordsInput('new keywords'))
            new_notedata = Notedata(notedataInput('new note data'))
            new_record = NoteRecord(new_title, new_keywords, new_notedata)
            del self.data[str(title)]
            self.data[str(new_title)] = new_record
            return f"Note '{title}' was changed to new note with title '{new_title}'!"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def remove_note(self):
        title = Title(titleInput('note title which you want to remove'))
        if str(title) in self.data:
            del self.data[str(title)]
            return f"Note '{title}' was removed!"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    #output in console
    def show_note(self):
        title = Title(titleInput())
        if str(title) not in self.data:
            return f"-!- Note with title '{title}' doesn't exist! -!-"
        header = ['Title', 'Keywords', 'Data']
        data = [[self.data[str(title)].title,
                self.data[str(title)].keywords,
                self.data[str(title)].notedata]]
        show_in_console(data, header)

    def show_all(self):

        data = [[str(i.title), str(i.keywords), str(i.notedata)]
                for i in self.data.values()]
        header = ['Title', 'Keywords', 'Data']
        show_in_console(data, header)

    def show_notes_with_tag(self):
        data = []
        header = ['Title', 'Keywords', 'Data']
        tag = tagsInput()
        for record in self.data.values():
            if tag in str(record.keywords):
                data.append([
                    str(record.title),
                    str(record.keywords),
                    str(record.notedata)])
        show_in_console(data, header)

    # sort_func
    def sort_notes_by(self):
        category = categoryInput()
        if category == '1':
            def key(x): return str(x[1].title)
        elif category == '2':
            def key(x): return str(x[1].keywords)
        else:
            def key(x): return str(x[1].notedata)
        self.data = dict(sorted(self.data.items(), key=key))
        return "Notes were sorted!"

        # title handling

    def change_title(self):
        title = Title(titleInput('note title which you want to change'))
        if str(title) in self.data:
            new_title = Title(titleInput('new note title'))
            old_record = self.data[str(title)]
            old_record.title = new_title
            self.data[str(new_title)] = old_record
            del self.data[str(title)]
            return f"Note title '{title}' was changed to new '{new_title}'!"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    # keywords handling
    def add_keywords(self):
        title = Title(titleInput(
            'note title for which you want to add keywords'))
        if str(title) in self.data:
            len_kwords = len(self.data[str(title)].keywords)
            if len_kwords < 3:
                keywords = keywordsInput(f'new keywords(max {3 - len_kwords})')
                if len(keywords) > 3 - len_kwords:
                    return 'Too much keywords!'
                self.data[str(title)].keywords = self.data[str(
                    title)].keywords + keywords
                return f"New keywords {keywords} were added to {title}!"
            return f'-!- Note {title} already has maximum count of keywords! -!-'
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def change_keywords(self):
        title = Title(titleInput(
            'note title for which you want to change keywords'))
        if str(title) in self.data:
            len_kwords = len(self.data[str(title)].keywords)
            if len_kwords < 3:
                new_keywords = keywordsInput(f'new keywords(max 3)')
                if len(new_keywords) > 3:
                    return 'Too much keywords!'
                self.data[str(title)].keywords = new_keywords
            return f"Note {title} keywards was changed to {str(new_keywords)}"
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def remove_keywords(self):
        title = Title(titleInput(
            'note title for which you want to remove keywords'))
        if str(title) in self.data:
            self.data[str(title)].value = []

    # notedata handling
    def add_notedata(self):
        title = Title(titleInput(
            'note title for which you want to add note data'))
        if str(title) in self.data:
            if not self.data[str(title)].notedata:
                new_notedata = notedataInput('note data')
                self.data[str(title)].notedata = new_notedata
                return f"Note data was added to note '{title}'!"
            return f"-!- Note {title} has note data! -!-\nYou can change it by entering change_notedata."
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def change_notedata(self):
        title = Title(titleInput(
            'note title for which you want to change note data'))
        if str(title) in self.data:
            if self.data[str(title)].notedata:
                new_notedata = notedataInput('new note data')
                self.data[str(title)].notedata = new_notedata
                return f"Note data was changed!"
            return f"-!- Note {title} has no note data! -!-\nYou can add it by entering add_notedata."
        return f"-!- Note with title '{title}' doesn't exist! -!-"

    def remove_notedata(self):
        title = Title(titleInput(
            'note title for which you want to change note data'))
        if str(title) in self.data:
            if self.data[str(title)].notedata:
                self.data[str(title)].notedata = None
                return f"Note data was removed!"
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
