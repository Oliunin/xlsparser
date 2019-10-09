import requests
import json
import sqlite3
import datetime as dt #ALTER TABLE House ADD COLUMN "timestamp" "timestamp"

#пилю функцию на вход подаю код фиас на выходе addr=ssug.get("value")) - адрес дома
def getaddr(house_guidGuid):
    headers = {'Content-Type': 'application/json','Accept': 'application/json','Authorization': 'Token 028a8609accc9e80a8b4544b34b83e71ba4cb09b',}
    data = '{ "query":' +'"' + house_guid + '" }"'
#    print('query:',data)
    response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/address', headers=headers, data=data)
    jhouse=response.json()
#    print(jhouse)
    dsug=(jhouse.get("suggestions"))
#    print(dsug)
    try:
        ssug=dsug[0]
        addr=ssug.get("value")
        dcoord=ssug.get("data")
    except:
        addr=('Отсутствуют данные ФИАС')
#    print(type(addr),addr)

    return addr
    #зДЕСЬ БУДУТ ДАННЫЕ:
    #print('адрес по ФИАС:',ssug.get("value"))
    #print('какая-то хуйня',ssug.get("unrestricted_value"))
    #print('данные',ssug.get("data"))

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()
cur.execute('''SELECT House_fias_code from House WHERE house_addr=""''')
house_list=cur.fetchall()
#print(type(house_list),house_list)
i=1
for thouse in house_list:
    house_guid=str(thouse[0])
    #    print(i,type(house_guid),'fias guid:',house_guid)
    addr=getaddr(house_guid)
    time=dt.datetime.now()
    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute('''UPDATE House SET House_addr=?, timestamp=?, WHERE House_fias_code=?;''' ,( addr, timestamp,house_guid,))
#        rid=return cur.lastrowid
    print(timestamp,'data inserted:',i,'fias guid:',house_guid,'addr:',addr)
    conn.commit()
#    except:
#        print("shit happened")
#        break
    i=i+1
