

import pygame,sys
import cell
import grid
import snake_cell

# the nodes of the linked list 
# i think every snake cell should have a refrence to the gridcell its on
# i plan on having the grid cell also have a refrence to any snake cell that on it so you can access both ways
class SnakeCell:
    current=None #cell
    nextCell=None #snakeCell
    previousCell=None #snakeCell
    
    def __init__(self):
        return




    