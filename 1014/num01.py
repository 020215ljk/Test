import math


def quadratic(a, b, c):
    x1 = ((0-b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    x2 = ((0-b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    listnum = [x1, x2]
    return listnum


print(quadratic(3, 2, 1))


