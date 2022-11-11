from collections import UserDict
from input_checker import NameInput


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(NameInput('name'))
        phones = None
        email = None
        record = ContactRecord(name, phones, email)
        self.data[str(name)] = record
        return f'Contact {str(name)}'

    def change_contact(self):
        pass

    def remove_contact(self):
        pass

    def show_contact(self):
        pass

    def show_all(self):
        pass

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
        name = self.NameInput()
        self.data[name].email = None

# birthday handling
    def add_birthday(self):
        pass

    def show_birthdays_after(self):
        pass

# address handling

    def add_address(self):
        pass

    def change_address(self):
        pass

    def remove_address(self):
        pass


class ContactRecord:

    def __init__(self, name, phone=None, email=None, birthday=None, address=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = [Phone(phone)] if phone else []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None


class ContactField:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


# Прописати __str__
class Name(ContactField):
    def __str__(self):
        return self.value


class Phone(ContactField):
    pass


class Email(ContactField):
    pass


class Birthday(ContactField):
    pass


class Address(ContactField):
    pass
