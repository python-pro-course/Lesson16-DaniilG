from tkinter import *
import os
from PIL import Image, ImageTk



class BankAccount:
    def __init__(self, login, password, balance=0):
        self.login = login
        self.password = password
        self.balance = balance
        self.create_user()
    def create_user(self):
        if self.login == '' or self.password == '':
            notif.config(text='Необходимо заполнить поля', fg='red')





main =  Tk()
main.title('Банковая система')
main.geometry('300x300')
def create_account():
    login = s_up_login.get()
    password = s_up_pass.get()
    BankAccount(login, password)

def sign_up():
    global s_up_login
    global s_up_pass
    global notif
    s_up_login = StringVar()
    s_up_pass = StringVar()

    sign_up_screen = Toplevel(main)
    sign_up_screen.title('Sign up')
    sign_up_screen.geometry('300x170')

    Label(sign_up_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)
    Label(sign_up_screen, text='логин').grid(row=1, sticky=W)
    Label(sign_up_screen, text='пароль').grid(row=2, sticky=W)
    notif = Label(sign_up_screen, font=('Calibri', 12))
    notif.grid(row=4, sticky=N, pady=10)

    Entry(sign_up_screen,  textvariable=s_up_login). grid(row=1, column=1)
    Entry(sign_up_screen,  textvariable=s_up_pass). grid(row=2, column=1)


    Button(sign_up_screen, text='Sign up',font=('Calibri', 12), width=15, command=create_account).grid(row=3, sticky=N, pady=10)


def log_in():
    global s_up_login
    global s_up_pass
    s_up_login = StringVar()
    s_up_pass = StringVar()

    log_in_screen = Toplevel(main)
    log_in_screen.title('Log in')
    log_in_screen.geometry('300x170')

    Label(log_in_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)
    Label(log_in_screen, text='логин').grid(row=1, sticky=W)
    Label(log_in_screen, text='пароль').grid(row=2, sticky=W)

    Entry(log_in_screen, textvariable=s_up_login).grid(row=1, column=1)
    Entry(log_in_screen, textvariable=s_up_pass).grid(row=2, column=1)




img = Image.open('data/images/bank.png')
img = img.resize((170, 170))
img = ImageTk.PhotoImage(img)

Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)


Button(main, text='Sign up',font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP)
Button(main, text='Log in',font=('Calibri', 12), width=15, command=log_in).pack(side=TOP)


main.mainloop()


