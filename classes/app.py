import operator
import tkinter as tk
import tkinter.messagebox as tm
from tkinter import Button, PhotoImage, Label, Entry
from classes.Utils import Helper


class App:
    def __submit(self, text: str):
        if operator.eq(Helper.Answer, text):
            tm.showinfo("Success", "correct")
        else:
            tm.showerror('error', 'please try again!')

    def __refresh_captcha(self, image: Label):
        Helper.Answer = Helper.random_text()
        Helper.generate_image()
        new_image = self.__get_image()
        image.configure(image=new_image)
        image.image = new_image
        return image

    def __get_image(self):
        return PhotoImage(file='captcha.png')

    def __init__(self, master):
        self.__master = master
        self.__master.title('captcha test example'.capitalize())
        self.__size = {"width": 600, "height": 450}

        self.__master.geometry(f"{self.__size.get('width')}x{self.__size.get('height')}")
        self.__frame = tk.Frame(self.__master)
        self.__master.resizable(0, 0)

        self.__captcha_image = self.__get_image()
        self.__image_view = Label(self.__frame, image=self.__captcha_image)
        self.__image_view.pack()

        Button(self.__frame, text='refresh'.capitalize(),
               command=lambda: self.__refresh_captcha(self.__image_view)).pack(pady=20)

        user_input = Entry(self.__frame)
        user_input.pack()
        Button(self.__frame, text='Submit'.capitalize(), command=lambda: self.__submit(user_input.get())).pack(pady=20)
        self.__frame.pack()
