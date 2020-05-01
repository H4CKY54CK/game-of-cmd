import os
import time
import numpy as np
from itertools import product
import pygame
from collections import deque


# 80 x 80 runs ok, but it really starts to slow down after that.
COLS = 60
ROWS = 60

# Used to be unicode values. Made it easy to switch it up on-the-fly.
FILLED = 1
EMPTY = 0

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Set color changer
d = deque((BLUE, RED, GREEN))
current_color = d[0]

# Grid cell size
WIDTH = 5
HEIGHT = 5
 
MARGIN = 1
 
class GameOfLife:

    def __init__(self):
        self.grid = np.array([EMPTY for i in range(ROWS*COLS)]).reshape(ROWS,COLS)

    # Counts neighbors. Now that I've explained what it does, this seems unnecessarily complicated.
    def check(self, a, b):
        x = [a-1,a,a+1]
        y = [b-1,b,b+1]

        for e, i in enumerate(x):
            if i < 0:
                x[e] = 0
            elif i == len(self.grid[:,0]):
                x[e] = len(self.grid[:,0])-1

        for e, i in enumerate(y):
            if i < 0:
                y[e] = 0
            elif i == len(self.grid[0,:]):
                y[e] = len(self.grid[0,:])-1

        box = self.grid[np.ix_([x[0],x[1],x[2]],[y[0],y[1],y[2]])]
        b = box.ravel()
        cnt = list(b).count(FILLED)
        return cnt

    # Reset all the values of the grid.
    def clear(self):
        for x,y in product(range(ROWS), range(COLS)):
            self.grid[x,y] = 0

    # Create a glider.
    def glider(self, x, y, direction=None):
        if direction is None:
            direction = 'right'
        g = np.array([EMPTY for i in range(9)]).reshape(3,3)
        g[0,1] = FILLED
        if direction == 'right':
            g[1,2] = FILLED
        if direction == 'left':
            g[1,0] = FILLED
        g[2,0] = FILLED
        g[2,1] = FILLED
        g[2,2] = FILLED
        # self.grid[x:x+3,y:y+3] = g
        for a,b in product(range(3),range(3)):
            if g[a,b] == 1:
                self.grid[x+a, y+b] = 1

    # Create a spaceship.
    def spaceship(self, x, y):
        g = np.array([EMPTY for i in range(20)]).reshape(4,5)
        g[0,0] = FILLED
        g[0,3] = FILLED
        g[1,4] = FILLED
        g[2,0] = FILLED
        g[2,4] = FILLED
        g[3,1:5] = FILLED
        # self.grid[x:x+4, y:y+5] = g
        for a,b in product(range(4),range(5)):
            if g[a,b] == 1:
                self.grid[x+a, y+b] = 1

    # Create a glider gun.
    def glider_gun(self, x, y):
        g = np.array([int(i) for i in '000000000000000000000000100000000000000000000000000000000010100000000000000000000000110000001100000000000011000000000001000100001100000000000011110000000010000010001100000000000000110000000010001011000010100000000000000000000010000010000000100000000000000000000001000100000000000000000000000000000000110000000000000000000000']).reshape(9,36)
        # self.grid[x:x+9, y:y+36] = g
        for a,b in product(range(9),range(36)):
            if g[a,b] == 1:
                self.grid[x+a, y+b] = 1

    # Update the grid, one step.
    def step(self):
        new = self.grid.copy()
        for x,y in product(range(ROWS), range(COLS)):
            cnt = self.check(x,y)
            if self.grid[x,y] == FILLED:
                if cnt < 3 or cnt > 4:
                    new[x,y] = EMPTY
            elif self.grid[x,y] == EMPTY:
                if cnt == 3:
                    new[x,y] = FILLED
        self.grid = new

        # Haven't figured out which is faster. Copying the grid, or using a list.

        # kill = []
        # revive = []
        # for i in kill:
        #     self.grid[i[0],i[1]] = EMPTY
        # for i in revive:
        #     self.grid[i[0],i[1]] = FILLED




grid = GameOfLife()
pygame.init()
 
screen = pygame.display.set_mode((360,360))
 
pygame.display.set_caption("Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Doesn't seem like we need it?
# clock = pygame.time.Clock()

# Other pre-defaults
paused = True
leftDragFlag = False
rightDragFlag = False

while not done:
    pos = pygame.mouse.get_pos()
    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)
    if paused is None:
        paused = True
    for event in pygame.event.get():
        # User clicks 'X'
        if event.type == pygame.QUIT:
            # Flag that says whether to close or not.
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                leftDragFlag = True
            elif event.button == 3:
                rightDragFlag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            leftDragFlag = False
            rightDragFlag = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p:
                paused = True if not paused else False
            if event.key == pygame.K_r:
                grid.clear()
                paused = None
            if event.key == pygame.K_g:
                try:
                    grid.glider(row, column)
                except:
                    pass
            if event.key == pygame.K_s:
                try:
                    grid.spaceship(row, column)
                except:
                    pass
            if event.key == pygame.K_u:
                try:
                    grid.glider_gun(row, column)
                except:
                    pass
            if event.key == pygame.K_c:
                d.rotate()
                current_color = d[0]

    if leftDragFlag:
        grid.grid[row][column] = 1

    if rightDragFlag:
        grid.grid[row][column] = 0

    screen.fill(BLACK)

    for row in range(len(grid.grid[0])):
        for column in range(len(grid.grid[0])):
            color = WHITE
            if grid.grid[row][column] == 1:
                color = current_color
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Not entirely sure why I need this if I have my own updating function.
    # clock.tick(60)

    if not paused:
        grid.step()
    
    pygame.display.flip()
pygame.quit()


