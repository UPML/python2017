import sys

import re


def error():
    print("ERROR")
    sys.exit(0)


def check_and_write_ans(ans):
    if len(ans) != 3:
        error()
    for channel in ans:
        if not 0 <= channel <= 255:
            error()
    for channel in ans:
        print(channel, end=' ')


s = input()
if s[0] == '#':
    nums = re.findall('[\d,abcdef]{2}', s)
    if len(nums) != 3:
        error()
    for i in range(3):
        nums[i] = int(nums[i], 16)
    check_and_write_ans(nums)
else:
    nums = list(map(lambda x: int(x), re.findall('\d+', s)))
    if len(nums) != 3:
        error()
    if '%' in set(s):
        if len(re.findall('%', s)) != 3:
            error()
        nums = list(map(lambda x: x * 255 // 100, nums))
    if 'r' in set(s):
        if not '(' in set(s) or not ')' in set(s) or ',' not in set(s):
            error()
        old_nums = nums[:]
        pos = {'r': 0, 'g': 1, 'b': 2}
        for i in range(len(old_nums)):
            nums[pos[s[i]]] = old_nums[i]
    check_and_write_ans(nums)
