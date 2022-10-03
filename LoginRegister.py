import sqlite3
from tkinter import *
from tkinter import messagebox



class Login:
    def __init__(self):
        self.connector = sqlite3.connect('CollegeManagement.db')
        cursor = self.connector.cursor()
        self.connector.execute(
            """
            CREATE TABLE IF NOT EXISTS "Users" (
	            "USER_ID"	INTEGER,
	            "FIRST_NAME"	TEXT,
	            "LAST_NAME"	TEXT,
	            "USERNAME"	TEXT NOT NULL UNIQUE,
	            "PASSWORD"	TEXT NOT NULL,
	            PRIMARY KEY("USER_ID" AUTOINCREMENT)
            )
            """
        )
        self.tk = Tk()
        self.fontIpLabel = "nunito 12"
        self.tk.geometry("567x330")
        self.tk.configure(bg="#ffffff")
        self.addTitleFrame()
        self.addLeftFrame()
        self.addRightFrame()
        self.tk.mainloop()

    def addTitleFrame(self):
        self.titleFrame = Frame(self.tk,width=567,height=67,bg="#D85D5D")
        self.titleFrame.pack(side=TOP,anchor=NW)
        self.titleFrame.propagate(0)
        self.lblTitle = Label(self.titleFrame,bg="#D85D5D",fg="#ffffff",font="nunito 25",text="College Management System")
        self.lblTitle.pack(side=TOP,anchor=CENTER,pady=10)

    def addLeftFrame(self):
        self.leftFrame = Frame(self.tk,width=239,height=230,bg="#ffffff")
        self.leftFrame.pack(side=LEFT,anchor=CENTER,padx=18.5)
        self.leftFrame.propagate(0)
        self.lblLogin = Label(self.leftFrame,text="Login",font="nunito 34 bold",bg="#ffffff",fg="#D85D5D")
        self.lblLogin.pack(side=LEFT,anchor=CENTER,padx=50)

    def addRightFrame(self):
        self.rightFrame = Frame(self.tk,width=270,height=374,bg="#ffffff")
        self.rightFrame.pack(side=LEFT,anchor=CENTER,padx=(0,18.5))
        # self.rightFrame.propagate(0)

        self.lblUsername = Label(self.rightFrame,text="Username",font=self.fontIpLabel,bg="#ffffff")
        self.lblUsername.pack(side=TOP,anchor=NW)

        self.txtUsername = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtUsername.pack(side=TOP,anchor=NW,pady=(0,10))

        self.lblPassword = Label(self.rightFrame,text="Password",font=self.fontIpLabel,bg="#ffffff")
        self.lblPassword.pack(side=TOP,anchor=NW)

        self.txtPassword = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtPassword.pack(side=TOP,anchor=NW,pady=(0,10))

        self.btnLogin = Button(self.rightFrame,command=self.login,text="Login",font=self.fontIpLabel+" bold",width=270,height=1,bg="#EE8F8F",fg="#ffffff")
        self.btnLogin.pack(side=TOP,anchor=NW,pady=(0,10))


        self.btnGoToRegister = Button(self.rightFrame,command=self.gotoRegister,text="Don't have an account",font=self.fontIpLabel+" bold",width=270,height=1,bg="#EE8F8F",fg="#ffffff")
        self.btnGoToRegister.pack(side=TOP,anchor=NW,pady=(0,10))

    def gotoRegister(self):
        self.tk.destroy()
        Register()

    def login(self):
        cursor = self.connector.cursor()
        """
        CREATE TABLE IF NOT EXISTS Users 
        (
            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            FIRST_NAME TEXT, 
            LAST_NAME TEXT, 
            USERNAME TEXT, 
            PASSWORD TEXT
        )
        """
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        if not username.strip():
            messagebox.showerror(title="Validation Error",message="Please enter username")
            return
        elif not password.strip():
            messagebox.showerror(title="Validation Error",message="Please enter password")
            return
        sql = "select * from Users where USERNAME=? and PASSWORD=?"
        cursor.execute(sql,(username,password))
        res = cursor.fetchall()
        if res:
            messagebox.showinfo(title="Success", message="Logged In Successfully")
            self.tk.destroy()
            import main
        else:
            messagebox.showerror(title="Login Error", message="Invalid Username / Password")

class Register:
    def __init__(self):
        self.connector = sqlite3.connect('CollegeManagement.db')
        cursor = self.connector.cursor()
        self.connector.execute(
            "CREATE TABLE IF NOT EXISTS Users (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FIRST_NAME TEXT, LAST_NAME TEXT, USERNAME TEXT, PASSWORD TEXT)"
        )
        self.tk = Tk()
        self.fontIpLabel = "nunito 12"
        self.tk.geometry("567x467")
        self.tk.configure(bg="#ffffff")
        self.addTitleFrame()
        self.addLeftFrame()
        self.addRightFrame()
        self.tk.mainloop()

    def addTitleFrame(self):
        self.titleFrame = Frame(self.tk,width=567,height=67,bg="#D85D5D")
        self.titleFrame.pack(side=TOP,anchor=NW)
        self.titleFrame.propagate(0)
        self.lblTitle = Label(self.titleFrame,bg="#D85D5D",fg="#ffffff",font="nunito 25",text="College Management System")
        self.lblTitle.pack(side=TOP,anchor=CENTER,pady=10)

    def addLeftFrame(self):
        self.leftFrame = Frame(self.tk,width=239,height=400,bg="#ffffff")
        self.leftFrame.pack(side=LEFT,anchor=CENTER,padx=18.5)
        self.leftFrame.propagate(0)
        self.lblRegister = Label(self.leftFrame,text="Register",font="nunito 34 bold",bg="#ffffff",fg="#D85D5D")
        self.lblRegister.pack(side=LEFT,anchor=CENTER,padx=30)

    def addRightFrame(self):
        self.rightFrame = Frame(self.tk,width=270,height=400,bg="#ffffff")
        self.rightFrame.pack(side=LEFT,anchor=CENTER,padx=(0,18.5))
        # self.rightFrame.propagate(0)

        self.lblFirstName = Label(self.rightFrame,text="First Name",font=self.fontIpLabel,bg="#ffffff")
        self.lblFirstName.pack(side=TOP,anchor=NW)

        self.txtFirstName = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtFirstName.pack(side=TOP,anchor=NW,pady=(0,10))

        self.lblLastName = Label(self.rightFrame,text="Last Name",font=self.fontIpLabel,bg="#ffffff")
        self.lblLastName.pack(side=TOP,anchor=NW)

        self.txtLastName = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtLastName.pack(side=TOP,anchor=NW,pady=(0,10))

        self.lblUsername = Label(self.rightFrame,text="Username",font=self.fontIpLabel,bg="#ffffff")
        self.lblUsername.pack(side=TOP,anchor=NW)

        self.txtUsername = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtUsername.pack(side=TOP,anchor=NW,pady=(0,10))

        self.lblPassword = Label(self.rightFrame,text="Password",font=self.fontIpLabel,bg="#ffffff")
        self.lblPassword.pack(side=TOP,anchor=NW)

        self.txtPassword = Entry(self.rightFrame,font=self.fontIpLabel,bg="#ffffff",width=26)
        self.txtPassword.pack(side=TOP,anchor=NW,pady=(0,10))

        self.btnRegister = Button(self.rightFrame,command=self.register,text="Register",font=self.fontIpLabel+" bold",width=270,height=1,bg="#EE8F8F",fg="#ffffff")
        self.btnRegister.pack(side=TOP,anchor=NW,pady=(0,10))

        self.btnGoToLogin = Button(self.rightFrame,command=self.gotoLogin,text="Already have an account",font=self.fontIpLabel+" bold",width=270,height=1,bg="#EE8F8F",fg="#ffffff")
        self.btnGoToLogin.pack(side=TOP,anchor=NW,pady=(0,10))

    def gotoLogin(self):
        self.tk.destroy()
        Login()

    def register(self):
        """
        CREATE TABLE IF NOT EXISTS Users
        (
            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            FIRST_NAME TEXT,
            LAST_NAME TEXT,
            USERNAME TEXT,
            PASSWORD TEXT
        )
        """
        firstName = self.txtFirstName.get()
        lastName = self.txtLastName.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        message = None
        if not firstName.strip():
            message = "Please enter your first name"
        elif not lastName.strip():
            message = "Please enter your last name"
        elif not username.strip():
            message = "Please enter your username"
        elif not password.strip():
            message = "Please enter your password"

        if message:
            messagebox.showerror(title="Validation Error", message=message)
            return

        try:
            sql = "INSERT INTO Users(FIRST_NAME,LAST_NAME,USERNAME,PASSWORD) values(?,?,?,?)"
            cursor = self.connector.cursor()

            cursor.execute(sql,(firstName,lastName,username,password))
            self.connector.commit()
            rowCount = cursor.rowcount
        except sqlite3.IntegrityError as err:
            messagebox.showerror(title="Registration Error", message=err)

        if rowCount != 0:
            messagebox.showinfo(title="Registration Successful!",message="Registration Successful!")

Login()