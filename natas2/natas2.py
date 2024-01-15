import requests
from config import BASE_URL


'''
1. ping BASE_URL.format(username)
2. go through the url dirs where you will find /files, /users.txt 
3. ping the users.txt endpoint
'''

username = "natas2"
password = "h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"
url = BASE_URL.format(username) + "/files/users.txt"

r = requests.get(url, auth=(username, password))

with open("output.txt", "w") as file:
    file.write(r.text)
