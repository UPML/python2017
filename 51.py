import sys
import functools


def takes(*takes_args):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(min(len(args), len(takes_args))):
                if not isinstance(args[i], takes_args[i]):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return wraps


exec(sys.stdin.read())
