ACTIONS = {
    1: 'add',
    2: 'show'
}
HELLO_MESSAGE = 'choose the action: 1 - add to contacts, 2 - show contacts: '


def get_action():
    act = input(HELLO_MESSAGE)
    return check_action(act)


def check_action(act):
    if not act.isdigit() or ACTIONS.get(int(act)) == None:
        return get_action()
    return int(act)


def get_contact_data():
    surename = input("Surename: ")
    name = input("Name: ")
    phone = input("Phone num: ")
    desctiption = input("Description: ")
    return (surename, name, phone, desctiption)


def show_contact_row(contact):
    print("Surename: {}\nName: {}\nPhone: {}\nDescription: {}".format(*contact))


def show_contact_sep(contact):
    print("Surename: {}\nName: {}\nPhone: {}\nDescription: {}".format(*contact))