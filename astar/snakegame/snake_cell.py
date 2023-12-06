

import pygame,sys
import cell
import grid
import snake_cell

#each cell of the main snake
class SnakeCell:
    
    #initialize snake
    def __init__(self,
    cell,
    next_cell=None,
    previous_cell=None,
    direction = "up",
    color = pygame.Color([34, 136, 76,1])
    ):
        self.current = cell # refrence to the grid cell the snake cell is on
        self.next_cell=next_cell#snakeCell this is the cell leading to head
        self.previous_cell=previous_cell #snakeCell this is the cell leading to tail
        self.direction = direction #string up down left right the last direction the snake moved in the snake body will copy the current direction when moving
        self.current.snake_cell=self #updates the cell thats curently being refrence to hold the current snake
        self.color = color # color of the snake 
        self.current.color=self.color # sets the colorof the cell the snake is refrenceing to that color
        return
        
    # move the snake recursivley, first move the head and check death conditions, then move body
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
            # ensures the head cannot inver and move into itself
            if(snake.invert_direction(self.direction)==direction):
                if (self.previous_cell!=None):
                    print("test")
                    return
        
        #checks if a tail head collision occurs if it does then change logic
        head_tail_collision = False
        if(self==snake.tail and snake.tail.current==snake.head.current and snake.size>1):
            head_tail_collision = True
            print("collision")
        
        # for every case except tail collision set the current cell to no refrence a snake 
        # and reset its color
        if head_tail_collision != True:
            self.current.snake_cell=None
            self.current.reset_color()
        
        #set the current snake to the neighbor that is in the direction of pased in by the move function
        self.current=self.current.neighbors[direction]
        
        #set the new current grid cell to a refrence to this cell
        self.current.snake_cell = self
        
        #set that grid to display the snake color
        self.current.color=self.color
        
        # recurese until their is not previous cell in which case you are the tail
        if(self.previous_cell!=None):
            #moves snake body in the direction of the snake was originally pointing when it called it
            self.previous_cell.move(self.direction,snake)
        
        # lastley update teh direction each cell of the snake is pointing tothe direction passed by it when called 
        self.direction = direction 
        return
        




    