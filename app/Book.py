from collections import UserDict
from input_checker import nameInput, emailInput, birthdayInput, addressInput, daysnumberInput
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
        name = Name(nameInput('the name for which you want to add email'))
        if str(name) in self.data:
            if not self.data[str(name)].email:
                email = Email(emailInput('the email to add'))
                self.data[str(name)].email = email
                return f'Email "{email}" was added to the Contact "{name}"'
            return f'Contact "{name}" already has the email! You can change it by entering command "change_email".'
        return f'Contact "{name}" does not exist!'

    def change_email(self):# <----------------------------------- ?
        name = Name(nameInput('the name for which you want to change email'))
        if str(name) in self.data:
            if self.data[str(name)].email:
                new_email = Email(emailInput('the new email'))
                old_email = self.data[str(name)].email
                self.data[str(name)].email = new_email
                return f'Email "{old_email}" was changed to "{new_email}"'
            return f'Contact "{name}" has no email! You can add it by entering the command "add_email".'
        return f'Contact "{name}" does not exist!'

    def remove_email(self):
        name = Name(nameInput('the name for which you want to remove email'))
        if str(name) in self.data:
            if self.data[str(name)].email:
                self.data[str(name)].email = None
                return f'Email for the Contact "{name}" was removed'
            return f'Contact "{name}" has no email!'
        return f'Contact "{name}" does not exist!'

# birthday handling
    def add_birthday(self):
        name = Name(nameInput('the name for which you want to add birthday'))
        if str(name) in self.data:
            if not self.data[str(name)].birthday:
                birthday = Birthday(birthdayInput('the birthday date to add'))
                self.data[str(name)].birthday = birthday
                return f'Birthday "{birthday}" was added to the Contact "{name}"'
            return f'Contact "{name}" already has the birhtday!'
        return f'Contact "{name}" does not exist!'

# func to calculate days number from today to the birtday
    def days_to_bd(self):# <-------------------------------------------------------NOT finished
        today_day = datetime.now()
        today_year = datetime.now().year
        dif = today_day - self.birthday.value.replace(year=today_year)
        if dif >= 0:
            days_number = dif.days
        else:
            dif = self.birthday.value.replace(year=today_year+1) - today_day
            days_number = dif.days
        return days_number

# func to show the list of birthdays which are in 'N' days from today
    def show_birthdays_after(self): # <-------------------------------------------NOT finished
        days_number = daysnumberInput('days number to birthady')
        contacts_list = []
        for name, record in self.data.items():
            if record.birthday:
                if days_number == days_to_bd(record.birthday):
                    contacts_list.append(record)
        if contacts_list:
            return f'Contacts in {days_number} days from today are: \n{contacts_list}'
        else:
            return f'No contacts with birthday after {days_number} days from today'

# address handling
    def add_address(self):
        name = Name(nameInput('the name for which you want to add address'))
        if str(name) in self.data:
            if not self.data[str(name)].address:
                address = Address(addressInput('the address to add'))
                self.data[str(name)].address = address
                return f'Address "{address}" was added to the Contact "{name}"'
            return f'Contact "{name}" already has the address. To change it enter the command "change_address".'
        return f'Contact "{name}" does not exist'

    def change_address(self):
        name = Name(nameInput('the name for which you want to change address'))
        if str(name) in self.data:
            if self.data[str(name)].address:
                new_address = Address(addressInput('the new address'))
                old_address = self.data[str(name)].address
                self.data[str(name)].address = new_address
                return f'Address "{old_address}" was changed to "{new_address}"'
            return f'Contact "{name}" has no address! You can add it by entering the command "add_address".'
        return f'Contact "{name}" does not exist!'

    def remove_address(self):
        name = Name(nameInput('the name for which you want to remove address'))
        if str(name) in self.data:
            if self.data[str(name)].address:
                self.data[str(name)].address = None
                return f'Address for the Contact "{name}" was removed'
            return f'Contact "{name}" has no address!'
        return f'Contact "{name}" does not exist!'


class ContactRecord:

    def __init__(self, name, phone=None, email=None, birthday=None, address=None):
        self.name = name
        self.birthday = birthday if birthday else None
        self.phones = phone if phone else []
        self.email = email if email else None
        self.address = address if address else None


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
        return self.value.capitalize()


class Phone(ContactField):
   def __str__(self):
        return ', '.join(self.value)


class Email(ContactField):
    def __str__(self):
        return self.value


class Birthday(ContactField):
    def __str__(self):
        return self.value


class Address(ContactField):
    def __str__(self):
        return self.value
