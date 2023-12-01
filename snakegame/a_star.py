import pygame,sys
import cell
import grid
import snake_cell
from queue import PriorityQueue

#given a grid 
#given a start cell
#given an end cell
#run astar to find the shortest path
# change colors based on searching
# give a linked list path
#compare the indexes to find cartesian distances
#snake cannot move in diagonals
#return linked list of cells


#G SCORE DISTANCE FROM START
#H SCORE DISTANCE FROM END 
#F SCORE H+F

class Path:
    def __init__(self,grid,start,end):
        return
    
class AStar:
    
    def __init__(self,grid,start,end):
        self.grid=grid
        self.start=start
        self.end=end
        self.open_set=PriorityQueue()
        
        self.closed_set= set() # if checked the add neighbors to set add thata cell to the closed set and remove from ope nset
        return
    
    def F():
        return
    def H():
        return 
    def G(h,f):
        return h+f
        
    def add_neighbors_to_set(self,cell):
    
        for neighbor in cell:
            if ((neighbor not in self.open_set) and (neighbor not in self.closed_set) and (not neighbor.isSnake)):
                self.open_set.insert(neighbor)
                
            
            self.open_set.remove(cell)
            self.closed_set.insert(cell)
        
        return
    
    def run(self):
    
        # what is the exit condition if the open set is empty
        # will break if the last thing is found
        # how to check if set is empty 
        # how to check if 
        f_cost =self.F(self.start)
        h_cost =self.H(self.start)
        g_cost=self.G(h_cost,f_cost)
        self.openset.put(g_cost,f_cost,h_cost,self.start)
        while not self.open_set.isEmpty():
            # select lowest item in priority que
            currentCell=self.openset[0] # first element in priority que
            
            # run add negihbors to set
            # repeat
            
            if(currentCell==self.end):
                return
        
            
        
    
        
        #check each direction
        #get the distance for each
        #check if snake or not
        
        #select temporary path based on the one with the shortest distance 
        #keep selecting shortest path until goal is reached
        # if a path becomes larger than a currently existing path then back track to the last good one 
        
        #so add to some datastructure and if added to that datastructure make blue
        # if it is selected as the best make red,
        # if part of final path make black or somthin
        # should be done in one frame so intermediate steps wont be shown
        # should be calculated every frame 
        
        return
        