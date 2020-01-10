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
    self.heading=Label(master, text="Update to the Database", font=('arial 30 bold'), fg='steelblue')
    self.heading.place(x=400, y=0)

    self.id_le = Label(master, text="Enter Id", font=('arial 18 bold'))
    self.id_le.place(x=0, y=60)
    self.id_leb =Entry(master, font=('arial 18 bold'), width=15)
    self.id_leb.place(x=300, y=60)

    self.btn_search =Button(master, text="Search", width=15, height=2, bg='orange', command=self.search)
    self.btn_search.place(x=550, y=50)

    self.name_1= Label(master, text="Enter Product Name", font=('arial 18 bold'))
    self.name_1.place(x=0, y=100)
    self.name_e =Entry(master, width=25, font=('arial 18 bold'))
    self.name_e.place(x=300, y=100)

    self.quantity_1= Label(master, text="Enter Quantity", font=('arial 18 bold'))
    self.quantity_1.place(x=0, y=150)
    self.quantity_e =Entry(master, width=25, font=('arial 18 bold'))
    self.quantity_e.place(x=300, y=150)

    self.buy_1= Label(master, text="Enter Buy Price", font=('arial 18 bold'))
    self.buy_1.place(x=0, y=200)
    self.buy_e =Entry(master, width=25, font=('arial 18 bold'))
    self.buy_e.place(x=300, y=200)

    self.sell_1= Label(master, text="Enter Sell Price ", font=('arial 18 bold'))
    self.sell_1.place(x=0, y=250)
    self.sell_e =Entry(master, width=25, font=('arial 18 bold'))
    self.sell_e.place(x=300, y=250)

    self.addedBy_1= Label(master, text="Enter Added By", font=('arial 18 bold'))
    self.addedBy_1.place(x=0, y=300)
    self.addedBy_e =Entry(master, width=25, font=('arial 18 bold'))
    self.addedBy_e.place(x=300, y=300)

    self.btn_update = Button(master, text="Update Database", width=20, height=2, bg='steelblue', fg='white', command=self.update)
    self.btn_update.place(x=420, y=350)
    self.btn_clear = Button(master, text="Clear All", width=15, height=2, bg='steelblue', fg='white', command=self.clear_items)
    self.btn_clear.place(x=300, y=350)

  def update(self, *args, **kwargs):
    self.productName = self.name_e.get()
    self.quantity= self.quantity_e.get()
    self.buy= self.buy_e.get()
    self.sell= self.sell_e.get()
    self.addedBy = self.addedBy_e.get()
    self.date= datetime.datetime.now()
    self.id= self.id_leb.get()

    if self.addedBy == '' or self.sell=='' or self.buy=='' or self.quantity=='' or self.productName=='' :
      tkinter.messagebox.showinfo("Error", "Please Fillup All")
    else:
      sql = "UPDATE inventory SET productName=%s, quantity=%s, buy=%s, sell=%s, addedBy=%s, date=%s WHERE id = %s"
      val = (self.productName, self.quantity, self.buy, self.sell, self.addedBy, self.date, self.id )
      mycursor.execute(sql, val)
      mydb.commit()
      tkinter.messagebox.showinfo("Updated Successful", "Data Updated Successfully")

  def clear_items(self, *args, **kwargs):
    self.name_e.delete(0,END)
    self.quantity_e.delete(0,END)
    self.buy_e.delete(0,END)
    self.sell_e.delete(0,END)
    self.addedBy_e.delete(0,END)

  def search(self, *args, **kwargs):
    sql2 = "select * from inventory where id = %s"
    mycursor.execute(sql2, (self.id_leb.get(),))
    result = mycursor.fetchall()
    
    for r in result:
      self.n1 =r[1] #name
      self.n2 =r[2] #quantity
      self.n3 =r[3] #buy
      self.n4 =r[4] #sell
      self.n5 =r[5] #addedBy
    mydb.commit()

    self.name_e.delete(0, END)
    self.name_e.insert(0, str(self.n1))
    self.quantity_e.delete(0, END)
    self.quantity_e.insert(0, str(self.n2))
    self.buy_e.delete(0, END)
    self.buy_e.insert(0, str(self.n3))
    self.sell_e.delete(0, END)
    self.sell_e.insert(0, str(self.n4))
    self.addedBy_e.delete(0, END)
    self.addedBy_e.insert(0, str(self.n5))
    


    




root =Tk()
b= Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()