import sys

hist = [0] * 256

for line in sys.stdin.readlines():
    for c in line:
        if c != ' ' and c != '\n':
            hist[ord(c)] += 1

maxElements = max(hist)

for i in range(maxElements, 0, -1):
    newLine = ""
    for j in range(len(hist)):
        if hist[j] > 0:
            newLine += "#" if hist[j] >= i else " "
    print(newLine, end="\n")

for i in range(len(hist)):
    if hist[i] > 0:
        print(chr(i), end="")
