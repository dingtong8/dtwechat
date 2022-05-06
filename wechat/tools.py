import hashlib
import random
import string


class GetRandomStr(object):
    """
    random返回字符串
    """

    def __init__(self):
        self.ascii_lowercase = string.ascii_lowercase
        self.ascii_uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.punctuation = string.punctuation

    def lowercase_(self, length=1):
        ran = self.ascii_lowercase
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def digits_(self, length=1):
        ran = self.digits
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def lowercase_uppercase(self, length=1):
        ran = self.ascii_lowercase + self.ascii_uppercase
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def lowercase_digits(self, length=1):
        ran = self.ascii_lowercase + self.digits
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def lowercase_punctuation(self, length=1):
        ran = self.ascii_lowercase + self.punctuation
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def lower_uppercase_digits(self, length=1):
        ran = self.ascii_lowercase + self.ascii_uppercase + self.digits
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char

    def lower_uppercase_digits_punctuation(self, length=1):
        ran = self.ascii_lowercase + self.ascii_uppercase + self.digits + self.punctuation
        char = ''
        for i in range(length):
            char += random.choice(ran)
        return char


def encrypt(des, data):
    ret = hashlib.new(des, data.encode(encoding='utf8')).hexdigest()
    print(ret)




# print(GetRandomStr().lower_uppercase_digits(32))
