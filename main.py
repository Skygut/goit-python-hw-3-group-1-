import commands_function
from AddressBook import AddressBook


def main():
    book = AddressBook()
    book.load()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = commands_function.parse_input(user_input)
        if command in ["close", "exit", "bye", "q"]:
            book.save()
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(commands_function.show_phone(args, book))
        elif command == "all":
            print(commands_function.show_all(book))
        elif command == "add":
            print(commands_function.add_contact(args, book))
        elif command == "change":
            print(commands_function.change_contact(args, book))
        elif command == "add-birthday":
            print(commands_function.add_birthday(args, book))
        elif command == "show-birthday":
            print(commands_function.show_birthday(args, book))
        elif command == "birthdays":
            print(commands_function.birthdays(book))

        else:
            print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()
