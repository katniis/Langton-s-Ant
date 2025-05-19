# Langton's Ant Simulation
# -------------------------
# Langton's Ant is a two-dimensional Turing machine invented by Chris Langton in 1986.
# It consists of a virtual "ant" that moves on a grid of black and white cells.
# 
# Rules:
# 1. At a white square, turn 90° right, flip the color of the square, move forward.
# 2. At a black square, turn 90° left, flip the color of the square, move forward.
# 
# Despite its simplicity, Langton's Ant produces complex, emergent behavior over time,
# including a predictable "highway" pattern after many steps.

import pygame
import sys

window_size = (width, height) = 1080 , 720
square_size = 10

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Langton's Ant")
clock  = pygame.time.Clock()

# Direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTION_VECTOR = {
    UP: (0, -1),
    RIGHT: (1, 0),
    DOWN: (0, 1),
    LEFT: (-1, 0)
}

# Start in the center of the screen (in grid cells, not pixels)
column = window_size[0] // square_size
row = window_size[1] // square_size
ant_pos = (column // 2, row // 2)
ant_dir = UP

grid = {}

def turn_right(direction):
    return (direction + 1) % 4

def turn_left(direction):
    return (direction - 1) % 4

def flip_color(grid, pos):
    if pos in grid:
        del grid[pos]  # Turn black → white
    else:
        grid[pos] = True  # Turn white → black

def move_forward(pos, direction):
    dx, dy = DIRECTION_VECTOR[direction]
    x, y = pos
    return (x + dx, y + dy)

def ant_step(pos, direction, grid):
    if pos in grid:
        direction = turn_left(direction)
    else:
        direction = turn_right(direction)

    flip_color(grid, pos)
    pos = move_forward(pos, direction)
    
    return pos, direction

ant_pos, ant_dir = ant_step(ant_pos, ant_dir, grid)

def draw(screen, grid, ant_pos, square_size):
    screen.fill((255, 255, 255))  # Fill background with white

    # Draw black cells
    for (x, y) in grid:
        rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
        pygame.draw.rect(screen, (0, 0, 0), rect)

    # Draw the ant in red
    ax, ay = ant_pos
    ant_rect = pygame.Rect(ax * square_size, ay * square_size, square_size, square_size)
    pygame.draw.rect(screen, (255, 0, 0), ant_rect)

    pygame.display.flip()

ant_pos, ant_dir = ant_step(ant_pos, ant_dir, grid)
draw(screen, grid, ant_pos, square_size)

clock.tick(60)  # Adjust FPS as needed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform one step of the simulation
    ant_pos, ant_dir = ant_step(ant_pos, ant_dir, grid)

    # Draw the grid and the ant
    draw(screen, grid, ant_pos, square_size)

    # Control the update speed (frames per second)
    clock.tick(60) 

pygame.quit()
sys.exit()
