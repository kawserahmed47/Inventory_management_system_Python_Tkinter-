#import all modules
from tkinter import *
import tkinter.messagebox
import datetime
import mysql.connector
import math
import random
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="store"
)

mycursor = mydb.cursor()
date = datetime.datetime.now().date()

product_list=[]
product_price=[]
product_quantity=[]
product_id=[]

label_list=[]

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.left = Frame(master, width=750, height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=616, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

        self.heading= Label(self.left, text="Amr Shop Store", font=('arial 40 bold'), bg='white')
        self.heading.place(x=0,y=0)

        self.date_1 = Label(self.right, text="Today's Date:" + str(date.strftime("%c")), font=('arial 12 bold'), bg='lightblue', fg='white')
        self.date_1.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Products", font=('arial 16 bold'), bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)
        self.tquantity = Label(self.right, text="Quantity", font=('arial 16 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=140, y=60)
        self.tprice = Label(self.right, text="Amount", font=('arial 16 bold'), bg='lightblue', fg='white')
        self.tprice.place(x=280, y=60)

        #enter stuff
        self.enterid= Label(self.left, text="Enter Product's ID", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0,y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=190, y=80)
        self.enteride.focus()


        self.search_btn = Button(self.left, text="Search", width=22, height=2, bg='orange',command=self.ajax)
        self.search_btn.place(x=350, y=120)

        self.productname = Label(self.left, text="", font=('arial 20 bold'), bg='white', fg='orange')
        self.productname.place(x=0, y=250)

        self.pprice= Label(self.left, text="", font=('arial 20 bold'), bg='white', fg='orange')
        self.pprice.place(x=0, y=300)
        
        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bill)

        self.total_1= Label(self.right, text="", font=('arial 18 bold'), bg='red')
        self.total_1.place(x=0, y=600)

    def ajax(self, *args, **kwargs):
        #query
        sql2 = "select * from inventory where id = %s"
        mycursor.execute(sql2, (self.enteride.get(),))
        result = mycursor.fetchall()
    
        for r in result:
            self.n0 =r[0] #id
            self.n1 =r[1] #name
            self.n2 =r[2] #quantity
            self.n3 =r[3] #buy
            self.n4 =r[4] #sell
            self.n5 =r[5] #addedBy
        
        mydb.commit()
        self.productname.configure(text="Product's Name:"+ str(self.n1))
        self.pprice.configure(text="Product's Unit Price:"+ str(self.n4))

        self.quantity_1 = Label(self.left, text="Enter Quantity", font='arial 18 bold', bg='white')
        self.quantity_1.place(x=0, y= 370)
        self.quantity_e = Entry(self.left, width=25, font='arial 18 bold', bg='lightblue')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()
        self.add_to_cart_btn = Button(self.left, text="Add to cart", width=22, height=2, bg='orange', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=410)

        self.change_1 = Label(self.left, text="Given Amount", font='arial 18 bold', bg='white')
        self.change_1.place(x=0, y= 470)
        self.change_e = Entry(self.left, width=25, font='arial 18 bold', bg='lightblue')
        self.change_e.place(x=190, y=470)
        self.change_amount_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='orange', command=self.change_money)
        self.change_amount_btn.place(x=350, y=510)

        self.generate_bill_btn = Button(self.left, text="Generate Bill", width=72, height=2, bg='red', fg='white', command=self.generate_bill)
        self.generate_bill_btn.place(x=0, y=600)


    def add_to_cart(self, *args, **kwargs):
        self.quantity2 = self.quantity_e.get()
        
        if int(self.n2) < int(self.quantity2) :
            tkinter.messagebox.showinfo("ERROR", "OUT Of Scock")
        else:
            self.total_price = float(self.quantity2)*float(self.n4)
            product_list.append(self.n1)
            product_quantity.append(self.quantity2)
            product_price.append(self.total_price)
            product_id.append(self.n0)

            self.x_index =0
            self.y_index= 100
            self.counter =0
           
            for self.p in product_list:
                self.tempName = Label(self.right, text=str(product_list[self.counter]), font =('arial 18 bold'), bg='lightblue')
                self.tempName.place(x=0, y=self.y_index)
                label_list.append(self.tempName)

                self.tempQuantity = Label(self.right, text=str(product_quantity[self.counter]), font =('arial 18 bold'), bg='lightblue')
                self.tempQuantity.place(x=140, y=self.y_index)
                label_list.append(self.tempQuantity)

                self.tempPrice = Label(self.right, text=str(product_price[self.counter]), font =('arial 18 bold'), bg='lightblue')
                self.tempPrice.place(x=280, y=self.y_index)
                label_list.append(self.tempPrice)

                self.y_index += 40
                self.counter += 1

                self.total_1.configure(text="Total Amount:"+ str(sum(product_price)))
                #delete
                self.quantity_1.place_forget()
                self.quantity_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()

                #auto focus
                self.enteride.focus()
                self.enteride.delete(0,END)




                

    def change_money ( self, *args, **kwargs ):
        self.change_5= Label(self.left, text="", font=('arial 18 bold'), bg='red')
        self.change_5.place(x=0, y=510)
        self.change_2 = self.change_e.get()
        if self.change_2=="" or self.quantity_e=="" :
             tkinter.messagebox.showinfo("ERROR", "Entry is empty!!!")
        else:
            self.change_3= float(self.change_2) - sum(product_price)
            self.change_5.configure(text="Change Amount:"+ str(self.change_3))


    def generate_bill(self, *args, **kwargs):
        #create the bill before updating to the database

        directory ="C:/Users/dcL/Desktop/Store_Managements_System/Invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        company= "\t\t\t\tAmar Shop Pvt. Ltd.\n"
        address= "\t\t\t\tDhaka, Bangladesh\n"
        phone="\t\t\t\t+88 01733728905\n"
        sample="\t\t\t\tInvoice\n"
        dt = "\t\t\t\t" + str(date)

        table_header ="\n\n\t\t\t---------------------------------\n\t\t\tSN.\tProducts\tQty\tAmount\n\t\t\t---------------------------------"
        final= company + address + phone + sample + dt + "\n" + table_header
        rnumber=random.randrange(5000,10000)
        file_name = str(directory) + str(rnumber) + ".rtf"
        f= open(file_name, 'w')
        f.write(final)
        r=1
        i=0
        for t in product_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(product_list[i] + "..." )[:7] + "\t" + str(product_quantity[i])+ "\t" + str(product_price[i]))
            r +=1
            i +=1
        f.write("\n\n\t\t\tTotal: Tk" + str(sum(product_price)))
        f.write("\n\t\t\tThanks for Shopping")
        f.close()

        
        self.x =0
        initial = "select * from inventory where id = %s"
        mycursor.execute(initial, (product_id[self.x],))
        result2 = mycursor.fetchall()

        for i in product_list:
            for r in result2:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            sql3 = "UPDATE inventory SET  quantity=%s  WHERE id = %s"
            val3 = (self.new_stock, product_id[self.x])
            mycursor.execute(sql3,val3)
            mydb.commit()

            sql4 = "INSERT INTO transaction (txnId, product_name, quantity, price, date) VALUES (%s, %s, %s, %s, %s)"
            val4 = (rnumber, product_list[self.x], product_quantity[self.x], product_price[self.x], date )
            mycursor.execute(sql4, val4)
            mydb.commit()
            print("Decressed")
            self.x +=1

        for a in label_list:
            a.destroy()

        del(product_id[:])
        del(product_list[:])
        del(product_quantity[:])
        del(product_price[:])

        
        self.total_1.configure(text="")
        
        self.change_e.delete(0,END)
        #tkinter.messagebox.showinfo("ERROR", "Entry is empty!!!")
        tkinter.messagebox.showinfo("Done", "Billing Successful!!!")

        
        


root = Tk()
b= Application(root)

root.geometry("1366x768+0+0")
root.mainloop()