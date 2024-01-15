import requests
from config import BASE_URL

username = "natas1"
password = "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"

url = BASE_URL.format(username)

r = requests.get(url, auth=(username, password))

with open("output.txt", "w") as file:
    file.write(r.text)
