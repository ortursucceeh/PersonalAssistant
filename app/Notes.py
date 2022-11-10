class Notes:

    def add_note(self):
        pass

    def change_note(self):
        pass

    def remove_note(self):
        pass

    def find_note(self):
        pass

    def show_all(self):
        pass

    def sort_notes(self):
        pass

    def show_notes_by(self):
        pass


class NoteRecord:

    # title handling
    def change_title(self):
        pass

    # keywords handling
    def add_keyword(self):
        pass

    def change_keyword(self):
        pass

    def remove_keyword(self):
        pass

    def remove_all_keywords(self):
        pass

    # notedata handling
    def add_notedata(self):
        pass

    def change_notedata(self):
        pass

    def remove_notedata(self):
        pass


class NoteField:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if isinstance(self, Title):
            self._check_title(new_value)
        elif isinstance(self, Keywords):
            self._check_keyword(new_value)
        elif isinstance(self, Notedata):
            self._check_notedata(new_value)

        self.__value = new_value

    def _check_title(self, value):
        pass

    def _check_keyword(self, value):
        pass

    def _check_notedata(self, value):
        pass


class Title(NoteField):
    pass


class Keywords(NoteField):
    pass


class Notedata(NoteField):
    pass
