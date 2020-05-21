import pygame
import numpy as np
from itertools import product

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 1
HEIGHT = 1

# This sets the margin between each cell
MARGIN = 0

GX = 200
GY = 200

grid = np.random.randint(2, size=(GX, GY))
# grid = np.zeros((GX,GY))


grid[50:53,50:53] = [[0,1,0],[0,0,1],[1,1,1]]

def step(grid):
    alive = []
    dead = []
    for (x,y), v in np.ndenumerate(grid):
        z = np.count_nonzero(grid[x-1:x+2,y-1:y+2])
        if v:
            if z < 3 or z > 4:
                dead.append((x,y))
        else:
            if z == 3:
                alive.append((x,y))
    for i in set(alive):
        grid[i[0],i[1]] = 1
    for i in set(dead):
        grid[i[0],i[1]] = 0
    return grid


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [600, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# For delaying the display until I hit record.
# import os
# os.system('pause')

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1

    # Set the screen background
    screen.fill(BLACK)


    # Draw the grid
    for x,y in product(range(GX),range(GY)):
        color = BLACK
        if grid[x,y] == 1:
            color = GREEN
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * y + MARGIN,
                          (MARGIN + HEIGHT) * x + MARGIN,
                          WIDTH,
                          HEIGHT])
    grid = step(grid)
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()