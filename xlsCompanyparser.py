import xlrd
import sqlite3

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()

rb = xlrd.open_workbook('registry_small.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
#    print('row legth:',len(row))
#    print(row)
    lic_num=row[0]
    lic_date=row[1]
    lic_status=row[2]
    lic_entry_date=row[3]
    comp_addr=row[6]
    comp_fias_code=row[7]
    comp_name=row[9]
    comp_inn=row[10]
    comp_ogrn=row[11]

#Записываем в базу информацию о компании
    cur.execute('''INSERT OR IGNORE INTO Company
    (lic_num, lic_date, lic_status, lic_entry_date, comp_addr, comp_fias_code, comp_name, comp_inn, comp_ogrn)
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (lic_num, lic_date, lic_status, lic_entry_date, comp_addr, comp_fias_code, comp_name, comp_inn, comp_ogrn))
#    print(cur.lastrowid)
    conn.commit()
