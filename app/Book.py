from collections import UserDict
from input_checker import name_input, phone_input, email_input, adsress_input, birtgday_input


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(name_input('name'))
        phones = Phone(phone_input('phone'))
        email = Email(email_input('email'))
        address = Address(adsress_input('address'))
        birthday = Birthday(birtgday_input('birthday'))
        for key in self.data:
            if key == str(name):
                return f'Contact {str(name)} exist in contacts'
        record = ContactRecord(name=name, phone=phones, email=email, birthday=birthday, address=address)
        self.data[str(name)] = record
        return f'Contact {str(name)} was added to contacts'

    def change_contact(self):
        name = Name(name_input('name'))
        phones = Phone(phone_input('new phone'))
        email = Email(email_input('new email'))
        address = Address(adsress_input('new address'))
        birthday = Birthday(birtgday_input('new birthday'))
        record = ContactRecord(name=name, phone=phones, email=email, birthday=birthday, address=address)
        self.data[str(name)] = record
        return f'Contact {str(name)} was changed in contacts'

    def remove_contact(self):
        name = Name(name_input('name'))
        try:
            self.data.pop(str(name))
            return f'Contact {str(name)} was remove from contacts!'
        except KeyError:
            return f'Contact {str(name)} not exist. Try again'

    def show_contact(self):
        name = Name(name_input('name'))
        try:
            record = self.data[str(name)]
            phones = ', '.join([str(phone.value) for phone in record.phones])
            return f'Name: {name}\n' \
                   f'Phone(s): {phones if phones else "-"}\n' \
                   f'Email: {record.email if record.email else "-"}\n' \
                   f'Birthday: {record.birthday if record.birthday else "-"}\n' \
                   f'Address: {record.address if record.address else "-"}'
        except KeyError:
            return f'Contact {str(name)} not exist. Try again'

    def show_all(self):
        pass

    # name handling
    # def change_name(self):
    #     pass

# phone handling
    def add_phone(self):
        name = Name(name_input('name'))
        phone = Phone(phone_input('new phone'))
        self.data[str(name)].phones.append(phone)
        return f'Phone {str(phone)} was added to contact {str(name)}'

    def change_phone(self):
        name = Name(name_input('name'))
        old_phone = Phone(phone_input('old phone'))
        new_phone = Phone(phone_input('new phone'))
        record = self.data[str(name)]
        change_flag = False
        for i, phone in enumerate(record.phones):
            if str(phone.value) == old_phone.value:
                record.phones[i] = Phone(new_phone)
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was changed to {new_phone}'
        else:
            return f'{old_phone} is not exist. Try again'

    def remove_phone(self):
        name = Name(name_input('name'))
        old_phone = Phone(phone_input('phone'))
        record = self.data[str(name)]
        change_flag = False
        for i, phone in enumerate(record.phones):
            if str(phone.value) == old_phone.value:
                record.phones.remove(phone)
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was remove from contact {name}'
        else:
            return f'{old_phone} is not exist. Try again'

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
    def __str__(self):
        return self.value


class Email(ContactField):
    pass


class Birthday(ContactField):
    pass


class Address(ContactField):
    pass
