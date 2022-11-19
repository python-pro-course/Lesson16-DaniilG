from tkinter import *
import os
from PIL import Image, ImageTk

from sign_up_window import SignUpWindow

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Банковская система')  # устанавливаем заголовок окна
        self.geometry('300x300-800+300')  # устанавливаем размер окна
        img = Image.open('data/images/bank.png').resize((170, 170))
        self.img = ImageTk.PhotoImage(img)


        # Labels
        Label(self, text='Самый безопасный банк').pack(side=TOP)
        Label(self, image=self.img).pack(side=TOP)

        Button(self, text='Sign Up', font=('Calibri', 12), width=15, command=self.sign_up_window).pack(side=TOP, pady=10)
        Button(self, text='Log In', font=('Calibri', 12), width=15).pack(side=TOP)

    def sign_up_window(self):
        SignUpWindow(self)



app = App()



app.mainloop()

