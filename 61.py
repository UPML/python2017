import sys
import traceback
import re
from io import StringIO


def force_load(name):
    name += '.py'
    lines = open(name).readlines()
    ldict = {}
    has_except = True
    while (has_except):
        try:
            ldict.clear()
            trueErrors = StringIO()
            # with redirect_stderr(trueErrors):
            exec(''.join(lines), globals(), ldict)
        except SyntaxError as sError:
            lines.pop(sError.lineno - 1)
        except Exception as s:
            # print(s)
            tb = s.__traceback__ #sys.exc_info()[-1]
            # print(traceback.extract_tb(tb))
            line = traceback.extract_tb(tb)[-1][1]
            # print(line)
            # match = re.search('line ([0-9]*)', line)
            # wrong_line_number = int(match.group(1))
            # print(wrong_line_number)
            lines.pop(line - 1)

            # for i, line in enumerate(lines):
            #     print(i, " ", line)
        else:
            has_except = False
    return ldict

# m = force_load('broken_module.py')
# print(m)
# m['bar']()
# m['foo']()
