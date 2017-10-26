import sys
import functools
import time


def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.start = time.time()
        if wrapper.in_recurse == 0:
            wrapper.calls = 0
        wrapper.in_recurse += 1
        wrapper.calls += 1
        res = func(*args, **kwargs)
        # print(wrapper.calls)
        wrapper.in_recurse -= 1
        # wrapper.last_time_taken = time.time() - wrapper.start
        # print(wrapper.last_time_taken)
        return res

    wrapper.in_recurse = 0
    wrapper.calls = 0
    wrapper.last_time_taken = 0
    return wrapper


#
# @profiler
# def foo(value):
#     if (value < 0):
#         return 0
#     a = 0
#     return foo(value - 1) + foo(value - 2)
#
#
# foo(4)
# foo(3)
exec(sys.stdin.read())
