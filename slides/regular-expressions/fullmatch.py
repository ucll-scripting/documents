import re

def is_valid_float(string):
    regex = r"-?\d+(\.\d+)?"
    return re.fullmatch(regex, string)

def is_valid_date(string):
    regex = r"\d\d([-/])\d\d\1\d\d(\d\d)?"
    return re.fullmatch(regex, string)