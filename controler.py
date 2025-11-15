from model import (
    Phonebook,
    Contact,
    FileHandler,
    ContactNotFoundError,
    FileOperationError
)

FILENAME = 'phonebook.txt'


class PhonebookController:
    """Контроллер для управления телефонным справочником."""

    def __init__(self, filename: str = FILENAME):
        self.phonebook = Phonebook()
        self.file_handler = FileHandler(filename)

    def load_phonebook(self) -> None:
        """Загружает телефонный справочник из файла."""
        try:
            data = self.file_handler.load_data()
            for line in data.splitlines():
                if line.strip():  # Skip empty lines
                    parts = line.split(',')
                    if len(parts) == 3:
                        name = parts[0].strip()
                        phone = parts[1].strip()
                        contact_id = parts[2].split(':')[1].strip()  # Extract ID
                        contact = Contact(name, phone, contact_id)
                        self.phonebook.add_contact(contact)
        except FileOperationError as e:
            print(f"Ошибка загрузки справочника: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка при загрузке: {e}")

    def save_phonebook(self) -> None:
        """Сохраняет телефонный справочник в файл."""
        try:
            data = '\n'.join(str(contact) for contact in self.phonebook.get_all_contacts())
            self.file_handler.save_data(data)  # Assuming FileHandler has save_data
        except FileOperationError as e:
            print(f"Ошибка при сохранении справочника: {e}")

    def replace_alan_with_alya(self) -> None:
        """Заменяет Alan на Alya."""
        try:
            alan = self.phonebook.find_contact_by_id("907!")  # Поиск Alan по ID
            new_contact = Contact("Alya", "+7 983", "987!")
            self.phonebook.replace_contact(alan.name, new_contact)
        except ContactNotFoundError:
            print("Alan не найден в справочнике.")

    def delete_alex(self) -> None:
        """Удаляет Alex."""
        try:
            self.phonebook.remove_contact("907.")  # Поиск Alex по ID
        except ContactNotFoundError:
            print("Alex не найдена в справочнике.")

    def get_all_contacts(self) -> list:
        """Возвращает все контакты из справочника."""
        return self.phonebook.get_all_contacts()

    def create_initial_data(self) -> None:
        """Создает начальные данные в файле, если он не существует."""
        try:
            self.file_handler.create_initial_data()
        except FileOperationError as e:
            print(f"Ошибка при создании начальных данных: {e}")

