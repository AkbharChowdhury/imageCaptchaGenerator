from io import BytesIO
from PIL import Image
from captcha.image import ImageCaptcha


class CustomImageCaptcha:
    def __init__(self, text: str = 'Hello'):
        self.__text = text if text else "hello world"
        self.__fonts: list[str] = [
            'Geeza Pro',
        ]
        self.__font_sizes: tuple[int, int, int] = (40, 70, 100)

    def generate_captcha(self):
        captcha: ImageCaptcha = ImageCaptcha(width=400,
                                             height=220,
                                             # fonts=self.__fonts,
                                             font_sizes=self.__font_sizes
                                             )
        # captcha.write(text, 'captcha.png')
        data: BytesIO = captcha.generate(self.__text)
        image: Image = Image.open(data)
        image.show('Sample')
