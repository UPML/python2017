import sys
import functools


def cache(max_cashe_size):
    cashed = {}
    queue = []

    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args in cashed.keys():
                queue.remove(args)
                queue.append(args)
                return cashed[args]
            value = func(*args, **kwargs)
            if len(queue) == max_cashe_size:
                del cashed[queue[0]]
                queue.pop(0)
            cashed[args] = value
            queue.append(args)
            return value

        return wrapper

    return wraps


# @cache(2)
# def foo(value):
#     print('calculate foo for {}'.format(value))
#     return value
#
#
# foo(1)
# foo(2)
# foo(1)
# foo(2)
# foo(3)
# foo(1)
exec(sys.stdin.read())
