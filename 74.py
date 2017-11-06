def transpose(matrix):
    return zip(*matrix)


def uniq(s):
    values = set()
    it = iter(s)
    while True:
        try:
            tmp = next(it)
            if tmp not in values:
                values.add(tmp)
                yield tmp
        except StopIteration:
            return


def dict_merge(*dicts):
    res = {}
    for d in dicts:
        for k, v in d.items():
            res[k] = v
    return res


def product(a, b):
    res = 0
    for x, y in zip(a, b):
        res += x * y
    return res

#
# print(list(uniq([1, 2, 3, 1, 2])))
# print(dict_merge({1:2}, {2: 2}, {1: 1}))
# print(product([1, 2, 3], [4, 5, 6]))
