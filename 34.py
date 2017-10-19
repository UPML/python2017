import re


def is_strong(pas):
    if len(pas) < 8:
        return False

    if not re.search(r'\d', pas):
        return False

    if not re.search(r'[a-z]', pas):
        return False

    if not re.search(r'[A-Z]', pas):
        return False

    if re.search(r'anna', pas.lower()):
        return False

    if len(set(pas)) < 4:
        return False

    return True


with open('input.txt') as f:
    for line in f:
        if is_strong(line):
            print("strong")
        else:
            print("weak")
