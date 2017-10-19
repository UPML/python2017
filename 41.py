import sys


class ExtendedList(list):
    def __init__(self, data):
        super().__init__(data)

    def __setattr__(self, key, value):
        if key == 'first' or key == 'F':
            self.__dict__[key] = self.__setitem__(0, value)

        if key == "last" or key == "L":
            self.__dict__[key] = self.__setitem__(-1, value)

        if key == "reversed" or key == "R":
            self.__dict__[key] = self.__reversed__

        if key == "size" or key == "S":
            if len(self) > value:
                for i in range(value, len(self)):
                    self.pop()
            else:
                for i in range(len(self), value):
                    self.append(None)

    def __getattr__(self, key):
        if key == 'first' or key == 'F':
            return self.__getitem__(0)

        if key == "last" or key == "L":
            return self.__getitem__(-1)

        if key == "reversed" or key == "R":
            res = []
            for x in super().__reversed__():
                res.append(x)
            return res

        if key == "size" or key == "S":
            return len(self)

        raise AttributeError()

exec(sys.stdin.read())
