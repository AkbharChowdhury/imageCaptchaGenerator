import random
import string


class Helper:
    Answer = '';
    @staticmethod
    def random_text(size=6):
        return ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=size))
