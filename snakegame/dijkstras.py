import sys


class Dijkstras:
    def __init__(self):
        # Computed vertices
        self.s = set()
        # Remaining vertices
        self.vs = set()
        # Distances from source vertex
        self.distance = dict()
        # Parent of least-distant vertex
        self.parent = dict()
        return

    def calculatePath(self, snake, game_grid):

        # Clear past dijkstra runs (before fruit collection)
        self.s.clear()
        self.vs.clear()
        self.distance.clear()
        self.parent.clear()

        # Initialize the dijkstra sets and dictionaries
        for i in range(0, game_grid.height):
            for j in range(0, game_grid.width):
                # Check for cells that are not part of the snake--do not add
                # Case that is not head
                if len(snake.snake_cells) > 0 and game_grid.cells[i][j] not in (list(snake.snake_cells[1::(len(snake.snake_cells))])):
                    self.vs.add(game_grid.cells[i][j])
                    # Initialize the distance for the source to just 0, and its parent to 1
                    if game_grid.cells[i][j] == snake.snake_cells[0]:
                        self.distance[snake.snake_cells[0]] = 0
                        self.parent[snake.snake_cells[0]] = -1
                    # All other cells will have a distance of INT_MAX and a -1 parent
                    else:
                        self.distance[game_grid.cells[i][j]] = sys.maxsize
                        self.parent[game_grid.cells[i][j]] = -1
                # Case when it is the head being inserted
                else:
                    if game_grid.cells[i][j] == snake.snake_cells[0]:
                        self.distance[snake.snake_cells[0]] = 0
                        self.parent[snake.snake_cells[0]] = -1

        distance_buffer = self.distance.copy()
        # While vs is not empty
        # Dijkstra Algorithm
        while self.vs:
            # Get the smallest distance in the distance dictionary
            # Buffer used to track those that were already computed
            smallest = min(distance_buffer, key=self.distance.get)
            del distance_buffer[smallest]
            self.vs.remove(smallest)
            self.s.add(smallest)
            # Relax neighbors
            for neighbor in smallest.neighbors:
                if smallest.neighbors[neighbor] not in snake.snake_cells:
                    if self.distance[smallest.neighbors[neighbor]] > self.distance[smallest] + smallest.fruit_distance:
                        self.distance[smallest.neighbors[neighbor]] = self.distance[smallest] + smallest.fruit_distance
                        self.parent[smallest.neighbors[neighbor]] = smallest

    def getFoodPath(self, source, target):
        stk = []
        path = []
        # Obtain the proper path by going in reverse (source to target)
        while source != target:
            stk.append(target)
            target = self.parent[target]
        for i in range(0, len(stk)):
            path.append(stk.pop())
        return path
