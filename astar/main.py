import pygame
import sys

sys.path.append("snakegame")
from snakegame import Grid, Snake,AStar


# Window Dimensions
width = 800
height = width

# Grid Dimensions
cell_size = 20 #
grid_width = int(width / cell_size)
grid_height = int(height / cell_size)

#PYGAME INIT
pygame.init()
pygame.display.set_caption("Path Finding Snake Game")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#screen
surface = pygame.Surface((width, height))  # width and height of the surface
surface.fill((0, 0, 255)) #FILL WITH BLACK

# initialize game gird
game_grid = Grid(grid_width, grid_height, cell_size)

# initialize snake
snek = Snake(game_grid)
# pass snake to game grid
game_grid.snake=snek

# generate first fruit
game_grid.gen_fruit(snek)

# start the snake randomly on the gird
snek.StartRandomly(game_grid, grid_height, grid_width)

# string variable used to play a real game of snake
last_move = "None"

# variable used to tell wheather to play ordinary snake or debug snake
debug= True

# astar class
astar = AStar(game_grid,snek)

# toggles weather to path find or not
toggle_pathfinder=False

# main game loop loop until exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # player input used to toggle the pathfinding and movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                last_move = "none"
                debug= not debug
            if event.key == pygame.K_g:
                toggle_pathfinder= not toggle_pathfinder
            if event.key == pygame.K_a:
                if(debug==True):snek.move("left")
                elif not (last_move=="right"and snek.size>1): last_move = "left"
            if event.key == pygame.K_d:
                if(debug==True):snek.move("right")
                elif not (last_move=="left"and snek.size>1): last_move = "right"
            if event.key == pygame.K_w:
                if(debug==True):snek.move("up")
                elif not (last_move=="down"and snek.size>1): last_move = "up"
            if event.key == pygame.K_s:
                if(debug==True):snek.move("down")
                elif not (last_move == "up"and snek.size>1):last_move = "down"
            if event.key == pygame.K_SPACE:
                toggle_pathfinder= not toggle_pathfinder

    # if debug is false then snek will move the last direction evey frame
    if last_move != "None":
        snek.move(last_move)
        
    #default screen color
    screen.fill((175, 215, 70))
    screen.blit(surface, (0, 0)) 

    # reset the grid colors every frame
    game_grid.reset_colors()
    
    # if pathfinding is set run astar
    if(toggle_pathfinder==True):
        #runs the astar algorthm if the a* algorthm does not return a path 
        #randomly move until one is found or it gets stuck
        if not astar.a_star():
            snek.random_move()
        
        # export the csv data every frame
        astar.export_data_to_csv()
        astar.average()


    # draw grid cells and lines
    game_grid.draw_grid(surface)
    game_grid.draw_grid_lines(surface)
    
    # dsiplay grid
    pygame.display.update()
    
    #max frame rate for small graph visualizations
    clock.tick(70)#20


