import re


class Base:
    def __init__(self, regex):
        self.regex = regex

    def is_valid(self, value):
        if type(value) == int:
            value = str(value)
        if re.match(self.regex, value):
            return True
        else:
            return False
