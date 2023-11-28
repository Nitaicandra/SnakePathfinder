import pygame,sys
sys.path.append("snakegame")
from snakegame import Cell,Grid,SnakeCell,Snake,Window,Dijkstras,AStar
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('SnakePathfinder')
clock = pygame.time.Clock()




font = pygame.font.SysFont('Georgia',40, bold=True)
surf = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,110,60)






#LOOOOOOOOOOOOOOOOOOOOP
run = True
while run:
    screen.fill((52,78,91))#fills the screen with a color
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                print("Pause")
                game_paused=True
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
        
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x +110 and button.y<=b <=button.y+60:
            pygame.draw.rect(screen,(180,180,180),button)
    else:
        pygame.draw.rect(screen,(110,110,110),button)
    screen.blit(surf,(button.x+5, button.y+5))
            
            
    
    
    
    #draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)



    pygame.display.update()
    clock.tick(60)#limits while loop to 60 fps # will replace with delta time at soem point
    
pygame.quit()