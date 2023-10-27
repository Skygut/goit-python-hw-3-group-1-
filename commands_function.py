from AddressBook import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return "Give me name and phone please"
        except KeyError as ke:
            return "User not found"
        except IndexError as ie:
            return "Enter user name"
        except Exception as ea:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    if len(user_input) == 0:
        raise Exception
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


@input_error
def add_contact(args, book):
    name, phone = args
    contact = book.find(name)
    if contact:
        contact.add_phone(phone)
        return "Phone number was added!"
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return f"User: {name} was added."


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    if not book.find(name):
        return "Users contact was not found."
    else:
        contact = book.find(name)
        contact.edit_phone(old_phone, new_phone)
    return f"User: {name} was updated."


@input_error
def show_phone(args, book):
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact
    else:
        return f"User: {name} was not found!"


@input_error
def show_all(book):
    formatted_list = []
    if not book.data:
        raise Exception
    for name, record in book.data.items():
        formatted_list.append(f"{name} : {record}\n")
    return "".join(formatted_list)


@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return f"Users {name} birthday was added"
    else:
        return f"User: {name} was not found!"


@input_error
def show_birthday(args, book):
    name = args[0]
    contact = book.find(name)
    if contact and contact.birthday:
        return contact.birthday.value
    else:
        return f"User: {name} was not found!"


@input_error
def birthdays(book):
    return book.get_birthdays_per_week()
