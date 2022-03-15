import math


def main(x):
    if x < 151:
        return 80 * x ** 3 - (x - 82 * x ** 2) ** 7
    elif 151 <= x < 208:
        return x ** 3 - 55 * x ** 6
    elif 208 <= x <= 249:
        return (x / 6 + 42 + 36 * x ** 3) ** 4
    else:
        return 70 * (0.02 + 38 * x + x ** 2) ** 2 + x + x ** 7 /72
    
   

print('{:.2e}'.format(main(124)))
    
