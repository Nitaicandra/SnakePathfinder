import pygame, sys
import cell
import grid
import random
from enum import Enum


# probably just a head and tail to snake cells # form a sort of linked list
class Snake:
    snake_cells = list()
    moving_direction = "left"
    tail_direction = "right"

    def __init__(self, game_grid, grid_height, grid_width):
        self.snake_cells.append(game_grid.cells[int((grid_height - 1)/2)][int((grid_height - 1) / 2)])
        self.snake_cells[0].color = pygame.Color([34, 136, 76, 1])
        self.tail = self.snake_cells[len(self.snake_cells) - 1]
        self.prev_cell = self.snake_cells[0]
        return

    # Move the snake by changing the colors of the grid and tracking those cells
    # Need to complete movement for cells appended to the snake (must follow the previous moved cell until the tail)
    def move(self, cell_index, direction, cell, fruit, game_grid):
        cell_buff = cell
        match direction:
            case "left":
                if self.moving_direction != "right" or cell != self.snake_cells[0]:
                    if "left" in self.snake_cells[cell_index].neighbors:
                        if cell == self.snake_cells[0]:
                            self.moving_direction = "left"
                        self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                        self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["left"]
                        self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])

                        if cell_index != len(self.snake_cells) - 1:
                                self.move(cell_index + 1, list(self.snake_cells[cell_index + 1].neighbors.keys())[
                                    list(self.snake_cells[cell_index + 1].neighbors.values()).index(cell_buff)],
                                          self.snake_cells[cell_index + 1], fruit, game_grid)
                        else:
                            self.tail = self.snake_cells[len(self.snake_cells) - 1]
                            self.tail_direction = "right"

            case "right":
                if self.moving_direction != "left" or cell != self.snake_cells[0]:
                    if "right" in self.snake_cells[cell_index].neighbors:
                        if cell == self.snake_cells[0]:
                            self.moving_direction = "right"
                        self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                        self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["right"]
                        self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
                        if cell_index != len(self.snake_cells) - 1:
                                self.move(cell_index + 1, list(self.snake_cells[cell_index + 1].neighbors.keys())[
                                    list(self.snake_cells[cell_index + 1].neighbors.values()).index(cell_buff)],
                                          self.snake_cells[cell_index + 1], fruit, game_grid)
                        else:
                            self.tail = self.snake_cells[len(self.snake_cells) - 1]
                            self.tail_direction = "left"
            case "up":
                if self.moving_direction != "down" or cell != self.snake_cells[0]:
                    if "up" in self.snake_cells[cell_index].neighbors:
                        if cell == self.snake_cells[0]:
                            self.moving_direction = "up"
                        self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                        self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["up"]
                        self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
                        if cell_index != len(self.snake_cells) - 1:
                                self.move(cell_index + 1, list(self.snake_cells[cell_index + 1].neighbors.keys())[
                                    list(self.snake_cells[cell_index + 1].neighbors.values()).index(cell_buff)],
                                          self.snake_cells[cell_index + 1], fruit, game_grid)
                        else:
                            self.tail = self.snake_cells[len(self.snake_cells) - 1]
                            self.tail_direction = "down"
            case "down":
                if self.moving_direction != "up" or cell != self.snake_cells[0]:
                    if "down" in self.snake_cells[cell_index].neighbors:
                        if cell == self.snake_cells[0]:
                            self.moving_direction = "down"
                        self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                        self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["down"]
                        self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])
                        if cell_index != len(self.snake_cells) - 1:
                                self.move(cell_index + 1, list(self.snake_cells[cell_index + 1].neighbors.keys())[
                                    list(self.snake_cells[cell_index + 1].neighbors.values()).index(cell_buff)],
                                          self.snake_cells[cell_index + 1], fruit, game_grid)
                        else:
                            self.tail = self.snake_cells[len(self.snake_cells) - 1]
                            self.tail_direction = "up"
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

    def kill(self):
        for cell in self.snake_cells:
            cell.color = pygame.Color([0, 0, 0, 1])
        self.snake_cells.clear()
