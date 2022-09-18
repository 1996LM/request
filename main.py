#vamos a estudiar la libreria request

import requests 

url = 'https://www.google.com/?client=safari'

def get_request(url):
    response=requests.get(url)
    return response
response = get_request(url)
print(response.text)

