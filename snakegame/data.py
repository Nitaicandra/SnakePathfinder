import pygame, sys
import cell
import grid
import random
from snake_cell import SnakeCell
from enum import Enum
import pandas as pd


# probably just a head and tail to snake cells # form a sort of linked list
class Data:
    
    s1 = pd.Series([5, 6, 7])
    s2 = pd.Series([7, 8, 9])

    frameData = pd.DataFrame([list(s1), list(s2)],  columns =  ["dijkstas", "A*"])
    
    
    
    
    
    def insert():
        return
    