from tkinter import *

root = Tk()
root.title('captcha test example')
root.geometry("400x250")


def thing():
    print("prees")


captcha_image = PhotoImage(file='captcha.png')
# imgLabel = Label(image=captcha_image)
# myButton = Button(root, image=captcha_image, command=thing() )
# myButton.pack(pady=20)

image_view = Label(root, image=captcha_image, )
image_view.pack(pady=20)


myLabel = Button(root, text='sss')
myLabel.pack(pady=20)
mainloop()
