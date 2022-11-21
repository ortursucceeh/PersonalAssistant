from collections import UserDict
from datetime import datetime, timedelta
from console_output import show_in_console


class Book(UserDict):

    # work with contact
    def add_contact(self, name, phones, email, birthday, address):
        name = Name(name)
        if str(name) not in self.data:
            record = ContactRecord(name, Phones(phones), Email(email),
                                   Birthday(birthday), Address(address))
            self.data[str(name)] = record
            return f'[+] Contact {str(name)} was added to contacts!'
        return f'-!- Contact {str(name)} is already in contacts! -!-'

    def change_contact(self, old_name, new_name, phones, email, birthday, address):
        name = Name(old_name)
        if str(name) in self.data:
            record = ContactRecord(Name(new_name), Phones(phones), Email(
                email), Birthday(birthday), Address(address))
            self.data[str(name)] = record
            return f'[+] Contact {str(name)} was changed!'
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def remove_contact(self, name):
        name = Name(name)
        if str(name) in self.data:
            del self.data[str(name)]
            return f'[+] Contact {str(name)} was removed from contacts!'
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def show_contact(self, search_data):
        data = [[str(i.name), str(i.phones),
                 str(i.email), str(i.birthday), str(i.address)]
                for k, i in self.data.items() if
                search_data in str(i.name).lower()
                or search_data in str(i.phones).lower()
                or search_data in str(i.email).lower()
                or search_data in str(i.address).lower()]
        if data:
            headers = ('Name', 'Phones', 'Email', 'Birthday', 'Address')
            show_in_console(data, headers, 'rounded_outline')
        else:
            return f"-!- No contacts with data {search_data} -!-"

    def show_all(self):
        data = [[str(i.name), str(i.phones),
                str(i.email), str(i.birthday), str(i.address)]
                for i in self.data.values()]
        headers = ('Name', 'Phones', 'Email', 'Birthday', 'Address')
        show_in_console(data, headers, "mixed_grid")

    # name handling
    def change_name(self, old_name, new_name):
        old_name = Name(old_name)
        new_name = Name(new_name)
        if str(old_name) in self.data:
            old_record = self.data[str(old_name)]
            old_record.name = new_name
            self.data[str(new_name)] = old_record
            del self.data[str(old_name)]
            return f"[+] Contact {str(old_name)} name was changed to new '{new_name}'!"
        return f'-!- Contact {str(old_name)} doesn`t exist in contacts! -!-'

    # phone handling
    def add_phone(self, name, phones):
        name = Name(name)
        if str(name) in self.data:
            len_phones = len(self.data[str(name)].phones)
            if len_phones < 3:
                if len(phones) <= 3 - len_phones:
                    self.data[str(name)].phones = self.data[str(
                        name)].phones + phones
                    return f'[+] New phones were added to contact {str(name)}'
                return f'You entered too much phones. You can add {3 - len_phones} phones'
            return f"-!- Contact '{name} already has 3 phones' -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def change_phone(self, name, old_phone, new_phone):
        name = Name(name)
        if str(name) in self.data:
            record = self.data[str(name)]
            if old_phone[0] in str(record.phones):
                record.phones.value[record.phones.value.index(
                    old_phone[0])] = new_phone[0]
                return f'[+] Phone {old_phone} was changed to {new_phone}!'
            return f"-!- Number {old_phone} doesn`t exist in contact '{name}' -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    def remove_phone(self, name, phone):
        name = Name(name)
        if str(name) in self.data:
            if phone[0] in self.data[str(name)].phones.value:
                self.data[str(name)].phones.value.remove(phone[0])
                return f'[+] Phone {phone} was removed from contact {name}'
            return f"-!- Number {phone} doesn`t exist in contact '{name}' -!-"
        return f'-!- Contact {str(name)} doesn`t exist in contacts! -!-'

    # email handling
    def add_email(self, name, email):
        name = Name(name)
        if str(name) in self.data:
            if not self.data[str(name)].email:
                self.data[str(name)].email = Email(email)
                return f'[+] Email "{email}" was added to the Contact "{name}"'
            return f'-!- Contact "{name}" already has the email! -!-\nYou can change it by entering command "change_email". '
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def change_email(self, name, new_email):
        name = Name(name)
        if str(name) in self.data:
            if self.data[str(name)].email:
                self.data[str(name)].email = Email(new_email)
                return f'[+] {name}`s email was changed to "{new_email}"'
            return f'-!- Contact "{name}" has no email! -!-\nYou can add it by entering the command "add_email".'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def remove_email(self, name):
        name = Name(name)
        if str(name) in self.data:
            if self.data[str(name)].email:
                self.data[str(name)].email = Email(None)
                return f'[+] {name}`s email was removed'
            return f'-!- Contact "{name}" has no email! -!-'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

# birthday handling
    def add_birthday(self, name, birthday):
        name = Name(name)
        if str(name) in self.data:
            if not self.data[str(name)].birthday:
                self.data[str(name)].birthday = Birthday(birthday)
                return f'[+] Birthday "{birthday}" was added to the Contact "{name}"'
            return f'-!- Contact "{name}" already has the birhtday! -!-'
        return f'-!- Contact "{name}" does not exist! -!-'

# func to show the list of contact's with birthdays which are in 'N' days from today
    def show_birthdays_after(self, daysNumber):
        if self.data:
            check_day = datetime.now() + timedelta(days=daysNumber)
            data = [[str(i.name), str(i.phones),
                     str(i.email), str(i.birthday), str(i.address)]
                    for k, i in self.data.items() if i.birthday
                    and datetime.strptime(i.birthday.value, '%d.%m.%Y').day == check_day.day
                    and datetime.strptime(i.birthday.value, '%d.%m.%Y').month == check_day.month]
            if data:
                headers = ('Name', 'Phones', 'Email', 'Birthday', 'Address')
                show_in_console(data, headers, 'rounded_outline')
                return
            else:
                return f"-!- No contacts with birthday on {check_day.date()} -!-"
        return f"-!- Contacts data doesn`t exist -!-"

    # address handling
    def add_address(self, name, address):
        name = Name(name)
        if str(name) in self.data:
            if not self.data[str(name)].address:
                self.data[str(name)].address = Address(address)
                return f'[+] Address "{address}" was added to the contact "{name}"!'
            return f'-!- Contact "{name}" already has the address! -!-\nYou can change it by entering "change_address".'
        return f'-!- Contact "{name}" doesn`t exist -!-'

    def change_address(self, name, new_address):
        name = Name(name)
        if str(name) in self.data:
            if self.data[str(name)].address:
                self.data[str(name)].address = Address(new_address)
                return f'[+] {name}`s address was changed to "{new_address}"!'
            return f'-!- Contact "{name}" has no address! -!-\nYou can add it by entering the command "add_address".'
        return f'-!- Contact "{name}" doesn`t exist! -!-'

    def remove_address(self, name):
        name = Name(name)
        if str(name) in self.data:
            if self.data[str(name)].address:
                self.data[str(name)].address = Address(None)
                return f'[+] {name}`s address was removed!'
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
        return self.value.capitalize().strip()


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
