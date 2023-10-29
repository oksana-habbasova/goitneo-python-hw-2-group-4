class NoContactsError(Exception):
    pass

class NotExistsContactError(Exception):
    pass

class PhoneLengthError(Exception):
    pass

class NotExistsPhoneError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('Enter user name and phone please')
        except KeyError:
            print('There is no contact with this name')
        except IndexError:
            print('Enter user name please')
        except NoContactsError:
            print('There are no saved contacts yet')
        except NotExistsContactError:
            print('A contact with this name does not exists')
        except PhoneLengthError:
            print('Enter 10 digits phone number')
        except NotExistsPhoneError:
             print('A contact with this phone does not exists')
        
    return inner