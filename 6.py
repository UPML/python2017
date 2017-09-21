def isHappy(n):
    start = 0
    if (n < 0 or n > 999999):
        return False
    for i in range(3):
        start += n % 10
        n //= 10
    for i in range(3):
        start -= n % 10
        n //= 10
    return start == 0


n = int(input())

for i in range(1000000):
    if (isHappy(n - i)):
        print(format(n - i, '06d'))
        exit(0)
    if (isHappy(n + i)):
        print(format(n + i, '06d'))
        exit(0)
