import tkinter as tk
#import mysql.connector
from tkinter import *
import mysql.connector

my_w = tk.Tk()
my_w.geometry("1100x650")
my_w.title("Product information")
# add one Label

customer=tk.Label(my_w,text='Product',font=('Helvetica', 50),width=30,anchor='c')
customer.grid(row=1,column=1,columnspan=4)

prod_id=tk.Label(my_w,text='Product Id:',font=('Helvetica', 20),width=30,anchor='c')
prod_id.grid(row=3,column=1)
prod_idtxt = tk.Entry(my_w, width=40,bg='white')
prod_idtxt.grid(row=3,column=2)

prod_brand=tk.Label(my_w,text='Brand:',font=('Helvetica', 20),width=30,anchor='c')
prod_brand.grid(row=4,column=1)
prod_brandtxt = tk.Entry(my_w, width=40,bg='white')
prod_brandtxt.grid(row=4,column=2)

prod_name=tk.Label(my_w,text='Product Name:',font=('Helvetica', 20),width=30,anchor='c')
prod_name.grid(row=5,column=1)
prod_nametxt = tk.Entry(my_w, width=40,bg='white')
prod_nametxt.grid(row=5,column=2)

prod_nameurdu=tk.Label(my_w,text='Product Name Urdu:',font=('Helvetica', 20),width=30,anchor='c')
prod_nameurdu.grid(row=6,column=1)
prod_nameurdutxt = tk.Entry(my_w,   width=40,bg='white')
prod_nameurdutxt.grid(row=6,column=2)

quantity_perpackage=tk.Label(my_w,text='Quantity Per Package:',font=('Helvetica', 20),width=30,anchor='c')
quantity_perpackage.grid(row=7,column=1)
quantity_perpackagetxt = tk.Entry(my_w, width=40,bg='white')
quantity_perpackagetxt.grid(row=7,column=2)

purchaseprice=tk.Label(my_w,text='Purchase Price:',font=('Helvetica',20),width=30,anchor='c')
purchaseprice.grid(row=8,column=1)
purchasepricetxt = tk.Entry(my_w, width=40, bg='white')
purchasepricetxt.grid(row=8,column=2)

productcode=tk.Label(my_w,text='Code:',font=('Helvetica',20),width=30,anchor='c')
productcode.grid(row=9,column=1)
productcodetxt = tk.Entry(my_w, width=40, bg='white')
productcodetxt.grid(row=9,column=2)

prod_saleprice=tk.Label(my_w,text='Sale Price:',font=('Helvetica',20),width=30,anchor='c')
prod_saleprice.grid(row=10,column=1)
prod_salepricetxt = tk.Entry(my_w, width=40, bg='white')
prod_salepricetxt.grid(row=10,column=2)

prod_wholesaleprice=tk.Label(my_w,text='WholeSale Price:',font=('Helvetica',20),width=30,anchor='c')
prod_wholesaleprice.grid(row=11,column=1)
prod_wholesalepricetxt = tk.Entry(my_w, width=40, bg='white')
prod_wholesalepricetxt.grid(row=11,column=2)

prod_lastupdatedate=tk.Label(my_w,text='Last Update Date:',font=('Helvetica',20),width=30,anchor='c')
prod_lastupdatedate.grid(row=12,column=1)
prod_lastupdatedatetxt = tk.Entry(my_w, width=40, bg='white')
prod_lastupdatedatetxt.grid(row=12,column=2)

prodadd = tk.Button(my_w,text='Add', width=10, command=lambda: add_data())
prodadd.grid(row=13, column=2)


def add_data():
    flag_validation = True  # set the flag
    prodid=prod_idtxt.get("1.0", END)  
    prodbrand=prod_brandtxt.get("0", END)  
    prodname = prod_nametxt.get("0", END)  # read mark
    prodnameurdu= prod_nameurdutxt.get("0", END)
    quantityperpackage = quantity_perpackagetxt.get("0", END)
    purchaseprice = purchasepricetxt.get("0", END)
    product_code = productcodetxt.get("1.0", END)
    productsaleprice = prod_salepricetxt.get("1.0", END)
    productwholesaleprice = prod_wholesalepricetxt.get("1.0", END)
    productlastupdatedate = prod_lastupdatedatetxt.get("1.0", END)

   
    mydb= mysql.connector.connect(
    user="root", password="Ahmad123@", host="localhost", database='ha_db')
    sql="INSERT INTO  product (product_id ,brand ,product_name ,product_name_urdu,quantity_per_package,perchaise_price,code,sale_price, wholesale_price, last_update)VALUES(%s,%s,%s,%s,%s,%s)"
    val=(prodid, prodbrand, prodname, prodnameurdu, quantityperpackage, purchaseprice,product_code,productsaleprice,productwholesaleprice,productlastupdatedate)
    
    mycursor = mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")







my_w.mainloop()
