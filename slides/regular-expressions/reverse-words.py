import re

def reverse_words(string):
    def transform(match):
        word = match.group(0)
        return word[::-1]
    regex = r'[a-zA-Z]+'
    return re.sub(regex, transform, string)
