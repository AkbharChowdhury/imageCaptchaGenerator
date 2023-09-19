import tkinter as tk
from tkinter import *

import PIL
from PIL import ImageTk, Image


# try:
#     from tkinter import *
#     import tkinter.messagebox as tm
#     import tkinter as tk
#
#     import Tkinter
#     import ttk
#     import islice
#     import os
#
# except ImportError:  # Python 3
#     import tkinter as Tkinter
#     import tkinter.ttk as ttk


# PIL.


class Home:

    def __init__(self, master):
        self.master = master
        self.master.title("Image captcha")
        self.master.geometry("400x250")
        self.frame = tk.Frame(self.master)
        self.captcha_image = ImageTk.PhotoImage(PIL.Image.open("src/captcha.png"))
        # ImageTk.PhotoImage(Image.open("Sample.png"))
        photo = PhotoImage(file="src/captcha.png")
        photoimage = ImageTk.PhotoImage(PIL.Image.open("src/captcha.png"))

        # create title Button
        Label(self.frame, text="Please complete the captcha below", width="300", height="1",
              font='Helvetica 18 bold').pack()
        label = Label(image=photoimage).pack()

        # Label(self.frame, image=IMG).pack()
        # self.login_button = Button(self.frame, text='Login', height="2", width="30",
        #                            ).pack()
        # # lambda prevents function from executing until button is clicked
        #
        # # create spacing between button
        #
        # self.empty_Label_2 = Label(self.frame, text="").pack()
        # self.Quit_button = Button(self.frame, text='Register', height="2", width="30", relief=RAISED,
        #                           ).pack()
        # self.empty_Label = Label(self.frame, text="").pack()
        # self.Quit_button = Button(self.frame, text='Quit', height="2", width="30", relief=RAISED,
        #                          ).pack()
        self.frame.pack()


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Login")
        self.master.geometry("350x120")

        self.frame = tk.Frame(self.master)
        # self.master.resizable(0, 0)  # set resizable to false
        self.captcha_image = ImageTk.PhotoImage(PIL.Image.open("src/captcha.png"))

        # login UI
        # self.label_title = Label(self.frame, text="Student Login", font=("Helvetica", 16))
        self.label_title = Label(self.frame, image=self.captcha_image)
        self.label_username = Label(self.frame, text="Enter username")
        self.label_password = Label(self.frame, text="Enter Password")

        self.entry_username = Entry(self.frame)
        self.entry_password = Entry(self.frame, show="*")
        self.entry_username.focus_set()  # sets focus on username Entry

        self.label_title.grid(row=0, sticky=N)
        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=2, sticky=E)

        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

        self.login_Button = Button(self.frame, text="Login", relief=RAISED,
                               )
        self.login_Button.grid(columnspan=3, padx=5, pady=5)

        self.register_Button = Button(self.frame, text="Register", relief=RAISED,
                                    )
        self.register_Button.grid(row=3, column=1)

        self.frame.pack()


root = tk.Tk()
Login(root)  # Default to the Home Class
# root.resizable(0, 0)  # set resizable to false
root.mainloop()
