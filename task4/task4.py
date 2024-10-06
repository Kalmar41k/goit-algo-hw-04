"""
Модуль консольного асистента для керування контактами.

Цей модуль дозволяє користувачеві додавати, змінювати,
шукати контакти за іменем та виводити всі збережені контакти.

Підтримуються команди:
    `add <name> <phone>` — додавання контакту.
    `change <name> <phone>` — зміна номера телефону для існуючого контакту.
    `phone <name>` — пошук номера телефону за іменем.
    `all` — показати всі контакти.
    `exit` або `close` — завершити роботу програми.

Функції:
    `parse_input(user_input)` — розбиває команду користувача на частини.
    `add_contact(args, contacts)` — додає новий контакт до словника.
    `change_contact(args, contacts)` — змінює існуючий контакт у словнику.
    `find_phone(args, contacts)` — шукає телефон за ім'ям у списку контактів.
    `show_all(contacts)` — повертає всі збережені контакти.
    `main()` — головна функція для запуску програми.
"""
def parse_input(user_input):
    """
    Парсує команду, введену користувачем, і розділяє її на команду та аргументи.

    Аргументи:
        user_input (str): рядок введений користувачем.

    Повертає:
        cmd (str): команда в нижньому регістрі.
        *args (list): список аргументів команди.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.

    Аргументи:
        args (list): список аргументів, що містить ім'я та номер телефону.
        contacts (dict): словник контактів.

    Повертає:
        str: повідомлення про успіх або помилку.
    """
    if 1 < len(args) < 3:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    return "Name and phone must be separated by a space."

def change_contact(args, contacts):
    """
    Змінює існуючий контакт у словнику.

    Аргументи:
        args (list): список аргументів, що містить ім'я та новий номер телефону.
        contacts (dict): словник контактів.

    Повертає:
        str: повідомлення про успіх або помилку.
    """
    if 1 < len(args) < 3:
        name, phone = args
        contacts[name] = phone
        return "Contact changed."
    return "Name and phone must be separated by a space."

def find_phone(args, contacts):
    """
    Шукає телефон за іменем у словнику контактів.

    Аргументи:
        args (list): список аргументів, що містить ім'я контакту.
        contacts (dict): словник контактів.

    Повертає:
        str: номер телефону або повідомлення про те, що контакт не знайдений.
    """
    if 0 < len(args) < 2:
        name = args[0]
        for key in contacts:
            if key.lower() == name.lower():
                return contacts[key]
        return "This contact does not exist."
    return "Please write the name as argument."

def show_all(contacts):
    """
    Показує всі контакти у словнику.

    Аргументи:
        contacts (dict): словник контактів.

    Повертає:
        dict: словник всіх контактів.
    """
    return contacts

def main():
    """
    Головна функція, яка запускає консольний асистент.

    Описує командний інтерфейс для взаємодії з користувачем.
    Підтримує команди для додавання, зміни, пошуку та перегляду контактів.
    """
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
            print(find_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
