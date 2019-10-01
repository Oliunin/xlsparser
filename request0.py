import requests
import json

#пилю функцию на вход подаю код фиас на выходе ssug.get("value")) - адрес дома
#def getaddr(FIASGuid)
headers = {'Content-Type': 'application/json','Accept': 'application/json','Authorization': 'Token 028a8609accc9e80a8b4544b34b83e71ba4cb09b',}
data = '{ "query": "86f3eec0-4769-4ea4-a8f7-d3b5be27dc43" }'
print('data',type(data),data)
response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/address', headers=headers, data=data)
#print(response.json())
jhouse=response.json()
#print(type(jhouse),jhouse)
ssug=(jhouse.get("suggestions"))[0]
#print(type(dsug),dsug)
#ssug=dsug[0]
print('адрес по ФИАС:',ssug.get("value"))
print('какая-то хуйня',ssug.get("unrestricted_value"))
print('данные',ssug.get("data"))
