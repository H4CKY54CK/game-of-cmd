import os
import time
import numpy as np
from itertools import product
ROWS = 17
COLS = 17
X = '\u2B1B'
Y = '\u2B1C'

grid = np.array([Y for i in range(ROWS*COLS)]).reshape(ROWS,COLS)

# Glider :P
grid[3,13] = X
grid[4,12] = X
grid[5,12] = X
grid[5,13] = X
grid[5,14] = X

def check(a,b):
    x = [a-1,a,a+1]
    y = [b-1,b,b+1]

    for e, i in enumerate(x):
        if i < 0:
            x[e] = 0
        elif i == len(grid[:,0]):
            x[e] = len(grid[:,0])-1

    for e, i in enumerate(y):
        if i < 0:
            y[e] = 0
        elif i == len(grid[0,:]):
            y[e] = len(grid[0,:])-1

    box = grid[np.ix_([x[0],x[1],x[2]],[y[0],y[1],y[2]])]
    b = box.ravel()
    cnt = list(b).count(X)
    return cnt

input("Hit enter to start.")
while True:
    kill = []
    revive = []
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in grid:
        print(''.join(list(i)))
    # print(grid)
    time.sleep(.1)
    for x,y in product(range(ROWS), range(COLS)):
        cnt = check(x,y)
        if grid[x,y] == X:
            if cnt < 3 or cnt > 4:
                kill.append((x,y))
        elif grid[x,y] == Y:
            if cnt == 3:
                revive.append((x,y))

    for i in kill:
        grid[i[0],i[1]] = Y
    for i in revive:
        grid[i[0],i[1]] = X
