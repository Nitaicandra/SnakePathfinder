import pygame, sys
import cell
import grid
import random
from snake_cell import SnakeCell
from enum import Enum

class Snake:
    #initialize the snake it holds a head and tail and a refrence to grid
    # the hea and tail hold snake cells
    def __init__(self,grid=None):
        self.head=None
        self.tail=None
        self.size=1
        self.grid= grid
        self.dead = False
    
    # start at a specific position
    def StartAt(self, game_grid, x, y):
        self.head =SnakeCell(game_grid.cells[y][x],color = pygame.Color([34, 100, 76,1]))
        self.tail=self.head
        return
    
    # start at a random position
    def StartRandomly(self, game_grid, grid_height, grid_width):
        random_y =random.randint(0, grid_height - 1)
        random_x =random.randint(0, grid_width - 1)
        self.head =SnakeCell(game_grid.cells[random_y][random_x],color = pygame.Color([34, 100, 76,1]))
        self.tail=self.head
        return
        
    # utility function used to get the opposite direction as input
    def invert_direction(self,direction):
        if direction=="up":
            return "down"
        elif direction=="down":
            return "up"
        elif direction=="left":
            return "right"
        elif direction=="right":
            return "left"
        
    # adds a snake cell to the tail of teh snake
    # snake gets appended to the cell of the opposite driection the tail is facing
    def append(self):
        self.size+=1
        if(self.invert_direction(self.tail.direction)in self.tail.current.neighbors):
            tail_neighbor =self.tail.current.neighbors[self.invert_direction(self.tail.direction)]
        
        self.tail.previous_cell = SnakeCell(
        tail_neighbor,
        direction =self.tail.direction
        ) 
        self.tail.previous_cell.next_cell = self.tail
        self.tail = self.tail.previous_cell
    
    # calls the move function on the snake head which recurses through the snake body
    def move(self,direction):
        self.head.move(direction,self)
        self.eat()
    
    # checks weather a fruit is in the same spot as the head if it is then generate a new fruit and increase the size of the snake
    def eat(self):
        if self.head.current.is_fruit==True:
            self.append()
            self.head.current.is_fruit=False
            self.grid.gen_fruit(self)
    
    # set the snake to dead and print snake is dead
    def die(self):
        self.dead = True
        #print(self.dead)
        print("snake is dead")
        return
    
    # randomly move in one of the cardinal directions as long as that cell is not a snake cell
    def random_move(self):
        selection =random.choice(list(self.head.current.neighbors.keys()))
        if(self.head.current.neighbors[selection].is_snake()==False):
            self.head.move(selection,self)
            self.eat()
