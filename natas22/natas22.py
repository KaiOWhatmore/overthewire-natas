import requests

import utils

LEVEL = 22

url, auth = utils.get_natas_credentials(LEVEL)
query_params = {'revelio': ''}

with requests.Session() as session:
    r = session.get(url, auth=auth, params=query_params, allow_redirects=False)
    utils.save_file('out.txt', r.text)