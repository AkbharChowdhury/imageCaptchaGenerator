from matplotlib import font_manager

from ImageCaptcha import CustomImageCaptcha


# link: https://www.youtube.com/watch?v=O70FuH2LhNg&t=180s
def main():
    # name = input("Name")
    # print(name is emp)
    # print(font_manager.get_font_names())
    text: str = input('Enter captcha image text: ')
    image = CustomImageCaptcha(text)
    image.generate_captcha()


if __name__ == '__main__':
    main()
