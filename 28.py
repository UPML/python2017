from PIL import Image
import numpy as np

# прочитаем изображение
bmpFile = Image.open("CFA.bmp")
image = 255 - np.array(bmpFile)
res = np.array([[[0] * 3] * bmpFile.size[0]] * bmpFile.size[1])
R = 0
G = 1
B = 2
print(image.shape)
print(res.shape)

# res = res[1300:1600, 1700:2500]
# image = image[1300:1600, 1700:2500]
res = res[1:10]
image = image[1:10]

print(image.shape)
print(res.shape)


class Position:
    x = -1
    y = -1

    def add(self, d):
        pos = Position()
        pos.x = self.x + d[0]
        pos.y = self.y + d[1]
        return pos


# вернет значение на данной позиции, если выходит за рамки, то вернет 0
def getValue(image, position):
    if (min(position.x, position.y) < 0 or
                position.x >= image.shape[1] or
                position.y >= image.shape[0]):
        return 0
    return image[position.y][position.x]


def getValueColor(image, position, collor):
    if (min(position.x, position.y) < 0 or
                position.x >= image.shape[1] or
                position.y >= image.shape[0]):
        return 0
    return image[position.y][position.x][collor]


def getDiff(image, position, first, second, left, right):
    return 2 * abs(getValue(image, position.add(first)) - getValue(image, position.add(second))) + \
           abs(getValue(image, position.add(left)) - getValue(image, position.add(right)))


# посчитать значение зеленого по нужному направлению
def getdiffGreen(image, position, d):
    return (3 * getValue(image, position.add(d[0])) + getValue(image, position.add(d[1])) + \
            getValue(image, position.add(d[2])) - getValue(image, position.add(d[3]))) // 4


# вернет значение зеленого для данной позиции
def getGreenValue(image, position):
    dW = getDiff(image, position, [0, 0], [-2, 0], [1, 0], [-1, 0])
    dS = getDiff(image, position, [0, 0], [0, 2], [0, -1], [0, 1])
    dN = getDiff(image, position, [0, 0], [0, -2], [0, 1], [0, -1])
    dE = getDiff(image, position, [0, 0], [2, 0], [-1, 0], [1, 0])
    minDiff = min([dN, dE, dW, dS])
    if (dN == minDiff):
        return getdiffGreen(image, position, [[0, -1], [0, 1], [0, 0], [0, -2]])
    if (dS == minDiff):
        return getdiffGreen(image, position, [[0, 1], [0, -1], [0, 0], [0, 2]])
    if (dW == minDiff):
        return getdiffGreen(image, position, [[-1, 0], [1, 0], [0, 0], [-2, 0]])
    if (dE == minDiff):
        return getdiffGreen(image, position, [[1, 0], [-1, 0], [0, 0], [2, 0]])


def hue_transit(L1, L2, L3, V1, V3):
    if (L1 < L2 < L3) or (L1 > L2 > L3):
        return V1 + (V3 - V1) * (L2 - L1) / (L3 - L1)
    else:
        return (V1 + V3) / 2 + (L2 - (L1 + L3) / 2) / 2


# в d - смещение по х, смещение по у, цвета отдельно в colors. цвета для пары сразу
def getCollorDiff(image, position, d, colors):
    return abs(
        getValueColor(image, position.add(d[0]), colors[0]) - getValueColor(image, position.add(d[1]), colors[0])) + \
           abs(getValueColor(image, position.add(d[2]), colors[1]) - getValueColor(image, position.add(d[3]),
                                                                                   colors[1])) + \
           abs(getValueColor(image, position.add(d[3]), colors[2]) - getValueColor(image, position.add(d[4]),
                                                                                   colors[2])) + \
           abs(getValueColor(image, position.add(d[0]), colors[3]) - getValueColor(image, position.add(d[3]),
                                                                                   colors[3])) + \
           abs(getValueColor(image, position.add(d[3]), colors[4]) - getValueColor(image, position.add(d[1]),
                                                                                   colors[4]))


def getBlue(image, position):
    dNE = getCollorDiff(image, position, [[1, -1], [-1, 1], [2, -2], [0, 0], [-2, 2]], [B, R, R, G, G])
    dNW = getCollorDiff(image, position, [[-1, -1], [1, 1], [-2, -2], [0, 0], [2, 2]], [B, R, R, G, G])
    if (dNE < dNW):
        return hue_transit(getValueColor(image, position.add([1, -1]), G),
                           getValueColor(image, position, G),
                           getValueColor(image, position.add([-1, 1]), G),
                           getValueColor(image, position.add([1, -1]), B),
                           getValueColor(image, position.add([-1, 1]), B))
    else:
        return hue_transit(getValueColor(image, position.add([-1, -1]), G),
                           getValueColor(image, position, G),
                           getValueColor(image, position.add([1, 1]), G),
                           getValueColor(image, position.add([-1, -1]), B),
                           getValueColor(image, position.add([1, 1]), B))


def getRed(image, position):
    dNE = getCollorDiff(image, position, [[1, -1], [-1, 1], [2, -2], [0, 0], [-2, 2]], [R, B, B, G, G])
    dNW = getCollorDiff(image, position, [[-1, -1], [1, 1], [-2, -2], [0, 0], [2, 2]], [R, B, B, G, G])
    if (dNE < dNW):
        return hue_transit(getValueColor(image, position.add([1, -1]), G),
                           getValueColor(image, position, G),
                           getValueColor(image, position.add([-1, 1]), G),
                           getValueColor(image, position.add([1, -1]), R),
                           getValueColor(image, position.add([-1, 1]), R))
    else:
        return hue_transit(getValueColor(image, position.add([-1, -1]), G),
                           getValueColor(image, position, G),
                           getValueColor(image, position.add([1, 1]), G),
                           getValueColor(image, position.add([-1, -1]), R),
                           getValueColor(image, position.add([1, 1]), R))


import scipy.misc


def isRed(w, h):
    return w % 2 == 0 and h % 2 == 0


def isBlue(w, h):
    return w % 2 == 1 and h % 2 == 1


def isGreen(w, h):
    return not isRed(w, h) and not isBlue(w, h)


def demosaicing(rawImage, imageRes):
    debugImage = np.array([[[0] * 3] * rawImage.shape[1]] * rawImage.shape[0])
    # перенесем начальные данные в новое изображение
    for h in range(rawImage.shape[0]):
        for w in range(rawImage.shape[1]):
            if isRed(w, h):
                imageRes[h][w][R] = rawImage[h][w]
            elif isBlue(w, h):
                imageRes[h][w][B] = rawImage[h][w]
            else:
                imageRes[h][w][G] = rawImage[h][w]

    # восстановим зеленый

    for h in range(rawImage.shape[0]):
        for w in range(rawImage.shape[1]):
            position = Position()
            position.x = w
            position.y = h
            if isRed(w, h) or isBlue(w, h):
                # print(getGreenValue(rawImage, position))
                imageRes[h][w][G] = getGreenValue(rawImage, position)

    # для изначально зеленых восстановим красный и синий
    for h in range(rawImage.shape[0]):
        for w in range(rawImage.shape[1]):
            position = Position()
            position.x = w
            position.y = h
            if isGreen(w, h):
                imageRes[h][w][B] = hue_transit(getValueColor(imageRes, position.add([-1, 0]), G),
                                                getValueColor(imageRes, position.add([0, 0]), G),
                                                getValueColor(imageRes, position.add([1, 0]), G),
                                                getValueColor(imageRes, position.add([-1, 0]), B),
                                                getValueColor(imageRes, position.add([1, 0]), B))
                imageRes[h][w][R] = hue_transit(getValueColor(imageRes, position.add([0, -1]), G),
                                                getValueColor(imageRes, position.add([0, 0]), G),
                                                getValueColor(imageRes, position.add([0, 1]), G),
                                                getValueColor(imageRes, position.add([0, -1]), R),
                                                getValueColor(imageRes, position.add([0, 1]), R))

    # для изначально красных восстановим синий, для изначально синих - красный
    for h in range(rawImage.shape[0]):
        for w in range(rawImage.shape[1]):
            position = Position()
            position.x = w
            position.y = h
            if isRed(w, h):
                imageRes[h][w][B] = getBlue(imageRes, position)
            if isBlue(w, h):
                imageRes[h][w][R] = getRed(imageRes, position)

    scipy.misc.imsave('outfile.bmp', imageRes)


demosaicing(image, res)
