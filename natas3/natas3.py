import requests
from config import BASE_URL

"""
1. ping the /robots.txt path.  robots.txt is used to avoid web crawlers 
2. inside there will be a path called /s3cr3t
3. nested inside /s3cr3t will be /users.txt, i.e. http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
"""

username = "natas3"
url = BASE_URL.format(username) + "/s3cr3t/users.txt"
password = "G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"

r = requests.get(url, auth=(username, password))

with open("output.txt", "w") as file:
    file.write(r.text)