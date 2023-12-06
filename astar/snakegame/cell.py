import random
import pygame, sys
import snake_cell


class Cell:
    def __init__(self, size,x,y):
        #shape color and neighbors
        self.shape = pygame.Rect(0, 0, size, size)
        self.color = pygame.Color([34, 34, 34, 1])
        self.neighbors = {}
        
        self.x =x #position in grid
        self.y =y #y postion in grid index
        self.snake_cell = None # holds snake cell if present
        self.is_fruit=False # tells you weather the current cell is a fruit
        return
    
    # resets the color of a cell to default
    def reset_color(self):
        self.color=pygame.Color([34, 34, 34, 1])
        
    def is_snake(self):
        return self.snake_cell != None
    
    def is_unique(self):
        return self.is_snake()==True or self.is_fruit==True
