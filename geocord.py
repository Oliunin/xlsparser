import requests
import json
import sqlite3
import datetime as dt #ALTER TABLE House ADD COLUMN "timestamp" "timestamp"

def getcord(house_guid):
    headers = {'Content-Type': 'application/json','Accept': 'application/json','Authorization': 'Token 028a8609accc9e80a8b4544b34b83e71ba4cb09b',}
    data = '{ "query":' +'"' + house_guid + '" }"'
    response = requests.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/address', headers=headers, data=data)
    jhouse=response.json()
    dsug=(jhouse.get("suggestions"))
    try:
        ssug=dsug[0]
        dcoord=ssug.get("data")
        try:
            geo_lat=float(dcoord.get("geo_lat"))
            geo_lon=float(dcoord.get("geo_lon"))
            cord=(geo_lat,geo_lon)
        except:
            geo_lat=0
            geo_lon=0
            cord=(-1,-1)
            
    except:
        print('Для',house_guid,'Отсутствуют данные геолокации')
        cord=(-1,-1)

#    print('FIAS:', house_guid,'широта/долгота:', cord)
#    print('широта:',type(geo_lat),geo_lat)
#    print('долгота',type(geo_lon),geo_lon)
    return cord

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()
cur.execute('''SELECT House_fias_code from House WHERE geo_lat IS Null OR geo_lon is Null''')
house_list=cur.fetchall()
#print(type(house_list),house_list)
i=1
for thouse in house_list:
    house_guid=str(thouse[0])
    #    print(i,type(house_guid),'fias guid:',house_guid)
    coord=getcord(house_guid)
    geolat=coord[0]
    print('широта',type(geolat),geolat)
    geolon=coord[1]
    print('широта',type(geolon),geolon)
    time=dt.datetime.now()
    timestamp=time.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute('''UPDATE House SET timestamp=?, geo_lat=?, geo_lon=? WHERE House_fias_code=?''' ,(timestamp, geolat, geolon, house_guid,) )
#        rid=return cur.lastrowid
    print(timestamp,'data inserted:',i,'fias guid:',house_guid,'geolat:',geolat,'geolon:', geolon)
    conn.commit()
#    except:
#        print("shit happened")
#        break
    i=i+1
