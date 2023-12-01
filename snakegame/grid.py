import pygame, sys
import cell
import snake_cell
import random


class Grid:
    # Cells are vertices with shape, color, and food distance
    def __init__(self, grid_width, grid_height, cell_size):
        self.cells = [[cell.Cell(cell_size) for j in range(grid_width)] for i in range(grid_height)]
        self.width = grid_width
        self.height = grid_height
        self.cell_size = cell_size
        for i in range(0, grid_height):
            for j in range(0, grid_width):
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
                if i + 1 < grid_height:
                    self.cells[i][j].neighbors["down"] = self.cells[i + 1][j]

    def draw_grid(self, surface):
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.cells[i][j].shape.top = i * self.cell_size
                self.cells[i][j].shape.left = j * self.cell_size
                pygame.draw.rect(surface, self.cells[i][j].color, self.cells[i][j].shape)

    def gen_fruit(self, snake):
        fruit = self.cells[random.randint(0, self.width)][random.randint(0, self.height)]
        while fruit in snake.snake_cells:
            fruit = self.cells[random.randint(0, self.width)][random.randint(0, self.height)]
        fruit.color = pygame.Color([211, 39, 55, 1])
        return fruit

