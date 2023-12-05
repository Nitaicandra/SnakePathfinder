import pygame, sys
import cell
import snake_cell
import random


class Grid:
    # Cells are vertices with shape, color, and food distance

    def __init__(self, grid_width, grid_height, cell_size):
        
        self.width = grid_width
        self.height = grid_height
        self.cell_size = cell_size
        self.fruit= self.cells[random.randint(0, self.width)][random.randint(0, self.height)]
        
        #width then height (0,0)is in the 
        #height then width, increasing height moves it down on the page, top right corner is 0,0
        self.cells = [[cell.Cell(cell_size,i,j) for j in range(self.height)] for i in range(self.width)]

        for i in range(0, self.height):
            for j in range(0, self.width):
                # Left
                if j - 1 >= 0:
                    self.cells[i][j].neighbors["left"] = self.cells[i][j - 1]
                # Right
                if j + 1 < grid_width:
                    self.cells[i][j].neighbors["right"] = self.cells[i][j + 1]
                # Up
                if i - 1 >= 0:
                    self.cells[i][j].neighbors["up"] = self.cells[i - 1][j]
                # Down
                if i + 1 < grid_width:
                    self.cells[i][j].neighbors["down"] = self.cells[i + 1][j]

    def draw_grid(self, surface):
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.cells[i][j].shape.top = i * self.cell_size
                self.cells[i][j].shape.left = j * self.cell_size
                pygame.draw.rect(surface, self.cells[i][j].color, self.cells[i][j].shape)
                
    def draw_grid_lines(self, surface):
        gap = self.cell_size
        for i in range(self.height): #rows
            pygame.draw.line(surface,pygame.Color([128, 128, 128,1]),(0,i*gap),(gap*len(self.cells),i*gap))
            for j in range(self.width): #columns
                pygame.draw.line(surface,pygame.Color([128, 128, 128,1]),(j*gap,0),(j*gap,gap*len(self.cells[0])))
                
    def reset_colors(self):
        for i in range(self.height): #rows
            for j in range(self.width): #columns
                if self.cells[i][j].isSnake()== False:
                    self.cells[i][j].reset_color()
    def snake_checker(self):
        for i in range(self.height): #rows
            for j in range(self.width): #columns
                if self.cells[i][j].isSnake()== True:
                    self.cells[i][j].color = pygame.Color([0, 0, 255, 1])
                else:
                    self.cells[i][j].reset_color()
    def gen_fruit(self, snake):
        fruit = self.cells[random.randint(0, self.width)][random.randint(0, self.height)]
        fruit.color = pygame.Color([211, 39, 55, 1])
        return fruit