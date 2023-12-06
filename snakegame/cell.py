import pygame

# Class representing each cell in the snake game grid
class Cell:

    def __init__(self, size):
        self.shape = pygame.Rect(0, 0, size, size)
        self.color = pygame.Color([0, 0, 0, 1])
        self.neighbors = {}
        # We store the fruit distance in the beginning for dijkstra's algorithm
        self.fruit_distance = 0
        return
