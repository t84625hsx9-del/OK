from model import (
    Phonebook,
    Contact,
    FileHandler,
    ContactNotFoundError,
    FileOperationError
)

FILENAME = 'phonebook.txt'


class PhonebookController:
    """Controller for managing the phonebook."""

    def __init__(self, filename: str = FILENAME):
        self.phonebook = Phonebook()
        self.file_handler = FileHandler(filename)

    def load_phonebook(self) -> None:
        """Loads the phonebook data from the file."""
        try:
            data = self.file_handler.load_data()
            for line in data.splitlines():
                if line.strip():  # Skip empty lines
                    parts = line.split(',')
                    # !!! ИСПРАВЛЕНИЕ ПАРСИНГА !!!
                    # Ожидаем формат "Имя, Телефон, ID: <ID>" (как в исходном __str__ модели)
                    # или "Имя, Телефон, ID" (как в исправленной модели)
                    if len(parts) == 3:
                        name = parts[0].strip()
                        phone = parts[1].strip()
                        raw_id_part = parts[2].strip()
                        # Универсальный парсинг ID:
                        if ':' in raw_id_part:
                            contact_id = raw_id_part.split(':')[1].strip()
                        else:
                            contact_id = raw_id_part
                            
                        # Очищаем ID от возможных знаков препинания, если модель этого не делает
                        contact_id = contact_id.strip('!. ') 
                        
                        contact = Contact(name, phone, contact_id)
                        self.phonebook.add_contact(contact)
        except FileOperationError as e:
            print(f"Error loading phonebook: {e}")
        except Exception as e:
             print(f"An unexpected error occurred during loading: {e}")

    def save_phonebook(self) -> None:
        """Saves the phonebook data to the file."""
        try:
            # ИСПРАВЛЕНИЕ: Используем метод get_all_contacts() для инкапсуляции
            contacts_list = self.phonebook.get_all_contacts() 
            data = '\n'.join(str(contact) for contact in contacts_list) 
            self.file_handler.save_data(data)
        except FileOperationError as e:
            print(f"Error saving phonebook: {e}")
        except Exception as e:
            print(f"Unexpected error during saving: {e}")

    def replace_alan_with_alya(self) -> None:
        """Replaces Alan with Alya."""
        try:
            # УПРОЩЕНИЕ: Полагаемся на метод модели update_contact_name и его обработку ошибок
            self.phonebook.update_contact_name("Alan", "Alya")
        except ContactNotFoundError as e:
            print(f"Ошибка при замене Alan на Alya: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка при замене Alan на Alya: {e}")


    def delete_alex(self) -> None:
        """Deletes Alex."""
        try:
            self.phonebook.remove_contact("Alex")
        except ContactNotFoundError as e:
            print(f"Ошибка при удалении Alex: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка при удалении Alex: {e}")

    def get_all_contacts(self) -> list:
        """Returns all contacts from the phonebook."""
        # ИСПРАВЛЕНИЕ: Используем метод get_all_contacts() для инкапсуляции
        return self.phonebook.get_all_contacts()

    def create_initial_data(self) -> None:
        """Creates initial data in the file if it doesn't exist."""
        try:
            self.file_handler.create_initial_data()
        except FileOperationError as e:
             print(f"Ошибка при создании начальных данных: {e}")

