import pygame,sys
sys.path.append("snakegame")
from snakegame import Cell,Grid,SnakeCell,Snake,Window,Dijkstras,AStar,Button
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('SnakePathfinder')
clock = pygame.time.Clock()





font = pygame.font.SysFont('Georgia',40, bold=True)
text = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,110,60)

button = Button(screen)






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
            
        button.handle_click(event)
        
    button.handle_hover()
    button.draw()

            
            
    
    
    
    #draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)



    pygame.display.update()
    clock.tick(60)#limits while loop to 60 fps # will replace with delta time at soem point
    
pygame.quit()