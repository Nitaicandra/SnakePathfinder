import pygame
import sys

sys.path.append("snakegame")
from snakegame import Grid, Snake


# Window Dimensions
width = 800
height = width

# Grid Dimensions
cell_size = 20
grid_width = int(width / cell_size)
grid_height = int(height / cell_size)

#PYGAME INIT
pygame.init()
pygame.display.set_caption("Path Finding Snake Game")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

surface = pygame.Surface((width, height))  # width and height of the surface
surface.fill((0, 0, 255)) #FILL WITH BLACK

game_grid = Grid(grid_width, grid_height, cell_size)
game_grid.cells[0][1].color = pygame.Color([255, 0, 255, 1])
 
snek = Snake()
snek.StartRandomly(game_grid, grid_height, grid_width)

debug= True
last_move = "None"
while True:

    # Tick Movement
    # snek.move(0, snek.moving_direction, snek.snake_cells[0])
    # Key input temporary to test snake movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if(debug==True):
                if event.key == pygame.K_a:
                    print("left")
                    snek.move("left")
                if event.key == pygame.K_d:
                    print("right")
                    snek.move("right")
                if event.key == pygame.K_w:
                    print("up")
                    snek.move("up")
                if event.key == pygame.K_s:
                    print("down")
                    snek.move("down")
                if event.key == pygame.K_SPACE:
                    print("append")
                    snek.append()
            else:
                if event.key == pygame.K_a:
                    print("left")
                    last_move = "left"
                if event.key == pygame.K_d:
                    print("right")
                    last_move = "right"
                if event.key == pygame.K_w:
                    print("up")
                    last_move="up"
                if event.key == pygame.K_s:
                    print("down")
                    last_move="down"
                if event.key == pygame.K_SPACE:
                    print("append")
                    snek.append()
                    
    if last_move != "None":
        snek.move(last_move)
        

    screen.fill((175, 215, 70))  # fills the screen with a color
    screen.blit(surface, (0, 0))  # places the test surface at the middle origin top left by default

    #game_grid.snake_checker()
    game_grid.draw_grid(surface)
    game_grid.draw_grid_lines(surface)
    
    pygame.display.update()
    clock.tick(20)  # limits while loop to 20
