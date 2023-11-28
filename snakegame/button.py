import pygame,sys
class Button():
    pygame.init()
    
    
    #font=pygame.font.SysFont('Georgia',40, bold=True)
    #text=font.render('Quit', True, 'white')
    #button_rect = pygame.Rect(200,200,110,60)
    

    def __init__(self,
        screen,
        font=pygame.font.SysFont('Georgia',40, bold=True),
        x_pos=0,
        y_pos=0,
        width=0,
        height=0,
        text_string='Quit',
        color=0,
        hover_color=0,
        clicked_color=0,
        button_rect=pygame.Rect(200,200,110,60),
        
        function=0):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.clicked_color =clicked_color
        self.font=font
        self.function=function
        self.screen =screen
        self.button_rect= button_rect
        
        self.text =font.render(text_string, True, 'white')
        #return

        
    def set(self):
        self.font = pygame.font.SysFont('Georgia',40, bold=True)
        self.text = self.font.render('Quit', True, 'white')
        self.button_rect = pygame.Rect(200,200,110,60)
        return
        
    def handle_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                pygame.quit()
    
    def handle_hover(self):
        a,b = pygame.mouse.get_pos()
        if self.button_rect.x <= a <= self.button_rect.x +110 and self.button_rect.y<=b <=self.button_rect.y+60:
                pygame.draw.rect(self.screen,(180,180,180),self.button_rect)
        else:
            pygame.draw.rect(self.screen,(110,110,110),self.button_rect)
    def draw(self):
        self.screen.blit(self.text,(self.button_rect.x+5, self.button_rect.y+5))
    

	