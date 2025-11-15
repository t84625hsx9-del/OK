class PhonebookError(Exception):
    """Базовый класс для исключений телефонного справочника."""
    pass


class ContactNotFoundError(PhonebookError):
    """Исключение, возникающее при отсутствии контакта."""
    pass


class FileOperationError(PhonebookError):
    """Исключение, возникающее при ошибках работы с файлом."""
    pass