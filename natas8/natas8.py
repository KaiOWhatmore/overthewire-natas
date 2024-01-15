import base64
import config
import requests

import utils

"""
up to here now 13012024
"""

secret = "3d3d516343746d4d6d6c315669563362"
actual_original_secret = 'oubWYf2kBq'
username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
url = config.BASE_URL.format(username)
auth = (username, password)

def reverse(secret):
    return secret[::-1]

def hex2bin(secret):
    return bytes.fromhex(secret)

def base64_decode(secret):
    return base64.b64decode(secret).decode()

def decodeSecret(secret):
    return base64_decode(reverse(hex2bin(secret)))

def bin2hex(secret):
    return secret.hex()

def base64_encode(secret):
    return base64.b64encode(secret.encode())

def encodeSecret(secret):
    return bin2hex(reverse(base64_encode(secret)))

decoded_secret = decodeSecret(secret)

data = {
    'secret': decoded_secret,
    'submit': 'Submit'
}

r = requests.post(url, auth=auth, data=data)

utils.save_file("out.txt", r.text)