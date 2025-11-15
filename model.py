import os
from typing import List


class PhonebookError(Exception):
    """Базовый класс для исключений телефонного справочника."""
    pass


class ContactNotFoundError(PhonebookError):
    """Исключение, возникающее при отсутствии контакта."""
    pass


class FileOperationError(PhonebookError):
    """Исключение, возникающее при ошибках работы с файлом."""
    pass


class Contact:
    """Класс, представляющий контакт в телефонном справочнике."""

    def __init__(self, name: str, phone: str, contact_id: str):
        self.name = name
        self.phone = phone
        self.contact_id = contact_id

    def __str__(self) -> str:
        return f"{self.name}, {self.phone}, ID:{self.contact_id}"


class Phonebook:
    """Класс, представляющий телефонный справочник."""

    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """Добавляет контакт в справочник."""
        self.contacts.append(contact)

    def remove_contact(self, contact_id: str) -> None:
        """Удаляет контакт из справочника по ID."""
        self.contacts = [
            contact for contact in self.contacts if contact.contact_id != contact_id
        ]

    def replace_contact(self, old_name: str, new_contact: Contact) -> None:
        """Заменяет контакт в справочнике по имени."""
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                return

    def get_all_contacts(self) -> List[Contact]:
        """Возвращает все контакты в справочнике."""
        return self.contacts

    def find_contact_by_id(self, contact_id: str) -> Contact:
        """Находит контакт по ID."""
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                return contact
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")


class FileHandler:
    """Класс для чтения и записи телефонного справочника в файл."""

    def __init__(self, filename: str):
        self.filename = filename
        print(f"FileHandler создан, filename = {self.filename}")  # Debug

    def load_data(self) -> str:
        """Загружает данные из файла."""
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            raise FileOperationError(f"Ошибка при чтении файла: {e}")

    def create_initial_data(self) -> None:
        """Создает начальные данные в файле, если он не существует."""
        if not os.path.exists(self.filename):
            try:
                print("Файл не существует, создаем...")  # Debug
                with open(self.filename, 'w') as file:
                    file.write("Alan, +7 903, ID:907!\n")
                    file.write("Alex, +7 345, ID:907.\n")
                    file.write("Alice, +7 346, ID:9800.\n")
                    file.write("Adelina, +7 367, ID:9678.\n")
                print("Начальные данные записаны в файл.")  # Debug
            except Exception as e:
                raise FileOperationError(f"Ошибка при создании начальных данных: {e}")
        else:
            print("Файл уже существует, ничего не делаем.")  # Debug


# Пример использования:
try:
    file_handler = FileHandler("my_phonebook.txt")
    file_handler.create_initial_data()  # Call the method
    content = file_handler.load_data()
    print(content)

except FileOperationError as e:
    print(f"Произошла ошибка: {e}")