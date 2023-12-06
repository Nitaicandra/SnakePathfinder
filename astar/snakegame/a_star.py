import pygame,sys
import cell
import grid
import snake_cell
import timeit 
import csv
from queue import PriorityQueue


class AStar:
    
    def __init__(self,grid,snake,start=None,end=None):
        # get a refrence to grid and snake
        self.grid=grid
        self.snake=snake
        self.start=snake.head
        self.end=grid.fruit
        
        # initializing timing files
        self.frame_data="a_star_frame_data.csv"
        open(self.frame_data, 'w').close()
        self.averaged_data="a_star_averaged_data.csv"
        open(self.averaged_data, 'w').close()
        
        # initalize iming variables
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.avg = None
        self.frames = 0
    
        # creat the priority que for dijkstras will hold fscore,count,cell priority based on fscore
        self.open_set=PriorityQueue()
        
        #create a list that holdsthe final path 
        self.shortest_path= list()

    
    #heuristic function used to calculate the distance between two cells
    def H(self,cell,cell2):
        return (cell.x-cell2.x)+(cell.y-cell2.y)

    # timing function used to read the frame data and average them
    def average(self,file=None,num=None):
        
        # stores the elapsed times in frame data
        elapsed_times=[] 
        #reads the framed data file and places data into elapsed time
        with open(self.frame_data, 'r') as rf:
            reader = csv.reader(rf, delimiter=',')
            if num == None:
                for row in reader:
                    elapsed_times.append(row[1])
            elif num>0:
                elapsed_times = [next(file) for _ in range(num)]
        # averages the elapsed times
        sum = 0
        for time in elapsed_times:
            sum +=float(time)
        average = sum/len(elapsed_times)
        
        #writes it to the file
        with open(self.averaged_data, 'w', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerow([f'A* AVERAGE: {average}'])
            
    # writes freame data every frame
    def export_data_to_csv(self,file=None,num=5):
        with open(self.frame_data, 'a', newline='') as file:
            writer = csv.writer(file)
            #for i in range(0,num):
            writer.writerow([f'frame {self.frames}',self.elapsed_time])
            


    # given the last cell found travel backwards using the came from dictionary we maid for each cell to construct and display a list of the shortest path
    def reconstruct_path(self,came_from,current):
        self.shortest_path.insert(0,self.end)
        while current in came_from:
            current = came_from[current]
            if(current.is_unique()==False):current.color = [93, 33, 106, 1]
            self.shortest_path.insert(0, current)
            
    # move the snake along the given linked list path
    def move_snake_along_path(self):
        self.shortest_path[-1].color = [211, 39, 55, 1]
        for key,neighbor in self.snake.head.current.neighbors.items():
            if(len(self.shortest_path)>1):
                if neighbor == self.shortest_path[1]:
                    self.snake.move(key)
        self.end =self.grid.fruit
        self.shortest_path.clear()
            
    # main function
    def a_star(self):
        # initialize timer
        self.frames+=1
        self.start_time = timeit.default_timer()
        
        
        count = 0
        # used to hold the priority of all evaluated cells
        open_set = PriorityQueue()
        
        #fcost, count aka tie breaker , node
        # priority que holding the elements that are curently being evaluated
        # holds the fcost and count
        open_set.put((0, count, self.start.current))
        came_from = {}
        
        #cost dictionary that holds the g cost or the cost to go to a cell
        g_score = {cell: float("inf") for row in self.grid.cells for cell in row}
        g_score[self.start.current] = 0
        
        # cost dicitionary that holds the f cost or the sum of the cost ot go into the cell plus the predicted cost to go to the goal
        f_score = {cell: float("inf") for row in self.grid.cells for cell in row}
        f_score[self.start.current] = self.H(self.start.current,self.end)
        
        #this is a set that holds every cell that is going to be evaluated
        # every cell that has been evaluated will be removed from this hash table
        # will continually be updated by removing the smallest fcost item which is current each time then expanding the searching edge which is ever cell in open set
        open_set_hash = {self.start.current}
        
        # will loop until the priority que is empty
        while not open_set.empty():
            # gets the cell refrence in priority que
            current = open_set.get()[2]
            
            # removes from the the hash set as it is now being evaluated
            open_set_hash.remove(current)
            
            # exit condition if the end goal is found
            if current == self.end:
                # once the end condition os found end the timer and get elapsed time
                self.end_time=timeit.default_timer()
                self.elapsed_time = self.end_time-self.start_time
                
                # reconstruct path then move snake one space along path this runs every frame
                self.reconstruct_path(came_from,self.end)
                self.move_snake_along_path()
                return True
            
            # using current evaluate currens neighbors
            for key,neighbor in current.neighbors.items():
                # if the neighbor is snake then skip it
                if(neighbor.is_snake()):
                    continue
                
                #cost of going to new cell is always one more than the old cell
                temp_g_score = g_score[current]+1
                
                #if the cost of going to a neighbor is less than what is currently in the table then
                # note when first going through the cells case it will always be lower because gscores are initialized to infinity
                if temp_g_score< g_score[neighbor]:
                    # replace whats curently ther make the new came from of the evaluate neighbro to current and set the f and g scores
                    came_from[neighbor]=current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor]= temp_g_score + self.H(neighbor,self.end)
                    
                    # if the neighbors of current are not in the open set then color it dark blue
                    # these are then added to the priority que and open_set
                    if neighbor not in open_set_hash:
                        count+=1 # tie breaker
                        open_set.put((f_score[neighbor],count,neighbor))
                        open_set_hash.add(neighbor)
                        if(current.is_unique()==False):neighbor.color=pygame.Color([8, 76, 97, 1])
                    
            # if the current is not the start node then color it cyan
            # current will go through every node up untill the final que coloring the searched spaces cyan
            if current != self.start:
                if(current.is_unique()==False):current.color = pygame.Color([8, 164, 167, 1])
        
        return False

        