import re

def find_email_addresses(string):
    regex = r"[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*" +
            r"@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)+"
    return re.findall(regex, string)