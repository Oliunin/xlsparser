import xlrd
import sqlite3

conn = sqlite3.connect('xlsparser.db')
cur = conn.cursor()

rb = xlrd.open_workbook('registry_small.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)

#Считываем из эксельки переменные
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    comp_inn=int(row[10])
    print('inn type:',type(comp_inn),comp_inn)
    House_addr=row[12]
    House_fias_code=row[13]
    House_reg_inc=row[14]
    House_man_start=row[15]
    House_man_end=row[16]
    House_reg_exc=row[17]
    House_reg_exc_base=row[18]
    House_198data=row[19]
    House_reg_pub=row[20]
    #ищу в базе Primary key компании с ИНН = comp_inn
    cur.execute("SELECT PK FROM Company WHERE comp_inn=?", (comp_inn,))
    comp_id = cur.fetchone()[0]
#    tcomp_id=lcomp_id[0]
#    comp_id=tcomp_id[0]
    print('ID type:', type(comp_id), comp_id)
    #Запиысываем в базу информацию о доме
    cur.execute('''INSERT OR IGNORE INTO House
    (House_addr, House_fias_code, House_reg_inc, House_man_start, House_man_end, House_reg_exc, House_reg_exc_base, House_198data, House_reg_pub, Comp_id)
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
    (House_addr, House_fias_code, House_reg_inc, House_man_start, House_man_end, House_reg_exc, House_reg_exc_base, House_198data, House_reg_pub, comp_id) )
    conn.commit()
#    except: print('shit happened')
#    for c_el in row:
#        print(c_el)
#        print('cel type:',type(c_el))
