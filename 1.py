def getTime(h, m, s):
    return int(s) + int(m) * 60 + int(h) * 60 ** 2


print(-getTime(input(), input(), input()) + getTime(input(), input(), input()))
