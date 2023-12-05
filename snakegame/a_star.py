import pygame,sys
import cell
import grid
import snake_cell
from queue import PriorityQueue

#

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
    
    def G(self,cell): # path from start to current cell
        
        return abs((cell.x-self.start.x)+(cell.y-self.start.y))
        
    def H(self, cell): #path from cell to end
        return abs((cell.x-self.end.x)+(cell.y-self.end.y))

    def F(self, cell):
        return self.G(cell)+self.H(cell) 
        

    def add_to_open_set(self,cell,prev_cell=None):
        g_cost =self.F(self.start) #from start
        h_cost =self.H(self.end) # to end
        f_cost=g_cost+h_cost
        self.open_set.put((f_cost,g_cost,h_cost,self.start,cell,None))
        #placing tuple into a priority que will automatically sort based on first element of tuple
        
    def add_neighbors_to_set(self,cell):
    
        for neighbor in cell:
            if ((neighbor not in self.open_set) and (neighbor not in self.closed_set) and (not neighbor.snake_cell==None)):
                self.add_to_open_set(neighbor)
                
        # when this is called on a cell move that cell into the closed set
        self.open_set.remove(cell)
        self.closed_set.insert(cell)
        
        return
    
    def run(self):
    
        # what is the exit condition if the open set is empty
        # will break if the last thing is found
        # how to check if set is empty 
        # how to check if 
        self.add_to_open_set(self.start)
        
        
        while not self.open_set.isEmpty():
            # select lowest item in priority que
            # the first item in the priority que is the one with the largest fcost
            currentCell=self.openset[0] # first element in priority que
            self.add_neighbors_to_set(currentCell)
            # run add negihbors to set
            # repeat
            
            if(currentCell==self.end):
                return
        # once end note is reached access that node and traverse refrences 
        
            
        
    
        
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
        