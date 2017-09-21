import queue


class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell:
    def __init__(self, pos, c):
        super().__init__()
        self.pos = pos
        self.alreadySeen = False
        self.symbol = c

    pos = Position(0, 0)
    alreadySeen = False
    symbol = ""


def readField():
    sizes = input().split(" ")
    height = int(sizes[0])
    width = int(sizes[1])
    dogPos = Position
    field = [[Cell for j in range(width)] for i in range(height)]
    for h in range(height):
        line = input()
        for w in range(width):
            field[h][w] = Cell(Position(w, h), line[w])
            if line[w] == '@':
                dogPos = Position(h, w)

    return field, dogPos


diff = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def step(field, pos):
    newStep = []
    for d in diff:
        newPos = Position(pos.x + d[0], pos.y + d[1])
        if field[newPos.x][newPos.y].symbol != "#" and \
                not field[newPos.x][newPos.y].alreadySeen:
            newStep.append(newPos)
    return newStep


que = queue.Queue()

room, dog = readField()
feed = 0
que.put(dog)
while not que.empty():
    pos = que.get()
    for p in step(room, pos):
        room[p.x][p.y].alreadySeen = True
        if room[p.x][p.y].symbol == "*":
            feed += 1
        que.put(p)

print(feed)
