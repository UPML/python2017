import re

with open('input.txt') as f:
    for line in f:
        words = line.split()
        first = words[0][:7]

        lastId = 10
        if words[10].__contains__("@"):
            lastId = 11
        lastPos = re.search(words[lastId], line)
        last = line[lastPos.span()[0]:]
        if last[-1] == '\n':
            last = last[:-1]
        print(first + '.' * (80 - (len(first) + len(last))) + last)
