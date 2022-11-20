from tkinter import *
import os
from PIL import Image, ImageTk
from login_session import LoginSession

class LoginWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Sign Up')
        self.geometry('300x200-800+300')
        self.parent = parent
        self.login = StringVar()
        self.password = StringVar()

        # Labels
        Label(self, text='Login to your account', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
        Label(self, text='Username', font=('Calibri', 12)).grid(row=1, sticky=W)
        Label(self, text='Password', font=('Calibri', 12)).grid(row=2, sticky=W)
        self.notif = Label(self, font=('Calibri', 12))
        self.notif.grid(row=4, sticky=N)
        # Entries
        Entry(self, textvariable=self.login).grid(row=1, column=1)
        Entry(self, textvariable=self.password, show='*').grid(row=2, column=1)

        # Buttons
        Button(self, text='Log in', font=('Calibri', 12), width=15, command=self.login_session).grid(row=3, pady=10,sticky=W)

    def get_details(self, user_login):
        with open(user_login, 'r') as f:
            f = f.read().split('\n')
            name = f[0]
            password = f[2]
        return name, password



    def login_session(self):
        all_accounts = os.listdir()
        user_login = self.login.get()
        user_password = self.password.get()

        for name in all_accounts:
            if name == user_login:
                name, file_password = self.get_details(user_login)
                if user_password == file_password:
                    self.destroy()
                    LoginSession(self.parent, name, user_login, user_password)
                    return
                else:
                    self.notif.config(fg='red', text="Password is incorrect")
                    return
        self.notif.config(fg='red', text="Такого аккаунта не существует")


