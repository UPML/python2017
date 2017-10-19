with open('input.txt') as f:
    keys = []
    words = []
    m = 0
    l = 0
    L = 0
    for i, line in enumerate(f):
        if i == 0:
            keys = line.split()
        else:
            words += filter(lambda x: not x == '', line.split())
            m += len(line)
            l += 1
            L = max(L, len(line) - 1)

    if keys.__contains__('-l'):
            print(l, end=" ")
    if keys.__contains__('-w'):
            print(len(words), end=" ")
    if keys.__contains__('-m'):
            print(m, end=" ")
    if keys.__contains__('-L'):
            print(L, end=" ")
