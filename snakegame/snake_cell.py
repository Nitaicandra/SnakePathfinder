

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
            if direction not in self.current.neighbors: #this means that the cell hit a boundry
                snake.die()
                return
            if (self.current.neighbors[direction].snake_cell != snake.tail):
                if (self.current.neighbors[direction].isSnake()==True):
                 # if u move into a cell that contains a tail then u wont die because tail will move
                    snake.die()
                    return
            #print(snake.invert_direction(self.direction))
            
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
        
        if(self.previous_cell!=None):# recursivley calls move on previuos cells
            self.previous_cell.move(self.direction,snake)#move preivous cell in the direction the current cell is facing before changing movement
            self.direction = direction #update at end so that coreect tail movement
            #print(self.direction)
        
        #move based on dir
        # go to previuos and move to current
        return
        




    