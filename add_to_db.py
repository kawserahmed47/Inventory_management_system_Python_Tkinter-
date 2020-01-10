from tkinter import *
import mysql.connector
import tkinter.messagebox
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="store"
)

mycursor = mydb.cursor()

class Database:
  def __init__(self, master, *args, **kwargs):
    self.master=master
    self.heading=Label(master, text="Add to the Database", font=('arial 40 bold'), fg='steelblue')
    self.heading.place(x=400, y=0)

    self.name_1= Label(master, text="Enter Product Name", font=('arial 18 bold'))
    self.name_1.place(x=0, y=60)
    self.quantity_1= Label(master, text="Enter Quantity", font=('arial 18 bold'))
    self.quantity_1.place(x=0, y=100)
    self.buy_1= Label(master, text="Enter Buy Price", font=('arial 18 bold'))
    self.buy_1.place(x=0, y=140)
    self.sell_1= Label(master, text="Enter Sell Price ", font=('arial 18 bold'))
    self.sell_1.place(x=0, y=180)
    self.addedBy_1= Label(master, text="Enter Added By", font=('arial 18 bold'))
    self.addedBy_1.place(x=0, y=220)

    self.name_e =Entry(master, width=25, font=('arial 18 bold'))
    self.name_e.place(x=300, y=60)
    self.quantity_e =Entry(master, width=25, font=('arial 18 bold'))
    self.quantity_e.place(x=300, y=100)
    self.buy_e =Entry(master, width=25, font=('arial 18 bold'))
    self.buy_e.place(x=300, y=140)
    self.sell_e =Entry(master, width=25, font=('arial 18 bold'))
    self.sell_e.place(x=300, y=180)
    self.addedBy_e =Entry(master, width=25, font=('arial 18 bold'))
    self.addedBy_e.place(x=300, y=220)

    self.btn_add = Button(master, text="Add to Database", width=20, height=2, bg='steelblue', fg='white', command=self.get_items)
    self.btn_add.place(x=420, y=280)
    self.btn_clear = Button(master, text="Clear All", width=15, height=2, bg='steelblue', fg='white', command=self.clear_items)
    self.btn_clear.place(x=300, y=280)

  def get_items(self, *args, **kwargs):
    self.productName = self.name_e.get()
    self.quantity= self.quantity_e.get()
    self.buy= self.buy_e.get()
    self.sell= self.sell_e.get()
    self.addedBy = self.addedBy_e.get()
    self.date= datetime.datetime.now()

    if self.addedBy == '' or self.sell=='' or self.buy=='' or self.quantity=='' or self.productName=='' :
      tkinter.messagebox.showinfo("Error", "Please Fillup All")
    else:
      sql = "INSERT INTO inventory (productName, quantity, buy, sell, addedBy, date) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (self.productName, self.quantity, self.buy, self.sell, self.addedBy, self.date )
      mycursor.execute(sql, val)
      mydb.commit()
      tkinter.messagebox.showinfo("Successful", "Data Inserted Successfully")

  def clear_items(self, *args, **kwargs):
    self.name_e.delete(0,END)
    self.quantity_e.delete(0,END)
    self.buy_e.delete(0,END)
    self.sell_e.delete(0,END)
    self.addedBy_e.delete(0,END)
    

    




root =Tk()
b= Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()