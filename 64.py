import sys, traceback


class supresser():
    def __init__(self, *args):
        self.exceptions = set(args)

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, traceback):
        if ex_type in self.exceptions:
            return True


class retyper():
    def __init__(self, type_from, type_to):
        self.type_from = type_from
        self.type_to = type_to

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, traceback):
        if ex_type == self.type_from:
            raise self.type_to(*ex_value.args). \
                with_traceback(sys.exc_info()[-1])


class dumper():
    def __init__(self, stream):
        self.stream = stream

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, traceback):
        self.stream.write(ex_type.__name__ + ": " + str(ex_value) + '\n')
        # уже понял, что локально у меня работает не так как на сервере
        # тестирую отработате ли это
        self.stream.write(str(traceback))


# def foo():
#     a = {}
#     a[1]


#
# with supresser(KeyError):
#     foo()
#
# with supresser(ValueError):
#     1 / 0
#
# try:
#     with retyper(OSError, IOError):
#         foo()
# except Exception as e:
#     print(e.args)
#     print(e.__class__)
# finally:
#     pass
#
# with dumper(sys.stdout):
#     foo()