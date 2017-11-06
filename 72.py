import collections


def flatit(iterable):
    for iter in iterable:
        if isinstance(iter, collections.Iterable):
            if iter == iterable:
                yield iter
            else:
                yield from flatit(iter)
        else:
            yield iter


# print(list(flatit([[1, [[2, [5, [6, [2, "test"]]]], 3], range(-5, -3, 1)]])))
# for x in flatit([[1, [[2, [5, [6, [2, "test"]]]], 3], range(-5, -3, 1)]]):
#     print(x)
