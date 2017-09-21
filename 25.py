import random as rand


def qSort(array):
    if len(array) < 2:
        return array
    middle = rand.randint(0, len(array) - 1)
    delimeter = array[middle]
    l = 0
    r = len(array) - 1
    while r >= l:
        while array[r] > delimeter:
            r -= 1
        while array[l] < delimeter:
            l += 1
        if l <= r:
            t = array[r]
            array[r] = array[l]
            array[l] = t
            r -= 1
            l += 1
    r += 1
    return qSort(array[:r]) + qSort(array[r:])


rand.seed(42)
nOfNumbers = int(input())
array = [int(x) for x in input().split(" ")]
res = qSort(array)
for i in res:
    print(i, end=' ')
