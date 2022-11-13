from collections import UserDict
from input_checker import nameInput, emailInput, birthdayInput, addressInput
from datetime import datetime


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(nameInput('name'))
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
        name = Name(nameInput(name))
        email = Email(emailInput(email))
        self.data[str(name)].email = email
        return f'Email {str(email)} was added to the Contact "{str(name)}"'

    def change_email(self):# <----------------------------------- ?
        pass
        # name = Name(nameInput(name))
        # old_email = X
        # new_email = Y
        # record = self.data[str(name)]
        # if 
        #     return f'Email "{old_email}" was changed on "{new_email}" for "{str(name)}"'
        # else:
        #     return f'No such email "{old_email} for name "{str(name)}"'

    def remove_email(self):
        name = Name(nameInput(name))
        self.data[str(name)].email = None
        return f'Email for the Contact {str(name)} was delleted'

# birthday handling
    def add_birthday(self):
        name = Name(nameInput(name))
        birthday = Birthday(birthdayInput(birthday))
        self.data[str(name)].birthday = birthday
        return f'Birthday date {str(birthday)} was added to the Contact "{str(name)}"'

    def show_birthdays_after(self, N=7): # <----------------------------------- ?
        pass
        # today_day = datetime.now()
        # today_year = datetime.now().year
        # contacts_list = []
        # for name, record in self.data.items():
        #     for birthday in record:
        #         dif = today_day - self.birthday.value.replace(year=today_year)
        #         if dif >= 0:
        #             days_number = dif.days
        #         else:
        #             dif = self.birthday.value.replace(year=today_year+1) - today_day
        #             days_number = dif.days
        #         if days_number == N:
        #             contacts_list.append(f'{str(name)}: {str(birthday)}\n')
        #     if contacts_list():
        #     return f'Contacts for {N} days from today are: \n{contacts_list}'
        # else:
        #     return f'No Contacts with birthday in {N} days befor today'


# address handling

    def add_address(self):
        name = Name(nameInput(name))
        address = Address(addressInput(address))
        self.data[str(name)].address = address
        return f'Address {str(address)} was added to the Contact "{str(name)}"'

    def change_address(self):# <----------------------------------- ?
        pass
        # name = Name(nameInput(name))
        # old_address = X
        # new_address = Y
        # record = self.data[str(name)]
        # if 
        #     return f'Address "{old_address}" was changed on "{new_adderessl}" for "{str(name)}"'
        # else:
        #     return f'No such email "{old_address} for name "{str(name)}"'

    def remove_address(self):
        name = Name(nameInput(name))
        self.data[str(name)].address = None
        return f'Address for the Contact {str(name)} was delleted'


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
   def __str__(self):
        return self.value


class Email(ContactField):
    def __str__(self):
        return self.value


class Birthday(ContactField):
    def __str__(self):
        return self.value


class Address(ContactField):
    def __str__(self):
        return self.value
