from tkinter import *
import os
from PIL import Image, ImageTk




main =  Tk()
main.title('Банковая система')
main.geometry('300x300')


def sign_up():
    sign_up_screen = Toplevel(main)
    sign_up_screen.title('Sign up')
    main.geometry('200x200')

    Label(sign_up_screen, text='Введите логин и пароль').grid(row=0, sticky=N, pady=10)
    Label(sign_up_screen, text='логин').grid(row=1, sticky=W)
    Label(sign_up_screen, text='пароль').grid(row=2, sticky=W)

img = Image.open('data/images/bank.png')
img = img.resize((170, 170))
img = ImageTk.PhotoImage(img)

Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)


Button(main, text='Signe up',font=('Calibri', 12), width=15, command=sign_up).pack(side=TOP)
Button(main, text='Log in',font=('Calibri', 12), width=15).pack(side=TOP)

main.mainloop()


