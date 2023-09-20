import tkinter as tk
from classes.Utils import Helper
from classes.app import App


# link: https://www.youtube.com/watch?v=O70FuH2LhNg&t=180s
# https://www.youtube.com/watch?v=bVnKX0315lo

def app():
    root = tk.Tk()
    App(root)
    root.resizable(False, False)
    root.mainloop()


def main():
    Helper.Answer = Helper.random_text()
    Helper.generate_image()
    app()


if __name__ == '__main__':
    main()
