import requests

package = {
    'APPID': 'your api key will go right here in a string'
    'q': 'portland'
}

r = requests.post('url goes here', params=package)

print(r.json())
