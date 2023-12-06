import pygame


# probably just a head and tail to snake cells # form a sort of linked list
class Snake:
    snake_cells = list()
    moving_direction = "left"
    tail_direction = "right"

    def __init__(self, game_grid, grid_height, grid_width):
        # Put the snake cell's head in the middle of the board
        self.snake_cells.append(game_grid.cells[int((grid_height - 1) / 2)][int((grid_width - 1) / 2)])
        self.snake_cells[0].color = pygame.Color([34, 136, 76, 1])
        self.tail = self.snake_cells[len(self.snake_cells) - 1]
        self.prev_cell = self.snake_cells[0]
        self.game_grid = game_grid

        return

    # Move the snake by changing the colors of the grid and tracking those cells
    def move(self, cell_index, direction, cell):
        cell_buff = cell
        dead = False
        match direction:
            # For all directions:


            case "left":
                if "left" in self.snake_cells[cell_index].neighbors:
                    if cell_index != len(self.snake_cells) - 1:
                        # Check if the cell to move towards is part of the snake, if so kill the snake
                        if cell == self.snake_cells[0] and self.snake_cells[0].neighbors["left"] in self.snake_cells:
                            self.kill()
                            dead = True
            # Check if the snake was not killed earlier
            # If it is alive, move to the proper cell as directed
            # Don't allow movement opposite to that of the moving direction
                if not dead:
                    if self.moving_direction != "right" or cell != self.snake_cells[0]:
                        # Avoid the wall/window
                        if "left" in self.snake_cells[cell_index].neighbors:
                            # Do not allow movement in the opposite direction of current moving direction
                            if cell == self.snake_cells[0]:
                                self.moving_direction = "left"
                            self.snake_cells[cell_index].color = pygame.Color([0, 0, 0, 1])
                            self.snake_cells[cell_index] = self.snake_cells[cell_index].neighbors["left"]
                            self.snake_cells[cell_index].color = pygame.Color([34, 136, 76, 1])

                            if cell_index != len(self.snake_cells) - 1:
                                self.move(cell_index + 1, list(self.snake_cells[cell_index + 1].neighbors.keys())[
                                    list(self.snake_cells[cell_index + 1].neighbors.values()).index(cell_buff)],
                                          self.snake_cells[cell_index + 1])
                            else:
                                self.tail = self.snake_cells[len(self.snake_cells) - 1]
                                self.tail_direction = "right"
                        else:
                            self.kill()

            case "right":
                if "right" in self.snake_cells[cell_index].neighbors:
                    if cell_index != len(self.snake_cells) - 1:
                        # Check if the cell to move towards is part of the snake, if so kill the snake
                        if cell == self.snake_cells[0] and self.snake_cells[0].neighbors["right"] in self.snake_cells:
                            self.kill()
                            dead = True
                # Check if the snake was not killed earlier
                # If it is alive, move to the proper cell as directed
                # Don't allow movement opposite to that of the moving direction
                if not dead:
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
                                          self.snake_cells[cell_index + 1])
                            else:
                                self.tail = self.snake_cells[len(self.snake_cells) - 1]
                                self.tail_direction = "left"
                        else:
                            self.kill()
            case "up":
                if "up" in self.snake_cells[cell_index].neighbors:
                    if cell_index != len(self.snake_cells) - 1:
                        # Check if the cell to move towards is part of the snake, if so kill the snake
                        if cell == self.snake_cells[0] and self.snake_cells[0].neighbors["up"] in self.snake_cells:
                            self.kill()
                            dead = True
                # Check if the snake was not killed earlier
                # If it is alive, move to the proper cell as directed
                # Don't allow movement opposite to that of the moving direction
                if not dead:
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
                                          self.snake_cells[cell_index + 1])
                            else:
                                self.tail = self.snake_cells[len(self.snake_cells) - 1]
                                self.tail_direction = "down"
                        else:
                            self.kill()
            case "down":
                if "down" in self.snake_cells[cell_index].neighbors:
                    if cell_index != len(self.snake_cells) - 1:
                        # Check if the cell to move towards is part of the snake, if so kill the snake
                        if cell == self.snake_cells[0] and self.snake_cells[0].neighbors["down"] in self.snake_cells:
                            self.kill()
                            dead = True
                # Check if the snake was not killed earlier
                # If it is alive, move to the proper cell as directed
                if not dead:
                    # Don't allow movement opposite to that of the moving direction
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
                                          self.snake_cells[cell_index + 1])
                            else:
                                self.tail = self.snake_cells[len(self.snake_cells) - 1]
                                self.tail_direction = "up"
                        else:
                            self.kill()
        # Check if the cell that we moved towards is the fruit--append if it is the case
        if self.game_grid.fruit == self.game_grid.snake.snake_cells[0]:
            self.game_grid.snake.append()
            self.game_grid.gen_fruit()
        return

    def append(self):
        # Add a new snake cell to the tail depending on the direction the cell is going
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

    # Following collision (with itself or the wall) destroy the cells and respawn the snake
    def kill(self):
        # Turn all cells to the background color
        for cell in self.snake_cells:
            cell.color = pygame.Color([0, 0, 0, 1])
        self.snake_cells.clear()
        self.reset()

    # Re-initialize all variables contained in the snake class
    def reset(self):
        self.moving_direction = "left"
        self.tail_direction = "right"
        self.snake_cells.append(
            self.game_grid.cells[int((self.game_grid.height - 1) / 2)][int((self.game_grid.width - 1) / 2)])
        self.snake_cells[0].color = pygame.Color([34, 136, 76, 1])
        self.tail = self.snake_cells[len(self.snake_cells) - 1]
        self.prev_cell = self.snake_cells[0]
        self.game_grid.fruit = self.game_grid.gen_fruit()
