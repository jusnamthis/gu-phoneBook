def get_parsed_raw_contact(data):
    return ';'.join([info for info in data])


def get_parsed_sep_contact(data):
    return '\n'.join([info for info in data])