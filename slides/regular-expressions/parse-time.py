import re

def parse_time(string):
    regex = r'(\d\d):(\d\d) ([ap]m)'
    match = re.fullmatch(regex, string)
    hours = int(match.group(1))
    minutes = int(match.group(2))
    am_pm = match.group(3)
    return (hours, minutes, am_pm)