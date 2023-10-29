from errors import  NotExistsContactError, PhoneLengthError, NotExistsPhoneError
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
     def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise PhoneLengthError
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        name = self.name.value
        phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {name}, phones: {phones}"
    
    def add_phone(self, phone):
        p = Phone(phone)
        self.phones.append(p)

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return 
        raise NotExistsPhoneError
        
    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

class AddressBook(UserDict):
    def add_record(self, record):
       self.data[record.name.value] = record

    def find_record(self, name):
        if not self.data.get(name):
            raise NotExistsContactError
        return self.data[name]
    
    def has_record(self, name):
        if self.data.get(name):
            return True
        return False
    
    def delete_record(self, name):
        if not self.data.get(name):
            raise NotExistsContactError
        del self.data[name]
       