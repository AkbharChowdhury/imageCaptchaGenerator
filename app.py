# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# win = Tk()
# win.geometry("700x500")
#
# frame = Frame(win, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)
#
# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("test.png"))
#
# # Create a Label Widget to display the text or Image
# label = Label(frame, image = img)
# label.pack()
# label2 = Label(frame, image = ImageTk.PhotoImage(Image.open("captcha.png")))
# label2.pack()
#
# win.mainloop()


from tkinter import Tk, Button, PhotoImage
# other modules you need to import

root = Tk()
root.title("Title of the window")

def eastereggtext1(event):
    # function code here....
    pass

img = PhotoImage(file = 'image_path.png')

imgbutn = Label(root, image=img)
imgbutn.grid(row = 18, column = 7)
imgbutn.bind("<Button-1>", eastereggtext1)

root.mainloop()