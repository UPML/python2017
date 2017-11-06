class Iter(object):
    def __init__(self, *args):
        super().__init__()
        assert len(args) == 3
        self.index, self.to, self.step = args

    def __next__(self):
        if self.index >= self.to:
            raise StopIteration
        self.index += self.step
        return self.index - self.step


class Range:
    def __init__(self, *args):
        if len(args) == 1:
            self.from_ = 0
            self.to = args[0]
            self.step = 1
        if len(args) == 2:
            self.from_, self.to = args
            self.step = 1
        if len(args) == 3:
            self.from_, self.to, self.step = args

    def __iter__(self):
        return Iter(self.from_, self.to, self.step)

    def __repr__(self):
        return "range({}, {}, {})".format(self.from_, self.to, self.step)

    def __contains__(self, item):
        if item >= self.to or item < self.from_:
            return False
        return (item - self.from_) % self.step == 0

    def __getitem__(self, item):
        return self.from_ + self.step * item

    def __len__(self):
        return max(0, (self.to - self.from_) // self.step)

#
# print(list(Range(5)))
# print(len(Range(5)))
# print(len(Range(5, 10)))
