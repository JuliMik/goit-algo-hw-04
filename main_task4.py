# Парсинг введеної строки
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додавання контакту
def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f'Contact {name} is in the list already!'
        else:
            contacts[name] = phone
            return "Contact added."
    except Exception as e:
        return f"An error occurred while adding the contact:{e}"


# Зміна контакту
def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f'Contact {name} is not in the list'

    except Exception as e:
        return f"An error occurred while changing the contact:{e}"


# Показ контакту
def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f'Phone number: {contacts[name]} '
        else:
            return f'Contact {name} is not in the list'
    except Exception as e:
        return f"An error occurred while showing the contact:{e}"


# Виведення всих номерів
def show_all(contacts):
    if not contacts:
        return "Contact list is empty"
    else:
        contact_list = "Contact list:\n"
        for name, phone in contacts.items():
            contact_list += f'Name: {name}\t phone: {phone}\n'
        return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
