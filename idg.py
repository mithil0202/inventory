import sqlite3

conn = sqlite3.connect('ims.db')

def idgenerator(tab):
        
    cur = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCT':
        idval = 'PRODUCT_ID'
    if tab=='ORDER':
        idval = 'ORDER_ID'
    if tab=='SUPLIER':
        idval = 'SUPLIER_ID'
    print(tab,idval)
    cur.execute(f"SELECT {idval} FROM {tab}")
    new = cur.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)

print(idgenerator('SUPLIER'))