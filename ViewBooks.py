from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# database stuff
mypass = "zHCykld3xKxUVRPX"
mydatabase="zap614733-1"

con = pymysql.connect(host="mysql-mariadb-25-104.zap-hosting.com",user="zap614733-1",password=mypass,database=mydatabase)
cur = con.cursor()

# asztal
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    # TODO adatbázisból lekérni az összes könyvet, azokat meg valahogy megjeleníteni majd írj dc-n és megbezéljük
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()