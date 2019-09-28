import xlrd
import sqlite3

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()

cur.execute("SELECT PK from Company")
lPK=cur.fetchall()
print(lPK)
for pk in lPK:
    ipk=pk[0]
    print(ipk)
    cur.execute("SELECT COUNT(Comp_id) from House where Comp_id=%s"),(ipk)
    Icount=cur.fetchone()[0]
    print(Icount)
