from tkinter import *
import os
from update_balance import UpdateBalance

class LoginSession(Toplevel):
    def __init__(self, parent, user_name, user_login, user_password):
        super().__init__(parent)
        self.title('Sign Up')
        self.geometry('300x200-800+300')
        self.parent = parent
        self.name = user_name
        self.login = user_login
        self.password = user_password
        self.balance =  self.get_current_balance()


        Label(self, text=f'Здравствуйте, {self.name}',font=('Calibri', 13)).pack(side=TOP)

        Label(self, text=f'Ваш, {self.balance}', font=('Calibri', 13)).pack(side=TOP)

        Button(self, text='Deposit', font=('Calibri', 12), width=15, command=self.update_balance).pack(side=TOP, pady=10)
    def get_current_balance(self):

        with open(self.login, 'r') as f:
            f = f.read().split('\n')
            balance = f[3]
        return balance

    def update_balance(self):
        UpdateBalance(self.parent, self.name, self.login, self.password, self.balance)