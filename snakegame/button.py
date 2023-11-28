import pygame,sys
class Button():
    pygame.init()
    
    
    #font=pygame.font.SysFont('Georgia',40, bold=True)
    #text=font.render('Quit', True, 'white')
    #button_rect = pygame.Rect(200,200,110,60)
    

    def __init__(self,
        screen,
        font=pygame.font.SysFont('arialblack',40),
        x_pos=0,
        y_pos=0,
        width=110,
        height=60,
        text_string='Quit',
        text_color=(255,255,255),
        button_color=(180,180,180),
        hover_color=(110,110,110),
        clicked_color=0,
        
        #height width
        
        function=None):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.clicked_color =clicked_color
        self.font=font
        self.function=function
        self.screen =screen
        self.button_rect=pygame.Rect(x_pos,y_pos,width,height)
        
        self.text =font.render(text_string, True, text_color)
        #return

        
    def handle_click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                #function()
                pygame.quit()
    
    def handle_hover(self):
        a,b = pygame.mouse.get_pos()
        if self.button_rect.x <= a <= self.button_rect.x +110 and self.button_rect.y<=b <=self.button_rect.y+60:
                pygame.draw.rect(self.screen,self.button_color,self.button_rect)
        else:
            pygame.draw.rect(self.screen,self.hover_color,self.button_rect)
    def draw(self):
        self.screen.blit(self.text,(self.button_rect.x+5, self.button_rect.y+5))
    

	