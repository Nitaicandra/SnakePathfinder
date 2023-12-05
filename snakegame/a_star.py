import pygame,sys
import cell
import grid
import snake_cell
import timeit 
import csv
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
    
    def __init__(self,grid,snake,start=None,end=None):
        self.grid=grid
        self.snake=snake
        self.start=snake.head
        self.end=grid.fruit
        
        self.frame_data="a_star_frame_data.csv"
        open(self.frame_data, 'w').close()
        self.averaged_data="a_star_averaged_data.csv"
        open(self.averaged_data, 'w').close()
        
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.avg = None
        self.frames = 0
    
        
        self.open_set=PriorityQueue()
        self.shortest_path= list()
        
        
        
        self.closed_set= set() # if checked the add neighbors to set add thata cell to the closed set and remove from ope nset
        return
    

    def H(self,cell,cell2):
        return (cell.x-cell2.x)+(cell.y-cell2.y)

    def average(self,file=None,num=None):

        elapsed_times=[]         #an empty list to store the second column
        with open(self.frame_data, 'r') as rf:
            reader = csv.reader(rf, delimiter=',')
            if num == None:
                for row in reader:
                    elapsed_times.append(row[1])
            elif num>0:
                elapsed_times = [next(file) for _ in range(num)]
                
        sum = 0
        for time in elapsed_times:
            sum +=float(time)
        average = sum/len(elapsed_times)
        
        with open(self.averaged_data, 'w', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerow([f'A* AVERAGE: {average}'])
            

    def export_data_to_csv(self,file=None,num=5):
        with open(self.frame_data, 'a', newline='') as file:
            writer = csv.writer(file)
            #for i in range(0,num):
            writer.writerow([f'frame {self.frames}',self.elapsed_time])
            


    
    def reconstruct_path(self,came_from,current):
        self.shortest_path.insert(0,self.end)
        while current in came_from:
            current = came_from[current]
            if(current.is_unique()==False):current.color = [93, 33, 106, 1]
            self.shortest_path.insert(0, current)
        
    def move_snake_along_path(self):
        self.shortest_path[-1].color = [211, 39, 55, 1]
        for key,neighbor in self.snake.head.current.neighbors.items():
            if(len(self.shortest_path)>1):
                if neighbor == self.shortest_path[1]:
                    self.snake.move(key)
        self.end =self.grid.fruit
        self.shortest_path.clear()
            
    def a_star(self):
        #timer
        self.frames+=1
        self.start_time = timeit.default_timer()
        
        
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start.current))
        came_from = {}
        g_score = {cell: float("inf") for row in self.grid.cells for cell in row}
        g_score[self.start.current] = 0
        
        f_score = {cell: float("inf") for row in self.grid.cells for cell in row}
        f_score[self.start.current] = self.H(self.start.current,self.end)
        
        open_set_hash = {self.start.current}
        while not open_set.empty():
            current = open_set.get()[2]
            open_set_hash.remove(current)
            
            if current == self.end:
                self.end_time=timeit.default_timer()
                self.elapsed_time = self.end_time-self.start_time
                
                self.reconstruct_path(came_from,self.end)
                self.move_snake_along_path()
                return True
                
            for key,neighbor in current.neighbors.items():
                if(neighbor.is_snake()):
                    continue
                temp_g_score = g_score[current]+1
                if temp_g_score< g_score[neighbor]:
                    came_from[neighbor]=current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor]= temp_g_score + self.H(neighbor,self.end)
                    if neighbor not in open_set_hash:
                        count+=1
                        open_set.put((f_score[neighbor],count,neighbor))
                        open_set_hash.add(neighbor)
                        if(current.is_unique()==False):neighbor.color=pygame.Color([8, 76, 97, 1])
                    
                    
            if current != self.start:
                if(current.is_unique()==False):current.color = pygame.Color([8, 164, 167, 1])
        
        return False

        