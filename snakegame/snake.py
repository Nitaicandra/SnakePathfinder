import pygame, sys
import cell
import grid
import random
import snake_cell
from enum import Enum


# probably just a head and tail to snake cells # form a sort of linked list
class Snake:

    def __init__(self):
        self.head=None
        self.tail=None
    #'''
    def StartAt(self, game_grid, x, y):
        self.head =snake_cell(game_grid[y][x])
        
        return
    
    def StartRandomly(self, game_grid, grid_height, grid_width):
            random_y =random.randint(0, grid_height - 1)
            random_x =random.randint(0, grid_width - 1)
            self.head =snake_cell(game_grid[random_y][random_x])
            self.tail=self.head
            self.dir = None
            return
    def append(self):
        self.tail
    #get dir boolean?

    #'''
    '''
    snake_cells = list()
    moving_direction = "left"
    tail_direction = "right"

    def __init__(self, game_grid, grid_height, grid_width):
        self.snake_cells.append(game_grid.cells[random.randint(0, grid_height - 1)][random.randint(0, grid_width - 1)])
        self.snake_cells[0].color = pygame.Color([34, 136, 76, 1])
        self.tail = self.snake_cells[len(self.snake_cells) - 1]
        self.prev_cell = self.snake_cells[0]
        return

    # Move the snake by changing the colors of the grid and tracking those cells
    # Need to complete movement for cells appended to the snake (must follow the previous moved cell until the tail)
    def move(self, cell_index, direction, cell):
        match direction:
            case "left":
                if "left" in self.snake_cells[cell_index].neighbors:
                    self.moving_direction = "left"
                    self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                    self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["left"]
                    if len(self.snake_cells) == 1:
                        self.tail = self.snake_cells[cell_index]
                        self.tail_direction = "right"
                    self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
            case "right":
                if "right" in self.snake_cells[cell_index].neighbors:
                    self.moving_direction = "right"
                    self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                    self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["right"]
                    if len(self.snake_cells) == 1:
                        self.tail = self.snake_cells[cell_index]
                        self.tail_direction = "left"
                    self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
            case "up":
                if "up" in self.snake_cells[cell_index].neighbors:
                    self.moving_direction = "up"
                    self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                    self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["up"]
                    if len(self.snake_cells) == 1:
                        self.tail = self.snake_cells[cell_index]
                        self.tail_direction = "down"
                    self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
            case "down":
                if "down" in self.snake_cells[cell_index].neighbors:
                    self.moving_direction = "down"
                    self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                    self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["down"]
                    if len(self.snake_cells) == 1:
                        self.tail = self.snake_cells[cell_index]
                        self.tail_direction = "up"
                    self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
        return

    def append(self):
        # Add a new snake cell depending on the direction the cell is going
        if self.tail_direction == "left":
            self.snake_cells.append(self.tail.neighbors["left"])
            self.tail = self.snake_cells[len(self.snake_cells) - 1]
        elif self.tail_direction == "right":
            self.snake_cells.append(self.tail.neighbors["right"])
            self.tail = self.snake_cells[len(self.snake_cells) - 1]
        elif self.tail_direction == "up":
            self.snake_cells.append(self.tail.neighbors["up"])
            self.tail = self.snake_cells[len(self.snake_cells) - 1]
        elif self.tail_direction == "down":
            self.snake_cells.append(self.tail.neighbors["down"])
            self.tail = self.snake_cells[len(self.snake_cells) - 1]
        self.tail.color = pygame.Color([34, 136, 76, 1])
    '''
