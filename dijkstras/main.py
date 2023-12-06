import random
import pygame
import sys
import queue

sys.path.append("snakegame")
from snakegame import Grid, dijkstras, cell

# Window Dimensions
width = 800
height = 800

# Grid Dimensions
cell_size = 10
grid_width = int(width / cell_size)
grid_height = int(height / cell_size)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
sys.setrecursionlimit(10000)
# Draw the surface
surface = pygame.Surface((width, height))  # width and height of the surface
surface.fill((0, 0, 255))

# Initialize the grid and the snake
game_grid = Grid(grid_width, grid_height, cell_size)

dijk = dijkstras.Dijkstras()

# Add distances to all cells using Manhattan Distance
game_grid.gen_distances()

# Queue for executing each move per tick
movement_queue = queue.Queue()

# Track if the cell pauses due to Dijkstra failing
curr_tick = game_grid.snake.snake_cells[0]
prev_tick = game_grid.snake.snake_cells[0]
start = True

while True:
    # Keep moving the snake for each request made
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    if not movement_queue.empty():
        prev_tick = curr_tick
        game_grid.snake.move(0, movement_queue.get(), game_grid.snake.snake_cells[0])
        curr_tick = game_grid.snake.snake_cells[0]
    # Calculate the path to fruit, store for traversing later
    dijk.calculatePath(game_grid.snake, game_grid)
    path = dijk.getFoodPath(game_grid.snake.snake_cells[0], game_grid.fruit)
    dijk.export_data_to_csv()
    dijk.average()

# Traverse the path and insert the cell to queue
    for cell in path:
        if cell in list(game_grid.snake.snake_cells[0].neighbors.values()):
            if list(game_grid.snake.snake_cells[0].neighbors.keys())[
                list(game_grid.snake.snake_cells[0].neighbors.values()).index(cell)]:
                movement_queue.put(list(game_grid.snake.snake_cells[0].neighbors.keys())[
                                       list(game_grid.snake.snake_cells[0].neighbors.values()).index(cell)])
    # If dijkstra fails, move to a random neighbor to run the algorithm again
    if curr_tick == prev_tick and start == False:
        game_grid.snake.move(0, (random.choice(list(game_grid.snake.snake_cells[0].neighbors.keys()))), game_grid.snake.snake_cells[0])
    start = False
    screen.fill((175, 215, 70))  # fills the screen with a color
    screen.blit(surface, (0, 0))  # places the test surface at the middle origin top left by default


    game_grid.draw_grid(surface)
    pygame.display.update()
    clock.tick(20)  # limits while loop to 60 fps # will replace with delta time at some point
