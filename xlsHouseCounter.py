import xlrd
import sqlite3

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()
cur.execute("SELECT PK from Company")
lPK=cur.fetchall()
print(lPK)
for pk in lPK:
    ipk=pk[0]
    print('IPK=',type(ipk),ipk)
    cur.execute('''SELECT COUNT(Comp_id) from House where Comp_id=? AND House_man_end=""''',(ipk,))
    Icount=cur.fetchone()[0]
    print('HouseCount=',type(Icount),Icount)
    cur.execute('''UPDATE Company SET comp_house_count=? WHERE PK=?;''' ,( Icount,ipk,))
    conn.commit()
