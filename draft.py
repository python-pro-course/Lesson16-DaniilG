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
            notif.config(text='Необходимо заполнить все поля', fg='red')
            return
        notif.config(text='', fg='red')
        all_accounts = os.listdir()
        for name in all_accounts:
            if name == self.login:
                notif.config(text='Такой аккаунт уже существует', fg='red')
                return
        notif.config(text='', fg='red')
        with open(self.login, 'w') as f:
            f.write(f'{self.login}\n'
                    f'{self.password}\n'
                    f'{self.balance}')
        notif.config(text='Аккаунт успешно создан', fg='green')


# Создание главного окна
main = Tk()  # Tk() - конструктор, инициализирующий окно
main.title('Банковская система')  # устанавливаем заголовок окна
main.geometry('300x300')  # устанавливаем размер окна
def login_session():
   all_accounts = os.listdir()
   login_name = log_login.get()
   login_pass = log_pass.get()

   for name in all_accounts:
       if name == login_name:
           with open(name, 'r') as f:
               f = f.read().split('\n')
               password = f[1]
           if login_pass == password:
               login_screen.destroy()
               account_window = Toplevel(main)
               account_window.title('DashBoard')
               return
           else:
               login_notif.config(fg='red', text="Password is incorrect")
               return
   login_notif.config(fg='red', text="Такого аккаунта не существует")

def login():
    # Variables
    global log_login
    global log_pass
    global login_notif
    global login_screen
    log_login = StringVar()
    log_pass = StringVar()

    # Login Screen
    login_screen = Toplevel(main)
    login_screen.title('Login')
    # Labels
    Label(login_screen, text='Login to your account', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text='Username', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text='Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=4, sticky=N)
    # Entries
    Entry(login_screen, textvariable=log_login).grid(row=1, column=1)
    Entry(login_screen, textvariable=log_pass, show='*').grid(row=2, column=1)
    # Entries
    Entry(login_screen, textvariable=log_login).grid(row=1, column=1)
    Entry(login_screen, textvariable=log_pass, show='*').grid(row=2, column=1)

    # Buttons
    Button(login_screen, text='Log in', font=('Calibri', 12), width=15, command=login_session).grid(row=3, pady=10,
                                                                                                    sticky=W)
def create_account():
    login = s_up_login.get()
    password = s_up_pass.get()
    BankAccount(login, password)


# Содздание окна регистрации
def sign_up():
    global s_up_login
    global s_up_pass
    global notif
    s_up_login = StringVar()
    s_up_pass = StringVar()

    sign_up_screen = Toplevel(main)
    sign_up_screen.title('Sign Up')
    sign_up_screen.geometry('200x200')

    # Labels
    Label(sign_up_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)  # row - строка
    Label(sign_up_screen, text='Login').grid(row=1, sticky=W)
    Label(sign_up_screen, text='Password').grid(row=2, sticky=W)
    notif = Label(sign_up_screen, font=('Calibri', 12))
    notif.grid(row=4, sticky=N, pady=10)

    # Entries
    Entry(sign_up_screen, textvariable=s_up_login).grid(row=1, column=1)
    Entry(sign_up_screen, textvariable=s_up_pass).grid(row=2, column=1)

    # Buttons
    Button(sign_up_screen, text='Sign In', font=('Calibri', 12), width=15, command=create_account).grid(row=3, sticky=N,
                                                                                                        pady=10)


# Создание картинки
img = Image.open('data/images/bank.PNG')
img = img.resize((170, 170))
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Buttons
Button(main, text='Sign Up', font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP, pady=10)
Button(main, text='Log In', font=('Calibri', 12), width=15, command=login).pack(side=TOP)

main.mainloop()