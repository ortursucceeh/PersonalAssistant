from collections import UserDict


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(input('Enter name: '))
        phone = Phone(input('Enter phone: '))
        email = Email(input('Enter email: '))
        birthday = Birthday(input('Enter birthday: '))
        try:
            record = ContactRecord(name, phone, email, birthday)
            self.data[name.value.lower()] = record
            return f'Contact {name.value().capitalize()} was added to contacts!'
        except:
            print("Try again?")
            vote = input(
                "Enter 'y' - to try again, 'n' - to choose another command\nYour choice -  ")
            if vote == 'y':
                self.add_contact()
            else:
                return "another"

    def change_contact(self):
        pass

    def remove_contact(self):
        pass

    def show_contact(self):
        pass

    def show_all(self):
        pass


class ContactRecord:

    def __init__(self, name, phone=None, email=None, birthday=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = [Phone(phone)] if phone else []

    # name handling
    def change_name(self):
        pass

# phone handling
    def add_phone(self):
        pass

    def change_phone(self):
        pass

    def remove_phone(self):
        pass

# email handling
    def add_email(self):
        pass

    def change_email(self):
        pass

    def remove_email(self):
        pass

# birthday handling
    def add_birthday(self):
        pass


class ContactField:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if isinstance(self, Name):
            self._check_name(new_value)
        elif isinstance(self, Phone):
            self._check_phone(new_value)
        elif isinstance(self, Birthday):
            self._check_birthday(new_value)
        elif isinstance(self, Email):
            self._check_email(new_value)

        self.__value = new_value

    def _check_name(self, value):
        pass

    def _check_phone(self, value):
        pass

    def _check_email(self, value):
        pass

    def _check_birthday(self, value):
        pass


class Name(ContactField):
    pass


class Phone(ContactField):
    pass


class Email(ContactField):
    pass


class Birthday(ContactField):
    pass


contactBook = ()
