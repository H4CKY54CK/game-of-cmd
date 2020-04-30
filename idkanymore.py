import os
import time
import numpy as np
from itertools import product
ROWS = 60
COLS = 30

FILLED = '\u2B1B'
EMPTY = '\u2B1C'

grid = np.array([EMPTY for i in range(COLS*ROWS)]).reshape(COLS,ROWS)

def glider(x,y):
    coords = []
    for a,b in product(range(3),range(3)):
        coords.append((0,0))
    coords[2] = (x+1,y+3)
    coords[3] = (x+2,y+1)
    coords[6] = (x+3,y+1)
    coords[7] = (x+3,y+2)
    coords[8] = (x+3,y+3)
    for i in coords:
        grid[i[0],i[1]] = FILLED


glider(20,50)


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
    cnt = list(b).count(FILLED)
    return cnt

# input("Hit enter to start.")
while True:
    kill = []
    revive = []
    os.system('cls' if os.name == 'nt' else 'clear')
    g = ''
    for i in grid:
        g += (''.join(list(i))+'\n')
    print(g)
    time.sleep(.1)
    for x,y in product(range(COLS), range(ROWS)):
        cnt = check(x,y)
        if grid[x,y] == FILLED:
            if cnt < 3 or cnt > 4:
                kill.append((x,y))
        elif grid[x,y] == EMPTY:
            if cnt == 3:
                revive.append((x,y))

    for i in kill:
        grid[i[0],i[1]] = EMPTY
    for i in revive:
        grid[i[0],i[1]] = FILLED
