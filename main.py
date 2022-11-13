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
            return
        notif.config(text='', fg='red')
        all_accounts = os.listdir()
        for name in all_accounts:
            if name == self.login:
                notif.config(text='твой аккаунт уже существует', fg='red')
                return
        notif.config(text='', fg='red')
        with open(self.login, 'w') as f:
            f.write(f'{self.login}\n'
                    f'{self.password}\n'
                    f'{self.balance}')
        notif.config(text='Аккаунт успешно создан', fg='green')




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


#\\\


def up_money(one=1):
    with open(login, 'r') as f:
        file_list = f.read().split('\n')
        up = money_sum.get()
        num = int(file_list[2])
        num  += (up * one)
    with open(login, 'w') as f:

        f.write(f'{file_list[0]}\n'
                f'{file_list[1]}\n'
                f'{num}')
    money_screen.destroy()


def pl():up_money()
def mi():up_money(-1)


def deposit():
    global money_sum
    global money_screen
    money_sum = IntVar()

    money_screen= Toplevel(log_session_screen)
    money_screen.geometry('320x90')

    Label(money_screen, text='Введите сумму', font=('Calibri', 14)).grid(row=0, column=0, pady=10)

    Entry(money_screen, textvariable=money_sum).grid(row=0, column=1)

    Button(money_screen, text='Пополнить', font=('Calibri', 14), width=15, command=pl).grid(row=1, column=0)
    Button(money_screen, text='Снять', font=('Calibri', 14), width=15, command=mi).grid(row=1, column=1)


def print_sum():
    pr_s = Toplevel(log_session_screen)
    pr_s.geometry('150x90')

    with open(login, 'r') as f:
        file_list = f.read().split('\n')

        Label(pr_s, text=f'{file_list[2]}', font=('Calibri', 18)).grid(pady=10, padx=20)

#///


def log_in_account():
    global log_session_screen
    global login

    login = log_login.get()
    password = log_pass.get()
    all_accounts = os.listdir()
    for name in all_accounts:
        if name == login:

            with open(login, 'r') as f:

                file_list = f.read().split('\n')
                if file_list[1] == password:
                    log_in_screen.destroy()
                    log_session_screen = Toplevel(main)
                    log_session_screen.title('Личный кабинет')
                    log_session_screen.geometry('300x170')
                    Button(log_session_screen, text='Баланс',font=('Calibri', 12), width=15, command=print_sum).pack(side=TOP, pady=10)
                    Button(log_session_screen, text='Изменить баланс', font=('Calibri', 12), width=15, command=deposit).pack(side=TOP,pady=10)

                    # Button(log_session_screen, text='Вывести деньги', font=('Calibri', 12), width=15, command=N).pack(side=TOP, pady=10)

                    print('Вы успешно авторизованы')
                    return
                else:
                    print('Неверный пароль')
                    return
    print('Такого аккаунта не существует')



def login():
    global log_login
    global log_pass
    global notif
    global log_in_screen
    log_login = StringVar()
    log_pass = StringVar()

    log_in_screen = Toplevel(main)
    log_in_screen.title('Log in')
    log_in_screen.geometry('300x170')

    Label(log_in_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)
    Label(log_in_screen, text='Логин').grid(row=1, sticky=W)
    Label(log_in_screen, text='Пароль').grid(row=2, sticky=W)

    Entry(log_in_screen, textvariable=log_login).grid(row=1, column=1)
    Entry(log_in_screen, textvariable=log_pass, ).grid(row=2, column=1)

    notif = Label(log_in_screen, font=('Calibri', 12))
    notif.grid(row=4, sticky=N, pady=10)

    Button(log_in_screen, text='Log in', font=('Calibri', 12), width=15, command=log_in_account).grid(row=3, sticky=N,pady=10)





img = Image.open('data/images/bank.png')
img = img.resize((170, 170))
img = ImageTk.PhotoImage(img)

Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)


Button(main, text='Sign up',font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP)
Button(main, text='Log in',font=('Calibri', 12), width=15, command=login).pack(side=TOP)


main.mainloop()


