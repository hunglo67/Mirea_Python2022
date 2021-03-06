import numppy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import pylab


def distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_happy(data, humanx, humany, xn, yn, t):
    neighbours = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = humanx + i
            y = humany + j
            if x == xn:
                x = 0
            if y == yn:
                y = 0
            if data [humanx, humany] == data [x, y]:
                # or data [x, y] == 0
                neighbours [z] = 1
            z += 1
    my_favourite_neighbour = -1
    for i in range(8):
        if neighbours[i] == 1:
            my_favourite_neighbour += 1
    if float(my_favourite_neighbour/8) >= t:
        return True
    else:
        return False
    

print('Размер популяции: ')
population = 9000
#population = int(input())
print('Размер сетки: ')
x = y = 100
#x = int(input())
#y = int(input())
print('Население 1 группы агентов (в процентах): ')
xper = 30
#xper = int(input())
print('Население 2 группы агентов (в процентах): ')
yper = 70
#yper = int(input())
print('Пороговое значение толерантности: ')
t = 0.5
#t = float(input())
print('Количество шагов моделирования: ')
n = 500000
#n = int(input())
if population > x * y:
    print('Населения слишком много')
elif xper + yper > 100:
    print('Неверно введено соотношение в процентах')
elif t > 1:
    print('Пороговое значение толерантности > 1')
else:
    fig, ax = plt.subplots(ncols = 2)
    data = np.random.randint(1, 2, (y, x))
    empty = x * y - population
    i = 0
    happy = itHappy = []
    while i < empty:
        ex = int(random.uniform(0, x)) 
        ey = int(random.uniform(0, y)) 
        if data[ex, ey] == 1:
            data[ex, ey] = 0
        else:
            i -= 1
        i += 1
    anotherpopulation = int(yper / 100 * population)
    i = 0
    while i < anotherpopulation:
        ex = int(random.uniform(0, x)) 
        ey = int(random.uniform(0, y)) 
        if data[ex, ey] == 1:
            data[ex, ey] = 3
        else:
            i -= 1
        i += 1
    i = 0
    ax[0].imshow(data)
    #plt.pause(2)
    #plt.close('all')
    while i < n:
        isHappy = 0
        #if i % 1000 == 0:
        #    for j in range(x):
        #        for k in range(y):
        #            if data[j, k] != 0:
        #               if is_happy(data, j, k, x, y, t) is True:
        #                   isHappy +=1
        happy.append(float(isHappy / population * 100))
        itHappy.append(i)
        empty = False
        ex = int(random.uniform(0, x)) 
        ey = int(random.uniform(0, y))
        newex = newey = 0
        if is_happy(data, ex, ey, x, y, t) is False:
            while empty is False:
                newex = int(random.uniform(0, x)) 
                newey = int(random.uniform(0, y))
                if data[newex, newey] == 0:
                    empty = True
                    data[newex, newey] = data[ex, ey]
                    data[ex, ey] = 0
        i += 1
    ax[1].imshow(data)
    plt.show()
    plt.scatter(itHappy, happy)
    plt.show()
