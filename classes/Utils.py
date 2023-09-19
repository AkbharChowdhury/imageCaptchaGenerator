import random
import string

from classes.ImageCaptcha import CustomImageCaptcha


class Helper:
    Answer = ''
    @staticmethod
    def generate_image():
        CustomImageCaptcha(Helper.Answer).generate_captcha()
    @staticmethod
    def random_text(size=6):
        return ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=size))
