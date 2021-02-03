import re

def fix_dates(string):
    regex = r'(\d+)/(\d+)/(\d+)'
    subst = r'\2/\1/\3'
    return re.sub(regex, subst, string)
