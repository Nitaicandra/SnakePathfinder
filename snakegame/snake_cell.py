

import pygame,sys
import cell
import grid
import snake_cell

# the nodes of the linked list 
# i think every snake cell should have a refrence to the gridcell its on
# i plan on having the grid cell also have a refrence to any snake cell that on it so you can access both ways
class SnakeCell:
    current=None #cell
    next_cell=None #snakeCell
    previous_cell=None #snakeCell
    direction = None #string up down left right
    color = pygame.Color([34, 136, 76,1])
    
    def __init__(self,cell):
        self.current = cell
        cell.snake_cell=self
        return
    def move(self,direction):
        self.direction = direction
        
        self.current.snake_cell=None
        self.current.default_color()
        
        self.current=self.current.neighbors[direction]
        self.current.snake_cell = self
        self.current.color=self.color

        #move based on dir
        # go to previuos and move to current
        return
        




    