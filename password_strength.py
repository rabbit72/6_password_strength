import re
import sys
import json
from string import punctuation


def load_blacklist(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_blacklist:
        return json.load(file_blacklist)


def get_password_strength(password):
    mark_password = 1
    path_to_blacklist = 'blacklist_passwords'
    black_list = load_blacklist(path_to_blacklist)
    if password in black_list or len(password) < 6:
        return mark_password
    check_list = [
        len(password) > 7,
        len(password) > 9,
        len(password) > 11,
        len(password) > 13,
        len(password) > 15,
        re.search('[0-9]', password),
        re.search('[a-z]', password),
        re.search('[A-Z]', password),
        re.search('[{0}]'.format(punctuation), password)
    ]
    for test in check_list:
        mark_password += 1 if test else 0
    return mark_password


if __name__ == '__main__':
    try:
        password = input('Enter password for evaluation: ')
        password_strength = get_password_strength(password)
        print('Password strength: {0}/10 '.format(password_strength))
    except json.JSONDecodeError:
        sys.exit('Blacklist passwords are not JSON')
    except FileNotFoundError:
        sys.exit('Blacklist was not found. Check file')
