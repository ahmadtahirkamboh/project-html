import tkinter as tk
#import mysql.connector
from tkinter import *
import mysql.connector

my_w = tk.Tk()
my_w.geometry("1100x650")
my_w.title("Customer information")
# add one Label

customer=tk.Label(my_w,text='Customer',font=('Helvetica', 50),width=30,anchor='c')
customer.grid(row=1,column=1,columnspan=4)

customer_name=tk.Label(my_w,text='Customer name:',font=('Helvetica', 20),width=30,anchor='c')
customer_name.grid(row=3,column=1)
customer_nametxt = tk.Entry(my_w, width=40,bg='white')
customer_nametxt.grid(row=3,column=2)

shop_name=tk.Label(my_w,text='Shop name:',font=('Helvetica', 20),width=30,anchor='c')
shop_name.grid(row=4,column=1)
shop_nametxt = tk.Entry(my_w, width=40,bg='white')
shop_nametxt.grid(row=4,column=2)

customer_address=tk.Label(my_w,text='Customer address:',font=('Helvetica', 20),width=30,anchor='c')
customer_address.grid(row=5,column=1)
customer_addressxt = tk.Entry(my_w, width=40,bg='white')
customer_addressxt.grid(row=5,column=2)

customer_contact=tk.Label(my_w,text='Customer contact:',font=('Helvetica', 20),width=30,anchor='c')
customer_contact.grid(row=6,column=1)
customer_contacttxt = tk.Entry(my_w,   width=40,bg='white')
customer_contacttxt.grid(row=6,column=2)

customer_2contact=tk.Label(my_w,text='Customer 2 contact:',font=('Helvetica', 20),width=30,anchor='c')
customer_2contact.grid(row=7,column=1)
customer_2contacttxt = tk.Entry(my_w, width=40,bg='white')
customer_2contacttxt.grid(row=7,column=2)

customer_2contactname=tk.Label(my_w,text='Customer 2 contact name:',font=('Helvetica',20),width=30,anchor='c')
customer_2contactname.grid(row=8,column=1)
customer_2contactnametxt = tk.Entry(my_w, width=40, bg='white')
customer_2contactnametxt.grid(row=8,column=2)

save = tk.Button(my_w,  text='Add Record', width=10, command=lambda: add_data())
save.grid(row=9, column=2)


def add_data():
    flag_validation = True  # set the flag
    name = customer_nametxt.get("1.0", END)  
    shopname= shop_nametxt.get("1.0",END)  
    customeraddress = customer_addressxt.get("1.0", END)  # read mark
    customercontact = customer_contacttxt.get("1.0", END)
    customer2contact = customer_2contacttxt.get("1.0", END)
    customer2contactname = customer_2contactnametxt.get("1.0", END)
    
    mydb= mysql.connector.connect(
    user="root", password="Ahmad123@", host="localhost", database='ha_db')
    sql="INSERT INTO  customer (name,shop_name ,address ,phone_number,2nd_phone_number,2nd_contact_name)VALUES(%s,%s,%s,%s,%s,%s)"
    val=(name, shopname, customeraddress, customercontact, customer2contact, customer2contactname)
    
    mycursor = mydb.cursor()
    #cursor.execute("""INSERT INTO customer(Customer name ,Shop name ,Customer address ,Customer contact,Customer 2 contact ,Customer 2 contact name)
    # VALUES('name', 'shopname', 'customeraddress',' customercontact', 'customer2contact', 'customer2contactname')""")
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")







my_w.mainloop()
