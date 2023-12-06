import pygame,sys
import cell
import grid
import snake_cell
import timeit 
import csv
from queue import PriorityQueue

class Dijkstras:
    def __init__(self,grid,snake,start=None,end=None):
        self.grid=grid
        self.snake=snake
        self.start=snake.head
        self.end=grid.fruit
        
        self.frame_data="dijkstras_frame_data.csv"
        open(self.frame_data, 'w').close()
        self.averaged_data="dijkstras_averaged_data.csv"
        open(self.averaged_data, 'w').close()
        
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.avg = None
        self.frames = 0
        
        self.open_set=PriorityQueue()
        self.shortest_path= list()
    
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
            writer.writerow([f'DIJKSTRAS AVERAGE: {average}'])
            

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
    
    
    def dijkstra(self):
        #create a map of unvisited cells
        self.frames+=1
        self.start_time = timeit.default_timer()
        
        
        unvisited = {cell: float("inf") for row in self.grid.cells for cell in row} 
        came_from = {}
        
        #set the first node to 0
        unvisited[self.start]=0
        visited={}
        
        while unvisited:
            current=min(unvisited,key=unvisited.get)
            visited[current]=unvisited[current]
            
            if current == self.end:
                self.end_time=timeit.default_timer()
                self.elapsed_time = self.end_time-self.start_time
                
                self.reconstruct_path(came_from,self.end)
                self.move_snake_along_path()
                return True
            
            for key,neighbor in current.neighbors.items():
                if(neighbor.is_snake()):
                    continue
                temp_distance = unvisited [current]+1
                if temp_distance < unvisited[neighbor]:
                    unvisited[neighbor]=temp_distance
                    came_from[neighbor]=current
            unvisited.pop(current)
            
            for current in visited:
                if(current.is_unique()==False):current.color = pygame.Color([8, 164, 167, 1])
            
                    
                
        return False
        