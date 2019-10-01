import urllib
import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Token 028a8609accc9e80a8b4544b34b83e71ba4cb09b',
}

data = '{ "query": "86f3eec0-4769-4ea4-a8f7-d3b5be27dc43" }'

response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/address', headers=headers, data=data)


response = urllib.request.urlopen('https://httpbin.org/get')
print(response.read())
