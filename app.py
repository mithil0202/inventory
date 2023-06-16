from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

import sqlite3



def idgenerator(tab):    
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCTS':
        idval = 'PRODUCT_ID'
    if tab=='ORDERS':
        idval = 'ORDER_ID'
    if tab=='SUPLIER':
        idval = 'SUPLIER_ID'
    print(tab,idval)
    cn.execute(f"SELECT {idval} FROM {tab}")
    new = cn.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customers')
def customer():
    return render_template('customers.html')

@app.route('/products')
def product():
    return render_template('products.html')

@app.route('/orders')
def order():
    return render_template('orders.html')


@app.route('/supliers')
def suplier():
    return render_template('supliers.html')


###################################################### show custoomer ###########################################################################
@app.route('/show-customers')
def customer_show():
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id']= i[0]
        customer['customer_name'] = i[1]
        customer['customer_addr'] = i[2]
        customer['customer_mail'] = i[3]
        data.append(customer)
    print(data)
    return render_template('showcustomers.html',data = data)

###################################################### show product ###########################################################################
@app.route('/show-product')
def product_show():
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from products")
    data = []
    for i in cn.fetchall():
        products = {}
        products['product_id']= i[0]
        products['product_name'] = i[1]
        products['product_stock'] = i[2]
        products['product_price'] = i[3]
        products['product_suplierid'] = i[4]
        data.append(products)    
    return render_template('showproduct.html',data = data)
    
###################################################### show supplier ###########################################################################
@app.route("/show-suplier")
def show_supplier(): 
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from suplier")
    data = []
    for i in cn.fetchall():
        suplier = {}
        suplier['SUPPLIER_ID'] = i[0]
        suplier['SUPPLIER_NAME'] = i[1]
        suplier['SUPPLIER_ADDR'] = i[2]
        suplier['SUPPLIER_MAIL'] = i[3]
        data.append(suplier)
    return render_template('showsuplier.html',data=data)

########################################################   SHOW ORDERS ##############################################################

@app.route("/show-orders")
def orders_show(): 
    conn = sqlite3.connect('ims.db')
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['ORDER_ID'] = i[0]
        orders['PRODUCT_ID'] = i[1]
        orders['CUSTOMER_ID'] = i[2]
        orders['QUANTITY'] = i[3]
        data.append(orders)
    return render_template('showorders.html',data=data)

################################################   ADD CUSTOMERS    #######################################################################
@app.route('/add-customer',methods = ['GET','POST'])
def addcustomer():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn = conn.cursor()
        customername = request.form.get('name')
        customeraddr = request.form.get('address')
        customermail = request.form.get('email')
        id = idgenerator('CUSTOMER')
        cn.execute(f"insert into customer(customer_id,customer_name,customer_addr,customer_mail) values('{id}','{customername}','{customeraddr}','{customermail}')")
        conn.commit()
        print('Data has been Inserted')
        return render_template('success.html', message='Data has been Inserted Successfully')
    else:
        return render_template('addcustomer.html')
    
################################################   ADD ORDERS    ########################################################################

@app.route("/add-orders",methods=['GET','POST'])
def addorders():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        productid=request.form.get('productid')
        customerid=request.form.get('customerid')
        quantity=request.form.get('quantity')
        id = idgenerator('ORDERS')
        cn.execute(f"insert into orders(order_id,product_id,customer_id,quantity) values('{id}','{productid}','{customerid}','{quantity}')")
        conn.commit()
        print('Data as been Inserted')
        return render_template('success.html', message='Data has been Inserted Successfully')
    else:
        return render_template('addorders.html')

################################################   ADD SUPPLIER    ########################################################################

@app.route("/add-suplier",methods=['GET','POST'])
def addsuplier():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        supliername=request.form.get('name')
        suplieraddr=request.form.get('address')
        supliermail=request.form.get('email')
        id = idgenerator('SUPLIER')
        cn.execute(f"insert into suplier(suplier_id,suplier_name,suplier_addr,suplier_mail) values('{id}','{supliername}','{suplieraddr}','{supliermail}')")
        conn.commit()
        print('Data as been Inserted')
        return render_template('success.html', message='Data has been Inserted Successfully')
    else:
        return render_template('addsuplier.html')

################################################   ADD PRODUCT    ########################################################################

@app.route("/add-product",methods=['GET','POST'])
def addproduct():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        productname=request.form.get('name')
        price=request.form.get('price')
        stock=request.form.get('stock')
        suplierid=request.form.get('product_suplierid')
        id = idgenerator('PRODUCTS')
        cn.execute(f"insert into products(product_id,product_name,price,stock,suplier_id) values('{id}','{productname}','{price}','{stock}','{suplierid}')")
        conn.commit()
        print('Data as been Inserted')
        return render_template('success.html', message='Data has been Inserted Successfully')
    else:
        return render_template('addproduct.html')

################################################   UPDATE CUSTOMER    ########################################################################

@app.route('/update-customer',methods =['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        CUSTOMER_ID= request.form.get("customerid")
        CUSTOMER_ADDR= request.form.get("address")
        CUSTOMER_MAIL= request.form.get("email")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)
        cn.execute(f"UPDATE CUSTOMER SET {change} = '{newvalue}' where customer_id = '{CUSTOMER_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Updated Successfully')
    else:
        return render_template('updatecustomer.html')
    
################################################   UPDATE product    ########################################################################

@app.route('/update-product',methods =['GET','POST'])
def updateproduct():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        PRODUCT_ID=request.form.get("productid")
        PRODUCT_NAME= request.form.get("name")
        PRICE= request.form.get("price")
        STOCK= request.form.get("stock")
        SUPPLIER_ID= request.form.get("supplier id")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)

        cn.execute(f"UPDATE PRODUCTS SET {change} = '{newvalue}' where product_id = '{PRODUCT_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Updated Successfully')
    else:
        return render_template('updateproduct.html')
    
################################################   UPDATE order    ########################################################################

@app.route('/update-order',methods =['GET','POST'])
def updateorder():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        ORDER_ID=request.form.get("orderid")
        PRODUCT_ID= request.form.get("productid")
        CUSTOMER_ID= request.form.get("customerid")
        QUANTITY= request.form.get("quantity")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)
        cn.execute(f"UPDATE ORDERS SET {change} = '{newvalue}' where order_id = '{ORDER_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Updated Successfully')
    else:
        return render_template('updateorder.html')
    
################################################   UPDATE suplier    ########################################################################

@app.route('/update-supplier',methods =['GET','POST'])
def updatesupplier():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        SUPPLIER_ID=request.form.get("supplierid")
        SUPPLIER_NAME= request.form.get("name")
        SUPPLIER_ADDR= request.form.get("address")
        SUPPLIER_MAIL= request.form.get("mail")
        change = request.form.get("change")
        newvalue = request.form.get("newvalue")
        print("change","newvalue")
        cn.execute(f"UPDATE SUPLIER SET {change} = '{newvalue}' where suplier_id = '{SUPPLIER_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Updated Successfully')
    else:
        return render_template('updatesupplier.html')
    
################################################   delete CUSTOMER    ########################################################################
        
@app.route('/delete-customer',methods =['GET','POST'])
def deletecustomer():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        CUSTOMER_ID=request.form.get("customerid")
        cn.execute(f"DELETE FROM CUSTOMER WHERE customer_id = '{CUSTOMER_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Deleted Successfully')
    else:
        return render_template('deletecustomer.html')

################################################   delete product    ########################################################################
    
@app.route('/delete-product',methods =['GET','POST'])
def deleteproduct():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        PRODUCT_ID=request.form.get("productid")
        cn.execute(f"DELETE FROM PRODUCTS WHERE product_id = '{PRODUCT_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Deleted Successfully')
    else:
        return render_template('deleteproduct.html')

################################################   delete order    ########################################################################
    
@app.route('/delete-order',methods =['GET','POST'])
def deleteorder():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        ORDER_ID=request.form.get("orderid")
        cn.execute(f"DELETE FROM ORDERS WHERE order_id = '{ORDER_ID}'")
        conn.commit()
        print('data inserted')
        return render_template('success.html', message='Data has been Deleted Successfully')
    else:
        return render_template('deleteorder.html')

################################################   delete suplier    ########################################################################
    
@app.route('/delete-supplier',methods =['GET','POST'])
def deletesupplier():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        SUPPLIER_ID=request.form.get("supplierid")
        cn.execute(f"DELETE FROM SUPLIER WHERE suplier_id = '{SUPPLIER_ID}'")
        conn.commit()
        print('data has been deleted')
        return render_template('success.html', message='Data has been Deleted Successfully')
    else:
        return render_template('deletesupplier.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)