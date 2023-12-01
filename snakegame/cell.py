import random
import pygame, sys
import snake_cell


class Cell:

    def __init__(self, size):
        self.shape = pygame.Rect(0, 0, size, size)
        # Test Grid
        # self.color = pygame.Color([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 1])
        self.color = pygame.Color([0, 0, 0, 1])
        self.neighbors = {}
        return
