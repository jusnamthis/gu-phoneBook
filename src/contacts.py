from view import get_contact_data, show_contact_row, show_contact_sep
from contact_parser import get_parsed_raw_contact, get_parsed_sep_contact


def get_contacts_in_raw():
    with open ('contacts_row.txt') as contacts:
        for line in contacts:
            contact = line.strip().split(';')
            show_contact_row(contact)


def get_contacts_separately():
    contact_data = []
    with open ('contacts_sep.txt') as contacts:
        for line in contacts:
            if line.strip() == '':
                show_contact_sep(contact_data)
                contact_data = []
            else:
                contact_data.append(line.strip())


def add_contact():
    contact = get_contact_data()
    add_contacts_in_raw(contact)
    add_contacts_separately(contact)


def add_contacts_separately(data):
    with open ('contacts_sep.txt', 'a') as contacts:
        contacts.write(get_parsed_sep_contact(data) + '\n\n')


def add_contacts_in_raw(data):
    with open ('contacts_row.txt', 'a') as contacts:
        contacts.write(get_parsed_raw_contact(data) + '\n')


def recognize_action(act):
    if act == 2:
        get_contacts_separately()
    else:
        add_contact()
