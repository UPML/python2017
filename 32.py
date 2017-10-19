import sys

line = sys.stdin.readline()[:-1]

maxLen = 0

for lenPal in range(1, len(line) + 1):
    if line[:lenPal] == line[:lenPal][::-1] or \
                    line[-lenPal:] == line[-lenPal:][::-1]:
        maxLen = lenPal

print(len(line) - maxLen)
