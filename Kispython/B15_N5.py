import math


def main(n):
    if n == 0:
        return 0.72
    elif n == 1:
        return 0.13
    else:
        return main(n - 1) ** 3 + main(n - 2) ** 2


print('{:.2e}'.format(main(9)))
    
