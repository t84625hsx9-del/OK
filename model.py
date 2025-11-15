import os
from typing import List
# Удаляем дублирующиеся определения исключений, 
# предполагая, что они уже импортированы из exception.py
from exception import FileOperationError, ContactNotFoundError 


class Contact:
    """Класс, представляющий контакт в телефонной книге."""

    def __init__(self, name: str, phone: str, contact_id: str):
        self.name = name
        self.phone = phone
        self.contact_id = contact_id.strip('!.') # Очищаем ID при инициализации для согласованности

    def __str__(self):
        # Используем согласованный формат без лишних знаков препинания в конце ID
        return f"{self.name}, {self.phone}, ID:{self.contact_id}"


class Phonebook:
    """Класс, представляющий телефонную книгу."""

    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """Добавляет контакт в телефонную книгу."""
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        """Удаляет контакт из телефонной книги по имени."""
        initial_len = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        if len(self.contacts) == initial_len:
            raise ContactNotFoundError(f"Контакт с именем '{name}' не найден.")
            
    # Добавляем метод для получения контактов для лучшей инкапсуляции (для контроллера)
    def get_all_contacts(self) -> List[Contact]:
        """Возвращает все контакты."""
        return self.contacts

    def update_contact_name(self, old_name: str, new_name: str) -> None:
        """Заменяет имя контакта."""
        found = False
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                found = True
                break
        if not found:
            raise ContactNotFoundError(f"Контакт с именем '{old_name}' не найден.")

    def display_contacts(self) -> str:
        """Возвращает строковое представление всех контактов в телефонной книге."""
        if not self.contacts:
            return "Телефонная книга пуста."
        # Используем get_all_contacts() для доступа
        return "\n".join(str(contact) for contact in self.get_all_contacts())


class FileHandler:
    """Класс для чтения и записи телефонного справочника в файл."""

    def __init__(self, filename: str):
        self.filename = filename
        # print(f"FileHandler создан, filename = {self.filename}")  # Debug

    def load_data(self) -> str:
        """Загружает данные из файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            # Если файла нет, возвращаем пустую строку, контроллер обработает
            return ""
        except Exception as e:
            raise FileOperationError(f"Ошибка при чтении файла: {e}")

    def save_data(self, data: str) -> None:
        """Сохраняет данные в файл."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(data)
            # print('Данные успешно записаны в файл.')  # Debug
        except Exception as e:
            raise FileOperationError(f"Ошибка при записи в файл: {e}")

    def create_initial_data(self) -> None:
        """Создает начальные данные в файле, если он не существует."""
        if not os.path.exists(self.filename):
            try:
                # print("Файл не существует, создаем...")  # Debug
                with open(self.filename, 'w', encoding='utf-8') as file:
                    # Используем согласованный формат без знаков препинания в конце строки
                    file.write("Alan, +7 903, ID:907\n")
                    file.write("Alex, +7 345, ID:907\n")
                    file.write("Alice, +7 346, ID:9800\n")
                    file.write("Adelina, +7 367, ID:9678\n")
                # print("Начальные данные записаны в файл.")  # Debug
            except Exception as e:
                raise FileOperationError(f"Ошибка при создании начальных данных: {e}")