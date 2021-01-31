def is_valid_float(string):
    if string[0] == '-':
        string = string[1:]
    parts = string.split('.')
    if len(parts) > 2:
        return False
    if not all(len(part) >= 1 for part in parts):
        return False
    return all(all(c.isdigit() for c in part)
               for part in parts)