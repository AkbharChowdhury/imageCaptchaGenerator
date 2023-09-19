import operator

from ImageCaptcha import CustomImageCaptcha


# link: https://www.youtube.com/watch?v=O70FuH2LhNg&t=180s
def main():



    # name = input("Name")
    # print(name is emp)
    # print(font_manager.get_font_names())
    # text: str = input('Enter captcha image text: ')
    answer: str = random_text();
    image = CustomImageCaptcha(answer)
    image.generate_captcha()
    text: str = input('Enter captcha image text: ')

    if operator.eq(answer, text):
        print("passed")
    else:
        print("failed")


def random_text():
    import string
    import random

    # initializing size of string
    size = 6

    # using random.choices()
    # generating random strings
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=size))


if __name__ == '__main__':
    main()

    # print(random_text())

    # main()
    # Import the following modules
    # from captcha.image import ImageCaptcha, DEFAULT_FONTS
    #
    # font_sizes: tuple[int, int, int] = (40, 70, 100)
    #
    # # Create an image instance of the given size
    # image = ImageCaptcha(width=280,
    #                      height=90,
    #                      font_sizes=(40, 70, 100),
    #                      fonts=DEFAULT_FONTS)
    #
    # # Image captcha text
    # captcha_text = 'apple'
    #
    # # generate the image of the given text
    # data = image.generate(captcha_text)
    #
    # # write the image on the given file and save it
    # image.write(captcha_text, 'test.png')
