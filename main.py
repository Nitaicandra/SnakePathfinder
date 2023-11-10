import pygame,sys

from snakegame import Cell,Grid,SnakeCell,Snake,UI,Window,Dijkstras,AStar


pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200)) #width and height of the surface
test_surface.fill((0,0,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))#fills the screen with a color
    screen.blit(test_surface,(200,250)) #places the test surface at the middle orgin top left by default
    pygame.display.update()
    clock.tick(60)#limits while loop to 60 fps # will replace with delta time at soem point
    
    