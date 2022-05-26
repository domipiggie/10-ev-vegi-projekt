from tkinter import *
import mysql.connector
def connectToDb(dbToConnect: str):
    global mydb 
    mydb = mysql.connector.connect(
        host="mysql-mariadb-25-104.zap-hosting.com",
        user="zap614733-1",
        password="zHCykld3xKxUVRPX",
        database=dbToConnect
    )
# stuff idk
mydb = None
dbToUse = "zap614733-1"
connectToDb(dbToUse)
mycursor = mydb.cursor()


# function that connects to the mysql database

def login():
    query = ("SELECT accountId, username, password FROM users "
             "WHERE username='"+e1.get()+"'")
    mycursor.execute(query)
    found = 0
    for (username) in mycursor:
        found += 1
    if found > 1:
        exit(-1)
    else:
        print(e1.get())

master = Tk()

Label(master, text='username').grid(row=0)
Label(master, text='password').grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

submit = Button(master, text="login", command=login)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
submit.grid(row=2, column=1)

mainloop()