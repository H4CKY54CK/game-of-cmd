import os
import time
import numpy as np
from itertools import product
COLS = 60
ROWS = 60

FILLED = '\u2B1B'
EMPTY = '\u2B1C'

grid = np.array([EMPTY for i in range(ROWS*COLS)]).reshape(ROWS,COLS)

def glider(x, y, direction=None):
    if direction is None:
        direciton = 'right'
    g = np.array([EMPTY for i in range(9)]).reshape(3,3)
    g[0,1] = FILLED
    if direction == 'right':
        g[1,2] = FILLED
    if direction == 'left':
        g[1,0] = FILLED
    g[2,0] = FILLED
    g[2,1] = FILLED
    g[2,2] = FILLED
    grid[x:x+3,y:y+3] = g
glider(20,50, 'left')
glider(20,20, 'right')
glider(40,20, 'right')
glider(40,50, 'left')


def spaceship(x,y):
    g = np.array([EMPTY for i in range(20)]).reshape(4,5)
    g[0,0] = FILLED
    g[0,3] = FILLED
    g[1,4] = FILLED
    g[2,0] = FILLED
    g[2,4] = FILLED
    g[3,1:5] = FILLED
    grid[x:x+4, y:y+5] = g
spaceship(5,5)



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

input("Hit enter to start.")
while True:
    kill = []
    revive = []
    os.system('cls' if os.name == 'nt' else 'clear')
    g = ''
    for i in grid:
        g += (''.join(list(i))+'\n')
    print(g)
    time.sleep(.05)
    for x,y in product(range(ROWS), range(COLS)):
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
