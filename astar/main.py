import pygame
import sys

sys.path.append("snakegame")
from snakegame import Grid, Snake,AStar,Dijkstras, dijkstras


# Window Dimensions
width = 800
height = width

# Grid Dimensions
cell_size = 2 #
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
#game_grid.cells[0][0].color = pygame.Color([255, 0, 255, 1])
#game_grid.cells[5][5].color = pygame.Color([255, 0, 255, 1])
 
snek = Snake(game_grid)
game_grid.snake=snek
game_grid.gen_fruit(snek)
snek.StartRandomly(game_grid, grid_height, grid_width)

last_move = "None"

debug= True

astar = AStar(game_grid,snek)
#dijkstra = Dijkstras(game_grid,snek)

toggle_pathfinder=False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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

                    
    if last_move != "None":
        snek.move(last_move)
        

    screen.fill((175, 215, 70))
    screen.blit(surface, (0, 0)) 


    game_grid.reset_colors()
    if(toggle_pathfinder==True):
        
        if(len(sys.argv)>1 and sys.argv[1]=="m"):
            pass
        elif(len(sys.argv)>1 and sys.argv[1]=="s"):
            if not astar.a_star():
                snek.random_move()
        elif(len(sys.argv)>1 and sys.argv[1]=="d"):
            #if not dijkstra.dijkstra():
                #snek.random_move()
            pass
        else:
            if not astar.a_star():
                snek.random_move()
            #if not dijkstra.dijkstra():
                #snek.random_move()
        astar.export_data_to_csv()
        astar.average()
        #dijkstra.export_data_to_csv()
        #dijkstra.average()


    game_grid.draw_grid(surface)
    
    game_grid.draw_grid_lines(surface)
    
    pygame.display.update()
    
    
    clock.tick(20)#20


