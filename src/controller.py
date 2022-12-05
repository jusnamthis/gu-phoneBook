import view
import contacts


def button_click():
    act = view.get_action()
    contacts.recognize_action(act)