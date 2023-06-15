import sqlite3

conn = sqlite3.connect('ims.db')

cur = conn.cursor()

#cur.execute('''create table customer(customer_id varchar(30),customer_name varchar(40),customer_addr varchar(50),customer_mail varchar(50))''')
#
#cur.execute('''create table orders(order_id varchar(30) ,product_id varchar(30) ,customer_id varchar(30) ,quantity int)''')
#
#cur.execute('''create table products(product_id varchar(30) ,product_name varchar(50),price float,stock int,suplier_id varchar(30))''')
#
#cur.execute('''create table suplier(suplier_id varchar(30)  ,suplier_name varchar(30),suplier_addr varchar(50),suplier_mail varchar(50))''')
#
#cur.execute('''insert into customer(customer_id,customer_name,customer_addr,customer_mail) values ('CUS1','mithil','knr','mithilreddy0202@gmail.com')''')
#
#cur.execute('''insert into products values ('PRD1','one plus nord',25000,100,'SUP1')''')
#
#cur.execute('''insert into orders values ('ORD1','PRD1','CUS1',10)''')
#
#cur.execute('''insert into suplier values ('SUP1','mithil reddy','hyd','mithilreddy0202@gmail.com')''')
#cur.execute('drop table suplier')
#cur.execute('''update products set product_id = 'PRO1' where product_id = 'PRD1' ''')
conn.commit()