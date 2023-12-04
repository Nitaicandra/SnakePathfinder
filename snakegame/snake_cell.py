

import pygame,sys
import cell
import grid
import snake_cell

# the nodes of the linked list 
# i think every snake cell should have a refrence to the gridcell its on
# i plan on having the grid cell also have a refrence to any snake cell that on it so you can access both ways
class SnakeCell:
    
    def __init__(self,
    cell,
    next_cell=None,
    previous_cell=None,
    direction = "up",
    color = pygame.Color([34, 136, 76,1])
    
    ):
        self.current = cell
        self.next_cell=next_cell#snakeCell this is the cell leading to head
        self.previous_cell=previous_cell #snakeCell this is the cell leading to tail
        self.direction = direction #string up down left right the last direction the snake moved in the snake body will copy the current direction when moving
        self.color = color
        cell.snake_cell=self
        self.current.color=self.color
        return
        
        
        
    def move(self,direction,snake):
        if self == snake.head:
            if direction not in self.current.neighbors:
                snake.die()
                return
            
            if (self.current.neighbors[direction].snake_cell != None):
                if (self.current.neighbors[direction].snake_cell != snake.tail):
                    snake.die()
                return
            print(snake.invert_direction(self.direction))
            '''
            if(snake.invert_direction(self.direction)==direction):
                if (self.previous_cell!=None):
                    return
            '''
            
            
        # in special case of head colliding with tail you want to move tail before head
        
        self.current.snake_cell=None
        #if(self.current== snake.tail):
            #self.current.snake_cell=None
            
        self.current.default_color()
        self.current=self.current.neighbors[direction]
        
            
        self.current.snake_cell = self
        self.current.color=self.color
        
        if(self.previous_cell!=None):
            self.previous_cell.move(self.direction,snake)#move preivous cell in the direction the current cell is facing before changing movement
            self.direction = direction #update at end so that coreect tail movement
        
        #move based on dir
        # go to previuos and move to current
        return
        




    