import operator
from tkinter import *
import tkinter.messagebox as tm

from classes.ImageCaptcha import CustomImageCaptcha
from classes.Utils import Helper

# # link: https://www.youtube.com/watch?v=O70FuH2LhNg&t=180s



def submit(text: str):
    print(Helper.Answer )
    print(text)
    # if operator.eq(answer, text):
    if text == Helper.Answer:
        tm.showinfo("Success", "correct")
    else:
        tm.showerror('error', f'please try again! the answer was {Helper.Answer}')


def create_app():
    root = Tk()
    root.title('captcha test example')
    root.geometry("600x450")

    captcha_image = PhotoImage(file='captcha.png')
    image_view = Label(root, image=captcha_image)
    image_view.pack()

    def refresh_captcha():
        # pass
        Helper.Answer = Helper.random_text()
        image = CustomImageCaptcha(Helper.Answer)
        image.generate_captcha()
        img2 = PhotoImage(file='captcha.png')
        image_view.configure(image=img2)
        image_view.image = img2

    refresh_button = Button(root, text='refresh'.capitalize(), command=lambda: refresh_captcha())
    refresh_button.pack(pady=20)

    user_input = Entry(root)
    user_input.pack()
    submit_button = Button(root, text='Submit', command=lambda: submit(user_input.get()))
    submit_button.pack(pady=20)
    mainloop()


def main():
    Helper.Answer = Helper.random_text()
    CustomImageCaptcha(Helper.Answer).generate_captcha()
    create_app()


if __name__ == '__main__':
    main()
