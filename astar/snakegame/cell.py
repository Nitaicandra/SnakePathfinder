import random
import pygame, sys
import snake_cell


class Cell:

    def __init__(self, size,x,y):
        self.shape = pygame.Rect(0, 0, size, size)
        # Test Grid
        # self.color = pygame.Color([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 1])
        self.color = pygame.Color([34, 34, 34, 1])
        self.neighbors = {}
        
        self.x =x #position in grid
        self.y =y #y postion in grid index
        self.snake_cell = None # holds snake cell if present
        self.is_fruit=False
        return
        
    def reset_color(self):
        self.color=pygame.Color([34, 34, 34, 1])
    def is_snake(self):
        return self.snake_cell != None
    
    def is_unique(self):
        return self.is_snake()==True or self.is_fruit==True
