import re
import sys
from getpass import getpass
from string import punctuation


def load_blacklist(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_blacklist:
        return [bad_password.rstrip() for bad_password in file_blacklist]


def get_password_strength(password, blacklist):
    min_password_score = 1
    min_len_password = 6
    if password in blacklist or len(password) < min_len_password:
        return min_password_score
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
    return min_password_score + sum(map(bool, check_list))


if __name__ == '__main__':
    try:
        path_to_blacklist = 'blacklist_passwords'
        blacklist = load_blacklist(path_to_blacklist)
        password = getpass()
        password_strength = get_password_strength(password, blacklist)
        print('Password strength: {0}/10 '.format(password_strength))
    except FileNotFoundError:
        sys.exit('Blacklist was not found. Check file')
