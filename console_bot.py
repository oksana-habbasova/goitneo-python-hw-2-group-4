class NoContactsError(Exception):
    pass

class ExistsContactError(Exception):
    pass

class NotExistsContactError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Enter user name and phone please'
        except KeyError:
            return 'There is no contact with this name'
        except IndexError:
            return 'Enter user name please'
        except NoContactsError:
            return 'There are no saved contacts yet'
        except ExistsContactError:
            return 'A contact with this name already exists'
        except NotExistsContactError:
            return 'A contact with this name does not exists'
        
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        raise ExistsContactError
    
    contacts[name] = phone
    return 'Contact added'

@input_error
def change_contact(args, contacts):
    name, phone = args

    if not contacts.get(name):
        raise NotExistsContactError
    
    contacts[name] = phone
    return 'Contact changed'

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def get_contacts(contacts):
    if len(contacts) == 0:
        raise NoContactsError
    
    contacts_str = ''

    for name, phone in contacts.items():
        contacts_str += f'{name}: {phone}, '
    return contacts_str[:-2]


def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')

        if user_input == '':
            print('Enter a command please')
            continue

        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_phone(args, contacts))
        elif command == 'all':
             print(get_contacts(contacts))
        else:
            print('Invalid command.')

main()
