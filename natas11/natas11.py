import os
import urllib.parse

import requests

import config
import utils


def get_cookie_data(url, auth, cookie_file):
    """
    Retrieves and returns the cookie data from the given URL.
    If the cookie file exists and is not empty, reads from it.
    Otherwise, makes a request to the URL, saves, and returns the cookie.
    """
    if not os.path.exists(cookie_file) or os.path.getsize(cookie_file) == 0:
        response = requests.get(url, auth=auth)
        cookie_value = urllib.parse.unquote(response.cookies['data'])
        utils.save_file(cookie_file, cookie_value)
        return cookie_value
    else:
        with open(cookie_file, 'r') as file:
            return file.read()


def get_xor_key(s1, s2):
    """
    Generates an XOR key by performing XOR operation between two strings.
    Returns a string representing the XOR result.
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def xor_encrypt(s, key):
    """
    Encrypts a given string using the XOR method with the provided key.
    Returns the encrypted string.
    """
    return ''.join(chr(ord(s[i]) ^ ord(key[i % len(key)])) for i in range(len(s)))


def get_encoded_cookie_payload(json_data, key):
    """
    Encodes the given JSON data using XOR encryption and base64 encoding.
    Returns a dictionary with the encoded data under the key 'data'.
    """
    cookie_payload_to_get_password = utils.encode_to_base64(xor_encrypt(json_data, key))
    return {'data': cookie_payload_to_get_password}


def main():
    # basic variables to start off with
    username = 'natas11'
    password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
    url = config.BASE_URL.format(username)
    auth = (username, password)
    json_defaultdata = '{"showpassword":"no","bgcolor":"#ffffff"}'
    cookie_file = 'cookie_encrypted.txt'

    # fetching the cookie, decoding, decrypting it and encoding and the right cookie to obtain the password
    cookie_b64_encoded_from_site = get_cookie_data(url, auth, cookie_file)
    cookie_decoded_b64_to_string = utils.decode_base64_to_string(cookie_b64_encoded_from_site)
    key = utils.find_smallest_repeating_substring(get_xor_key(cookie_decoded_b64_to_string, json_defaultdata))
    json_show_password_data = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    cookies = get_encoded_cookie_payload(json_show_password_data, key)

    r = requests.post(url, auth=auth, cookies=cookies)
    utils.save_file('out.txt', r.text)


if __name__ == "__main__":
    main()
