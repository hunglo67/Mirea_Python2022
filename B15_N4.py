import math


def main(b, y, a, m, p):
    sum1 = 0
    for c in range(1, b + 1):
        sum1 += 65 * ((c ** 2) / 60 + y ** 3 + 77 * y) ** 7

    sum2 = 0
    for c in range(1, m + 1):
        for j in range(1, a + 1):
            sum2 += c ** 6 + (p ** 8) / 79 + 75 * j ** 5

    return sum1 - sum2
    


print('{:.2e}'.format(main(3, 0.97, 6, 4, -0.96)))
    
