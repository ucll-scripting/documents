import re

def remove_comments(string):
    regex = r"//.*?$|/\*.*?\*/"
    return re.sub(regex, "", string,
                  flags=re.DOTALL | re.MULTILINE)
