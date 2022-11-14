from collections import UserDict
from input_checker import nameInput, phoneInput, emailInput, birthdayInput, addressInput, daysnumberInput
from datetime import datetime, timedelta
from console_output import show_in_console


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(nameInput('name'))
        if str(name) not in self.data:
            phones = Phones(phoneInput("phone numbers (max 3) separated by space"))
            email = Email(emailInput('email'))
            birthday = Birthday(birthdayInput('birthday'))
            address = Address(addressInput('address'))
            record = ContactRecord(name, phones, email, birthday, address)
            self.data[str(name)] = record
            return f'Contact {str(name)} was added to contacts!'
        return f'-!- Contact {str(name)} is already in contacts! -!-'

    def change_contact(self):
        name = Name(nameInput('name'))
        if str(name) in self.data:
            phones = Phones(phoneInput("new phone numbers (max 3) separated by space"))
            email = Email(emailInput('new email'))
            birthday = Birthday(birthdayInput('new birthday'))
            address = Address(addressInput('new address'))
            record = ContactRecord(name, phones, email, birthday, address)
            self.data[str(name)] = record
            return f'Contact {str(name)} was changed in contacts!'
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def remove_contact(self):
        name = Name(nameInput('name'))
        if str(name) in self.data:
            self.data.pop(str(name))
            return f'Contact {str(name)} was removed from contacts!'
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def show_contact(self):
        search_data = nameInput('search data')
        data = [[str(i.name), str(i.phones),
                 str(i.email), str(i.birthday), str(i.address)]
                for k, i in self.data.items() if
                search_data in str(i.name).lower()
                or search_data in str(i.phones).lower()
                or search_data in str(i.email).lower()
                or search_data in str(i.address).lower()]
        if data:
            headers = ['Name', 'Phones', 'Email', 'Birthday', 'Address']
            show_in_console(data, headers)
        else:
            return f"-!- No contacts with data {search_data} -!-"

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
        name = Name(nameInput('contacts name for which you want add phones'))
        if str(name) in self.data:
            len_phones = len(self.data[str(name)].phones)
            if len_phones < 3:
                phones = Phones(phoneInput(f'new phones numbers (max {3 - len_phones})'))
                if len(phones) <= 3 - len_phones:
                    self.data[str(name)].phones = self.data[str(name)].phones + phones.value
                    return f'New phones were added to contact {str(name)}'
                return f'You input more than {3 - len_phones}. Try again'
            return "-!- Too much phones in input! -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def change_phone(self):
        name = Name(nameInput('name'))
        if str(name) in self.data:
            old_phone = Phones(phoneInput('phone number which you want to change'))
            new_phone = Phones(phoneInput('new phone number'))
            record = self.data[str(name)]
            if old_phone.value[0] in record.phones.value:
                record.phones.value.insert(record.phones.value.index(old_phone.value[0]), new_phone.value[0])
                record.phones.value.remove(old_phone.value[0])
                return f'Phone {old_phone} was changed to {new_phone}!'
            return f"-!- Number {old_phone} doesn`t exist in contact '{name}' -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def remove_phone(self):
        name = Name(nameInput('name'))
        if str(name) in self.data:
            old_phone = Phones(phoneInput('phone number for remove'))
            record = self.data[str(name)]
            if old_phone.value[0] in record.phones.value:
                record.phones.value.remove(old_phone.value[0])
                return f'Phone {old_phone} was removed from contact {name}'
            return f"-!- Number {old_phone} doesn`t exist in contact '{name}' -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

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
        if self.data:
            days_number = daysnumberInput()
            check_day = datetime.now() + timedelta(days=days_number)
            data = [[str(i.name), str(i.phones),
                     str(i.email), str(i.birthday), str(i.address)]
                    for k, i in self.data.items() if i.birthday
                    and datetime.strptime(i.birthday.value, '%d.%m.%Y').day == check_day.day
                    and datetime.strptime(i.birthday.value, '%d.%m.%Y').month == check_day.month]
            if data:
                headers = ['Name', 'Phones', 'Email', 'Birthday', 'Address']
                show_in_console(data, headers)
            else:
                return f"-!- No contacts with birthday on {check_day.date()} -!-"
        return f"-!- Contacts data doesn`t exist -!-"

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


class Phones(ContactField):
    def __str__(self):
        return ', '.join(self.value) if self.value else "-"

    def __len__(self):
        return len(self.value)

    def __add__(self, other):
        return __class__(self.value + other)


class Email(ContactField):
    def __str__(self):
        return self.value if self.value else '-'


class Birthday(ContactField):
    def __str__(self):
        return self.value if self.value else '-'


class Address(ContactField):
    def __str__(self):
        return self.value if self.value else '-'
