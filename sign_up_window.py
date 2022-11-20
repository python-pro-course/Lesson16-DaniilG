from tkinter import *
import os
from PIL import Image, ImageTk

class SignUpWindow(Toplevel):
    def __init__(self, parant):
        super().__init__(parant)
        self.title('Sign Up')
        self.geometry('300x200-800+300')
        self.name = StringVar()
        self.login = StringVar()
        self.password = StringVar()

        # Labels
        Label(self, text='Введите свои данные').grid(row=0, sticky=N, pady=10)  # row - строка
        Label(self, text='Name').grid(row=1, sticky=W)
        Label(self, text='Login').grid(row=2, sticky=W)
        Label(self, text='Password').grid(row=3, sticky=W)
        self.notif = Label(self, font=('Calibri', 12))
        self.notif.grid(row=4, sticky=N, pady=10)

        # Entries
        Entry(self, textvariable=self.name).grid(row=1, column=1)
        Entry(self, textvariable=self.login).grid(row=2, column=1)
        Entry(self, textvariable=self.password, show='*').grid(row=3, column=1)

        # Buttons
        Button(self, text='Sign In', font=('Calibri', 12), width=15, command=self.create_account).grid(row=5,sticky=N)


    def create_account(self):
        name = self.name.get()
        login = self.login.get()
        password = self.password.get()
        all_accounts = os.listdir()

        if name == '' or login == '' or password == '':
            self.notif.config(text='Необходимо заполнить все поля', fg='red')
            return
        self.notif.config(text='', fg='red')
        all_accounts = os.listdir()
        for line in all_accounts:
            if line == self.login:
                self.notif.config(text='Такой аккаунт уже существует', fg='red')
                return
        self.notif.config(text='', fg='red')
        with open(login, 'w') as f:
            f.write(f'{name}\n'
                    f'{login}\n'
                    f'{password}\n'
                    f'0')
        self.notif.config(text='Аккаунт успешно создан', fg='green')


