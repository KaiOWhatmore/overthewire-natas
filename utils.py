import base64
import os
import string

import config

ASCII_CHARS = string.ascii_letters + string.digits


def hex2str(h):
    bytes_obj = bytes.fromhex(h)
    return bytes_obj.decode()


def str2hex(s):
    return s.encode().hex()


def is_file_missing_or_empty(file_path):
    """Check if file is empty by reading first character in it"""
    # if file doesn't exist or is empty, return True
    return not os.path.exists(file_path) or os.stat(file_path).st_size == 0


def encode_to_base64(string_to_encode):
    return base64.b64encode(string_to_encode.encode()).decode('utf-8')


def decode_base64_to_string(string_to_decode):
    return base64.b64decode(string_to_decode).decode('utf-8')


def read_file(file_path):
    """Read the contents of a file and return them."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None


def save_file(file_name, response):
    try:
        with open(file_name, "w") as file:
            file.write(response)
    except Exception as e:
        print(f"Error saving file: {e}")


def find_smallest_repeating_substring(s):
    for length in range(1, len(s) + 1):
        substring = s[:length]
        multiplier = len(s) // length
        # Create a repeated version of substring
        repeated_substring = substring * multiplier
        # Check if the repeated substring matches the original string
        if repeated_substring == s or repeated_substring + substring[:len(s) % length] == s:
            return substring
    return s


def get_natas_credentials(level):
    """ url, auth """
    if level < 0 or config.PASSWORDS.get(level - 1) is None:
        raise ValueError("Invalid level number")
    username = f"natas{level}"
    url = config.BASE_URL.format(username=username)
    # the password for the current level was provided from the previous level
    if level > 0:
        level -= 1
    password = config.PASSWORDS.get(level)
    auth = (username, password)
    return url, auth
