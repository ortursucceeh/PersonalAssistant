from collections import UserDict
# , email_input, adsress_input, birthday_input
from input_checker import name_input, phone_input
from console_output import show_in_console


class Book(UserDict):

    # work with contact
    def add_contact(self):
        name = Name(name_input('name'))
        if str(name) in self.data:
            return f'Contact {str(name)} exist in contacts'
        phones = Phone(phone_input('phone (max 3) separated by space'))
        # email = Email(email_input('email'))
        # address = Address(adsress_input('address'))
        # birthday = Birthday(birthday_input('birthday'))
        # , email=email, birthday=birthday, address=address)
        record = ContactRecord(name=name, phone=phones)
        self.data[str(name)] = record
        return f'Contact {str(name)} was added to contacts'

    def change_contact(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts'
        phones = Phone(phone_input('new phone (max 3) separated by space'))
        # email = Email(email_input('new email'))
        # address = Address(adsress_input('new address'))
        # birthday = Birthday(birtgday_input('new birthday'))
        # , email=email, birthday=birthday, address=address)
        record = ContactRecord(name=name, phone=phones)
        self.data[str(name)] = record
        return f'Contact {str(name)} was changed in contacts'

    def remove_contact(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts'
        self.data.pop(str(name))
        return f'Contact {str(name)} was removed from contacts!'

    def show_contact(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts'
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
        show_in_console(data, headers)

    # name handling
    def change_name(self):
        name = Name(name_input('name which you want to change'))
        if str(name) in self.data:
            new_name = Name(name_input('new name'))
            old_record = self.data[str(name)]
            self.data[str(new_name)] = old_record
            del self.data[str(name)]
            return f"Contact {str(name)} name was changed to new '{new_name}'!"
        return f'Contact {str(name)} doesn`t exist in contacts'

# phone handling
    def add_phone(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts'
        phone = Phone(phone_input('new phone (max 3) separated by space'))
        self.data[str(name)].phones.value.append(phone.value[0])
        return f'Phone {str(phone)} was added to contact {str(name)}'

    def change_phone(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts!'
        old_phone = Phone(phone_input('old phone'))
        new_phone = Phone(phone_input('new phone'))
        record = self.data[str(name)]
        change_flag = False
        for i, phone in enumerate(record.phones.value):
            if phone == old_phone.value[0]:
                record.phones.value[i] = new_phone.value[0]
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was changed to {new_phone}!'
        else:
            return f"Number {old_phone} doesn`t exist in contact '{name}'!"

    def remove_phone(self):
        name = Name(name_input('name'))
        if str(name) not in self.data:
            return f'Contact {str(name)} doesn`t exist in contacts!'
        old_phone = Phone(phone_input('phone for remove'))
        record = self.data[str(name)]
        change_flag = False
        for i, phone in enumerate(record.phones.value):
            if phone == str(old_phone.value[0]):
                record.phones.value.remove(phone)
                change_flag = True
        if change_flag:
            return f'Phone {old_phone} was removed from contact {name}!'
        else:
            return f"Number {old_phone} doesn`t exist in contact '{name}'!"

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
    pass


class Birthday(ContactField):
    pass


class Address(ContactField):
    pass
