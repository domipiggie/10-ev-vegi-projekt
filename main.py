import tkinter as tk
from tkinter import font as tkfont
import mysql.connector

mydb = None
mycursor = None
dbToUse = "zap614733-1"

class Main(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (LoginScreen, DummyScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginScreen")
    
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the login page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        
        button1 = tk.Button(self, text="Login",
                            command=lambda:login(e1.get(), e2.get(), self.controller))
        
        button1.pack()
        e1.pack()
        e2.pack()

class DummyScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login succesfull", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the login page",
                           command=lambda: controller.show_frame("LoginScreen"))
        button.pack()

def connectToDb(dbToConnect: str):
    global mydb 
    mydb = mysql.connector.connect(
        host="mysql-mariadb-25-104.zap-hosting.com",
        user="zap614733-1",
        password="zHCykld3xKxUVRPX",
        database=dbToConnect
    )

def login(username, password, controller) -> bool:
    query = ("SELECT accountId, username, password FROM users "
             "WHERE username='"+username+"' AND password='"+password+"'")
    mycursor.execute(query)
    found = 0
    for (username) in mycursor:
        found += 1
    if found > 1:
        exit(-1)
    elif found == 1:
        print(username)
        controller.show_frame("DummyScreen")
    else:
        print("not found")

if __name__ == "__main__":
    connectToDb(dbToUse)
    mycursor = mydb.cursor()
    app = Main()
    app.mainloop()