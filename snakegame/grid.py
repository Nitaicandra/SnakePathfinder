import pygame, sys
import cell
import random
import snake


class Grid:
    # Cells are vertices with shape, color, and food distance
    fruit = cell.Cell

    def __init__(self, grid_width, grid_height, cell_size):
        self.cells = [[cell.Cell(cell_size) for j in range(grid_width)] for i in range(grid_height)]
        self.width = grid_width
        self.height = grid_height
        self.cell_size = cell_size
        self.fruit_coord = (0, 0)
        self.snake = snake.Snake(self, grid_height, grid_width)
        self.fruit = self.gen_fruit()

        # For convenience, add neighboring cells to a list for each cell
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
        # Position rectangles and draw them with the given cell color
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.cells[i][j].shape.top = i * self.cell_size
                self.cells[i][j].shape.left = j * self.cell_size
                pygame.draw.rect(surface, self.cells[i][j].color, self.cells[i][j].shape)

    def gen_fruit(self):
        self.fruit.color = pygame.Color([0, 0, 0, 1])
        # Put a random fruit on the grid within the bounds of the window
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        self.fruit_coord = (x, y)
        # Select the location where the fruit will spawn
        self.fruit = self.cells[y][x]
        # Continue looking for a location until the cell is not part of the snake
        while self.fruit in self.snake.snake_cells:
            self.fruit = self.cells[random.randint(0, self.height - 1)][random.randint(0, self.width - 1)]
        self.fruit.color = pygame.Color([211, 39, 55, 1])

        return self.fruit

    def gen_distances(self):
        # Manhattan Distance
        # All cells have some distance to the fruit
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.cells[i][j].fruit_distance = abs(self.fruit_coord[0] - j) + abs(self.fruit_coord[1] - i)
