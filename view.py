from controler import PhonebookController


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
        self.controller.create_initial_data()
        self.controller.load_phonebook()
        choice: str = ''

        while choice != '4':
            self.display_menu()
            choice = input("Выберите действие: ")

            if choice == '1':
                self.controller.replace_alan_with_alya()
                print("Alan заменен на Alya (если существовал).")
                self.controller.save_phonebook()
            elif choice == '2':
                self.controller.delete_alex()
                print("Alex удалена (если существовала).")
                self.controller.save_phonebook()
            elif choice == '3':
                contacts = self.controller.get_all_contacts()
                print("\nСодержимое справочника:")
                for contact in contacts:
                    print(contact)
            elif choice == '4':
                print("Выход из программы.")
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")