import requests
from config import BASE_URL

username = "natas0"
url = BASE_URL.format(username)

r = requests.get(url, auth=("natas0", "natas0"))

with open("output.txt", "w") as file:
    file.write(r.text)
