from collections import UserDict


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(input('Enter name: '))
        phone = Phone(input('Enter phone: '))
        email = Email(input('Enter email: '))
        birthday = Birthday(input('Enter birthday: '))
        address = Address(input('Enter address: '))
        try:
            record = ContactRecord(name, phone, email, birthday, address)
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
        name = Name(input('Enter contact name for change: '))
        new_phone = Phone(input('Enter new phone: '))
        new_email = Email(input('Enter new email: '))
        new_birthday = Birthday(input('Enter birthday: '))
        new_address = Address(input('Enter address: '))
        try:
            record = ContactRecord(name, new_phone, new_email, new_birthday, new_address)
            self.data[name.value.lower()] = record
            return f'Contact {name.value().capitalize()} was changed in contacts!'
        except KeyError:
            print('Wrong name. Try again')
            self.change_contact()

    def remove_contact(self):
        name = Name(input('Enter name: '))
        try:
            self.data.pop(name.value.lower())
            return f'Contact {name.value().capitalize()} was remove from contacts!'
        except KeyError:
            print('Wrong name. Try again')
            self.remove_contact()

    def show_contact(self):
        name = Name(input('Enter name: '))
        result = [f"{'NAME': ^17} {'BIRTHDAY': ^14} {'EMAIL': ^12} {'ADDRESS': ^12} {'PHONES': ^13}"]
        try:
            rec = self.data[name.value.lower()].get()
            phones = ', '.join([phone.value for phone in rec.phones])
            bd = rec.birthday.value if rec.birthday else '-'
            address = rec.address.value[:8] if len(rec.address.value) > 8 else rec.address.value
            email = rec.email.value[:12] if len(rec.email.value) > 12 else rec.email.value
            name_rec = name.value.lower()[:8] + '...' if len(name.value) > 8 else name.value()
            result.append(f"[+] {name_rec.capitalize(): <12} | {bd: ^12} | {email: ^12} | {address: ^12} | {phones}")
            return '\n'.join(result)
        except KeyError:
            print('Wrong name. Try again')
            self.remove_contact()

    def show_all(self):
        pass


class ContactRecord:

    def __init__(self, name, phone=None, email=None, birthday=None, address=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = [Phone(phone)] if phone else []
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None

# name handling
    def change_name(self):
        new_name = input('Enter new name: ')
        if new_name:
            self.name = Name(new_name)
        else:
            print('Try again')
            self.change_name()

# phone handling
    def add_phone(self):
        new_phone = input('Enter phone for add: ')
        if new_phone:
            self.phones.append(Phone(new_phone))
            print(f'Phone {new_phone} was added')
        else:
            print('Try again')
            self.add_phone()

    def change_phone(self):
        old_phone = input('Enter phone for change: ')
        new_phone = input('Enter new phone')
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                print(f'Phone {old_phone} was changed to {new_phone}')
            else:
                print(f'{old_phone} is not exist. Try again')
                self.change_phone()

    def remove_phone(self):
        old_phone = input('Enter phone for remove: ')
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones.remove(phone)
                print(f'Phone {old_phone} was remove')
            else:
                print(f'{old_phone} is not exist. Try again')
                self.remove_phone()

# email handling
    def add_email(self):
        new_email = input('Enter Email for add: ')
        if new_email:
            self.email = Email(new_email)
            print(f'Email {new_email} was added')
        else:
            print('Try again')
            self.add_email()

    def change_email(self):
        old_email = input('Enter Email for change: ')
        new_email = input('Enter new Email')
        if self.email.value == old_email:
            self.email = Email(new_email)
            print(f'Email {old_email} was changed to {new_email}')
        else:
            print(f'{old_email} is not exist. Try again')
            self.change_email()

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

class Address(ContactField):
    pass

contactBook = ()
