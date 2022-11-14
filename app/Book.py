from collections import UserDict
from input_checker import nameInput, phoneInput, emailInput, birthdayInput, addressInput, daysnumberInput
from datetime import datetime, timedelta
from console_output import show_in_console


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(nameInput('name'))
        if str(name) in self.data:
            return f'-!- Contact {str(name)} is already in contacts! -!-'
        phones = Phone(phoneInput("phone numbers (max 3) separated by space"))
        email = Email(emailInput('email'))
        birthday = Birthday(birthdayInput('birthday'))
        address = Address(addressInput('address'))
        record = ContactRecord(name, phones, email, birthday, address)
        self.data[str(name)] = record
        return f'Contact {str(name)} was added to contacts!'

    def change_contact(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        phones = Phone(phoneInput(
            "new phone numbers (max 3) separated by space"))
        email = Email(emailInput('email'))
        birthday = Birthday(birthdayInput('birthday'))
        address = Address(addressInput('address'))
        record = ContactRecord(name, phones, email, birthday, address)
        self.data[str(name)] = record
        return f'Contact {str(name)} was changed in contacts!'

    def remove_contact(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        self.data.pop(str(name))
        return f'Contact {str(name)} was removed from contacts!'

    def show_contact(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        record = self.data[str(name)]
        data = [[str(record.name), str(record.phones),
                str(record.email), str(record.birthday), str(record.address)]]
        headers = ['Name', 'Phones', 'Email', 'Birthday', 'Address']
        show_in_console(data, headers, 'rounded_outline')

    def show_all(self):
        data = [[str(i.name), str(i.phones),
                str(i.email), str(i.birthday), str(i.address)]
                for i in self.data.values()]
        headers = ['Name', 'Phones', 'Email', 'Birthday', 'Address']
        show_in_console(data, headers, "mixed_grid")

    # name handling
    def change_name(self):
        name = Name(nameInput('name which you want to change'))
        if str(name) in self.data:
            new_name = Name(nameInput('new name'))
            old_record = self.data[str(name)]
            self.data[str(new_name)] = old_record
            old_record.name = new_name
            del self.data[str(name)]
            return f"Contact {str(name)} name was changed to new '{new_name}'!"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

# phone handling
    def add_phone(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        phone = Phone(phoneInput('new phone number'))
        self.data[str(name)].phones.value.append(phone.value[0])
        return f'Phone {str(phone)} was added to contact {str(name)}'

    def change_phone(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        old_phone = Phone(phoneInput('phone number which you want to change'))
        new_phone = Phone(phoneInput('new phone number'))
        record = self.data[str(name)]
        change_flag = False
        for i, phone in enumerate(record.phones.value):
            if phone == old_phone.value[0]:
                record.phones.value[i] = new_phone.value[0]
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was changed to {new_phone}!'
        else:
            return f"-!- Number {old_phone} doesn`t exist in contact '{name}'! -!-"

    def remove_phone(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'
        old_phone = Phone(phoneInput('phone for remove'))
        record = self.data[str(name)]
        change_flag = False
        for phone in record.phones.value:
            if phone == str(old_phone.value[0]):
                record.phones.value.remove(phone)
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was removed from contact {name}!'
        return f"-!- Number {old_phone} doesn`t exist in contact '{name}'! -!-"

# email handling
    def add_email(self):
        name = Name(nameInput('the name for which you want to add email'))
        if str(name) in self.data:
            if not self.data[str(name)].email:
                email = Email(emailInput('the email to add'))
                self.data[str(name)].email = email
                return f'Email "{email}" was added to the Contact "{name}"'
            return f'-!- Contact "{name}" already has the email! -!-\nYou can change it by entering command "change_email". '
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def change_email(self):  # <----------------------------------- ?
        name = Name(nameInput('the name for which you want to change email'))
        if str(name) in self.data:
            if self.data[str(name)].email:
                new_email = Email(emailInput('the new email'))
                old_email = self.data[str(name)].email
                self.data[str(name)].email = new_email
                return f'Email "{old_email}" was changed to "{new_email}"'
            return f'-!- Contact "{name}" has no email! -!-\nYou can add it by entering the command "add_email".'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def remove_email(self):
        name = Name(nameInput('the name for which you want to remove email'))
        if str(name) in self.data:
            if self.data[str(name)].email:
                self.data[str(name)].email = None
                return f'Email for the Contact "{name}" was removed'
            return f'-!- Contact "{name}" has no email! -!-'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

# birthday handling
    def add_birthday(self):
        name = Name(nameInput('the name for which you want to add birthday'))
        if str(name) in self.data:
            if not self.data[str(name)].birthday:
                birthday = Birthday(birthdayInput('the birthday date to add'))
                self.data[str(name)].birthday = birthday
                return f'Birthday "{birthday}" was added to the Contact "{name}"'
            return f'-!- Contact "{name}" already has the birhtday! -!-'
        return f'-!- Contact "{name}" does not exist! -!-'

# func to show the list of contact's with birthdays which are in 'N' days from today
    def show_birthdays_after(self):
        if not self.data:
            return f"-!- Contact's data doesn`t exist -!-"
        days_number = daysnumberInput()
        check_day = datetime.now() + timedelta(days=days_number)
        contacts_list = []
        for name, record in self.data.items():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y')
                if birthday.day == check_day.day and birthday.month == check_day.month:
                    contacts_list.append(name)
        if not contacts_list:
            return f"-!- No contacts with birthday on {check_day.date()} -!-"
        data = [[str(i.name), str(i.phones),
                 str(i.email), str(i.birthday), str(i.address)]
                for k, i in self.data.items() if k in contacts_list]
        headers = ['Name', 'Phones', 'Email', 'Birthday', 'Address']
        show_in_console(data, headers)

# address handling
    def add_address(self):
        name = Name(nameInput('the name for which you want to add address'))
        if str(name) in self.data:
            if not self.data[str(name)].address:
                address = Address(addressInput('the address to add'))
                self.data[str(name)].address = address
                return f'Address "{address}" was added to the Contact "{name}"'
            return f'-!- Contact "{name}" already has the address! -!-\nYou can change it by entering "change_address".'
        return f'-!- Contact "{name}" doesn`t exist -!-'

    def change_address(self):
        name = Name(nameInput('the name for which you want to change address'))
        if str(name) in self.data:
            if self.data[str(name)].address:
                new_address = Address(addressInput('the new address'))
                old_address = self.data[str(name)].address
                self.data[str(name)].address = new_address
                return f'Address "{old_address}" was changed to "{new_address}"!'
            return f'-!- Contact "{name}" has no address! -!-\nYou can add it by entering the command "add_address".'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def remove_address(self):
        name = Name(nameInput('the name for which you want to remove address'))
        if str(name) in self.data:
            if self.data[str(name)].address:
                self.data[str(name)].address = None
                return f'Address for the Contact "{name}" was removed!'
            return f'-!- Contact "{name}" has no address! -!-'
        return f'-!- Contact "{name}" doesn`t exist! -!-'


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
        return ', '.join(self.value) if self.value else "-"


class Email(ContactField):
    def __str__(self):
        return self.value if self.value else '-'


class Birthday(ContactField):
    def __str__(self):
        return self.value if self.value else '-'


class Address(ContactField):
    def __str__(self):
        return self.value if self.value else '-'
