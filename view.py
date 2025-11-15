from controller import PhonebookController
from exception import ContactNotFoundError, FileOperationError


class PhonebookView:
    """Отображение для телефонного справочника."""

    def __init__(self, controller: PhonebookController):
        self.controller = controller

    def display_menu(self) -> None:
        """Выводит меню."""
        print("\nТелефонный справочник")
        print("1. Заменить Alan на Alya")
        print("2. Удалить Alex")
        print("3. Показать содержимое")
        print("4. Выход")

    def run(self) -> None:
        """Запускает основное взаимодействие с пользователем."""
        
        # Обрабатываем потенциальные ошибки при инициализации данных
        try:
            self.controller.create_initial_data()
            self.controller.load_phonebook()
        except (FileOperationError, Exception) as e:
            print(f"Критическая ошибка при загрузке или создании данных: {e}")
            return # Выходим, если не можем инициализировать систему

        choice: str = ''

        while choice != '4':
            self.display_menu()
            choice = input("Выберите действие: ")

            if choice == '1':
                # Контроллер сам выводит ошибку, если не находит Alan
                self.controller.replace_alan_with_alya()
                print("Alan заменен на Alya (если он существовал).")
                self.controller.save_phonebook() 

            elif choice == '2':
                # Контроллер сам выводит ошибку, если не находит Alex
                self.controller.delete_alex()
                print("Alex удалена (если она существовала).")
                self.controller.save_phonebook() 

            elif choice == '3':
                contacts = self.controller.get_all_contacts()
                print("\nСодержимое справочника:")
                if not contacts:
                    print("Телефонная книга пуста.")
                for contact in contacts:
                    print(contact) # Метод __str__ класса Contact используется автоматически
            elif choice == '4':
                # Опционально: можно сохранить данные при выходе на всякий случай
                self.controller.save_phonebook() 
                print("Выход из программы.")
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")