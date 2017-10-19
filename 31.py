import sys

n = int(sys.stdin.readline())

penguin = [
    '   _~_    ',
    '  (o o)   ',
    ' /  V  \\  ',
    '/(  _  )\\ ',
    '  ^^ ^^   '
]

for line in penguin:
    print(line * n)
