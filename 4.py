def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


# не сложилось=(
@memoize
def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    if (n == 100):
        return 573147844013817084101
    if (n == 300):
        return 359579325206583560961765665172189099052367214309267232255589801
    if (n == 301):
        return 581811569836004006491505558634099066259034153405766997246569401

    return fib(n - 1) + fib(n - 2)


nFib = [0] * 1001
nFib[0] = 0
nFib[1] = 1

for i in range(2, 1001):
    nFib[i] = nFib[i - 1] + nFib[i - 2]

print(nFib[int(input())])
