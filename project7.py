import pickle
from abc import ABC, abstractmethod

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def list_contacts(self):
        return self.contacts


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


class UserView(ABC):
    """Абстрактний клас для представлення інформації користувачу."""
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_user_choice(self):
        pass

    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def get_contact_info(self):
        pass

    @abstractmethod
    def show_message(self, message):
        pass


class ConsoleView(UserView):
    """Конкретна реалізація представлення для консолі."""
    def display_menu(self):
        print("\nАдресна книга")
        print("1. Додати контакт")
        print("2. Переглянути контакти")
        print("3. Вийти")

    def get_user_choice(self):
        return input("Виберіть опцію (1/2/3): ")

    def show_contacts(self, contacts):
        if not contacts:
            print("\nКонтактів немає.")
        else:
            print("\nСписок контактів:")
            for contact in contacts:
                print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")

    def get_contact_info(self):
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        return name, phone

    def show_message(self, message):
        print(message)


def main():
    book = load_data()
    view = ConsoleView()

    while True:
        view.display_menu()
        choice = view.get_user_choice()

        if choice == '1':
            name, phone = view.get_contact_info()
            book.add_contact(name, phone)
            view.show_message(f"Контакт {name} додано.")
        elif choice == '2':
            view.show_contacts(book.list_contacts())
        elif choice == '3':
            save_data(book)
            view.show_message("Дані збережено. Вихід з програми.")
            break
        else:
            view.show_message("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
