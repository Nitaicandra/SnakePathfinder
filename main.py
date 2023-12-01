import pygame
import sys

sys.path.append("snakegame")
from snakegame import Grid, Snake

# Window Dimensions
width = 800
height = 800
# Grid Dimensions
cell_size = 50
grid_width = int(width / cell_size)
grid_height = int(height / cell_size)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

surface = pygame.Surface((width, height))  # width and height of the surface
surface.fill((0, 0, 255))

game_grid = Grid(grid_width, grid_height, cell_size)
snek = Snake(game_grid, grid_height, grid_width)

fruit = game_grid.gen_fruit(snek)
while True:
    # Tick Movement
    # snek.move(0, snek.moving_direction, snek.snake_cells[0])aa
    # Key input temporary to test snake movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("left")
                snek.move(0, "left",  snek.snake_cells[0], fruit, game_grid)
                if "left" in snek.snake_cells[0].neighbors and fruit == snek.snake_cells[0]:
                    snek.append()
                    fruit = game_grid.gen_fruit(snek)
                if "left" not in snek.snake_cells[0].neighbors:
                    snek.kill()
                    snek = Snake(game_grid, grid_height, grid_width)
                    fruit.color = pygame.Color([0, 0, 0, 1])
                    fruit = game_grid.gen_fruit(snek)
            if event.key == pygame.K_d:
                print("right")
                snek.move(0, "right", snek.snake_cells[0], fruit, game_grid)
                if "right" in snek.snake_cells[0].neighbors and fruit == snek.snake_cells[0]:
                    snek.append()
                    fruit = game_grid.gen_fruit(snek)
                if "right" not in snek.snake_cells[0].neighbors:
                    snek.kill()
                    snek = Snake(game_grid, grid_height, grid_width)
                    fruit.color = pygame.Color([0, 0, 0, 1])
                    fruit = game_grid.gen_fruit(snek)
            if event.key == pygame.K_w:
                print("up")
                snek.move(0, "up",  snek.snake_cells[0], fruit, game_grid)
                if "up" in snek.snake_cells[0].neighbors and fruit == snek.snake_cells[0]:
                    snek.append()
                    fruit = game_grid.gen_fruit(snek)
                if "up" not in snek.snake_cells[0].neighbors:
                    snek.kill()
                    snek = Snake(game_grid, grid_height, grid_width)
                    fruit.color = pygame.Color([0, 0, 0, 1])
                    fruit = game_grid.gen_fruit(snek)
            if event.key == pygame.K_s:
                print("down")
                snek.move(0, "down", snek.snake_cells[0], fruit, game_grid)
                if "down" in snek.snake_cells[0].neighbors and fruit == snek.snake_cells[0]:
                    snek.append()
                    fruit = game_grid.gen_fruit(snek)
                if "down" not in snek.snake_cells[0].neighbors:
                    snek.kill()
                    snek = Snake(game_grid, grid_height, grid_width)
                    fruit.color = pygame.Color([0, 0, 0, 1])
                    fruit = game_grid.gen_fruit(snek)
            if event.key == pygame.K_SPACE:
                print("append")
                snek.append()

    screen.fill((175, 215, 70))  # fills the screen with a color
    screen.blit(surface, (0, 0))  # places the test surface at the middle origin top left by default

    game_grid.draw_grid(surface)
    pygame.display.update()
    clock.tick(60)  # limits while loop to 60 fps # will replace with delta time at some point
