from tkinter import *
from PIL import Image, ImageTk

class UpdateBalance(Toplevel):
    def __init__(self, parent, user_name, user_login, user_password, user_balance):
        super().__init__(parent)
        self.title('Sign Up')
        self.geometry('300x300-800+300')
        self.parent = parent
        self.name = user_name
        self.login = user_login
        self.password = user_password
        self.balance = int(user_balance)
        self.amount = IntVar()
        img = Image.open('data/images/cat.jpg').resize((170, 170))

        self.img = ImageTk.PhotoImage(img)

        Label(self, text=f'Ваш баланс: {self.balance}', font=('Calibri', 13)).pack(side=TOP)
        Label(self, image=self.img).pack(side=TOP)

        Entry(self, textvariable=self.amount).pack(side=TOP)

        Button(self, text='Внести', font=('Calibri', 12), width=15, command=self.deposit).pack(side=TOP, pady=10)

        Button(self, text='Внести', font=('Calibri', 12), width=15, command=self.withdraw).pack(side=TOP, pady=10)

    def deposit(self):
        amount = self.amount.get()
        self.amount.set(0)
        self.balance += amount

        with open(self.login, 'w') as f:
            f.write(f'{self.name}\n'
                    f'{self.login}\n'
                    f'{self.password}\n'
                    f'{self.balance}')

    def withdraw(self):
        pass

