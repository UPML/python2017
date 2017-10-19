from copy import copy, deepcopy


class field:
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def updateAll(self):
        newData = deepcopy(self.data)
        self.update(2, newData)
        self.update(3, newData)
        self.data = newData

    def getNeigh(self, h, w, id):
        nNeigh = 0
        steps = [[0, 1], [0, -1],
                 [-1, -1], [-1, 0], [-1, 1],
                 [1, -1], [1, 0], [1, 1]]
        for move in steps:
            newH = h + move[0]
            newW = w + move[1]
            if (0 <= newH < self.height and 0 <= newW < self.width and
                    self.data[newH][newW] == id):
                nNeigh += 1
        return nNeigh

    def update(self, id, newData):
        for h, line in enumerate(self.data):
            for w, row in enumerate(line):
                if (self.data[h][w] == id and
                        (self.getNeigh(h, w, id) >= 4 or
                            self.getNeigh(h, w, id) <= 1)):
                    newData[h][w] = 0

                if self.data[h][w] == 0 and self.getNeigh(h, w, id) == 3:
                    newData[h][w] = id


steps = int(input())

sizes = [int(x) for x in input().split(" ")]
n = sizes[0]
m = sizes[1]
data = [[0 for x in range(m)] for y in range(n)]

for h in range(n):
    line = input().split(" ")
    for w in range(m):
        data[h][w] = int(line[w])

f = field(data)

for s in range(steps):
    f.updateAll()
for h in range(n):
    for w in range(m):
        print(f.data[h][w], end=" ")
    print("\n")
