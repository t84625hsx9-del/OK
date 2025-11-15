from controler import PhonebookController
from view import PhonebookView

if __name__ == "__main__":
    controller = PhonebookController()
    view = PhonebookView(controller)
    view.run()