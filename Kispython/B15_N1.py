import math


def main(y):
    A = 1 + y + y ** 2
    B = 25 * (y / 89 - y ** 3 - y ** 2) ** 7
    C = math.log(y ** 2) ** 2 + 48 * y ** 4
    return A / B - C


#print('{:.2e}'.format(main(-0.64)))
