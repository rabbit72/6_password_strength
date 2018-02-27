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
    if password in black_list or len(password) <= 6:
        return mark_password
    mark_password += 1 if len(password) >= 8 else 0
    mark_password += 1 if len(password) >= 10 else 0
    mark_password += 1 if len(password) >= 12 else 0
    mark_password += 1 if len(password) >= 14 else 0
    mark_password += 1 if len(password) >= 16 else 0
    mark_password += 1 if re.search('[0-9]', password) else 0
    mark_password += 1 if re.search('[a-z]', password) else 0
    mark_password += 1 if re.search('[A-Z]', password) else 0
    mark_password += 2 if re.search(punctuation, password) else 0
    return mark_password


if __name__ == '__main__':
    try:
        while True:
            password = input('Enter password for evaluation: ')
            if password:
                break
        password_strength = get_password_strength(password)
        print('Password strength: {0}/10 '.format(password_strength))
    except json.JSONDecodeError:
        sys.exit('Blacklist passwords are not JSON')
    except FileNotFoundError:
        sys.exit('Blacklist was not found. Check file: {0}'.format(PATH_TO_BLACKLIST))
