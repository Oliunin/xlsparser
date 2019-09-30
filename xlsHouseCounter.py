import xlrd
import sqlite3

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()
Housecount = "SELECT COUNT(Comp_id) from House where Comp_id=?"
cur.execute("SELECT PK from Company")
lPK=cur.fetchall()
#print(lPK)
for pk in lPK:
    ipk=pk[0]
    print(type(ipk),ipk)
    cur.execute(Housecount,(ipk,))
    Icount=cur.fetchone()[0]
    print(Icount)
    print(type(Icount),Icount)
    cur.execute("INSERT OR REPLACE INTO Company(comp_house_count) VALUES (?)",( Icount,))
conn.commit()
