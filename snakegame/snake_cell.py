

import pygame,sys
import cell
import grid
import snake_cell


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
            #this means that the cell hit a boundry
            if direction not in self.current.neighbors: 
                snake.die()
                return
            #if u run into the the tail the tail will move out of the way so u dont die but if u run iton a cell body that isnt the tail u will die
            if (self.current.neighbors[direction].snake_cell != snake.tail):
                if (self.current.neighbors[direction].is_snake()==True):
                    snake.die()
                    return

            if(snake.invert_direction(self.direction)==direction):
                if (self.previous_cell!=None):
                    print("test")
                    return
        
        head_tail_collision = False
        if(self==snake.tail and snake.tail.current==snake.head.current and snake.size>1):
            head_tail_collision = True
            print("collision")
        
        if head_tail_collision != True:
            self.current.snake_cell=None

        if head_tail_collision != True:
            self.current.reset_color()
        self.current=self.current.neighbors[direction]
        
        
        self.current.snake_cell = self
        
        
        self.current.color=self.color
        
        if(self.previous_cell!=None):
            self.previous_cell.move(self.direction,snake)
        self.direction = direction 
    
        return
        




    