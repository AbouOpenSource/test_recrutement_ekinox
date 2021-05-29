import random

from models.Cell import Cell
from models.Position import Position
from models.State import State


class Grid:

    def __init__(self, length=5, width=5, number_generations=5):
        self.length = length
        self.width = width
        self.number_generations = number_generations
        self.adjacency_matrix = []

    def start(self):
        for x in range(self.length):
            self.adjacency_matrix.append([])
            for y in range(self.width):
                position = Position(x, y)
                self.adjacency_matrix[x].append(Cell(random.choice(list(State)), position))

    def live(self):
        for idx in range(self.number_generations):
            self.next_state_of_grid()

    def next_state_of_grid(self):
        for x in range(self.length):
            for y in range(self.width):
                self.change_state(x, y)

    def change_state(self, x, y):

        alive_neighbors = 0
        neighbors = self.find_neighborhood(x, y)
        # print("For the position :" + str(x) + str(y)+ " Numbres : "+str(len(neighbors)))
        for neighbor in neighbors:
            alive_neighbors = alive_neighbors + 1 if self.adjacency_matrix[neighbor[0]][
                                                         neighbor[1]].is_alive() else 0
            # print(alive_neighbors)

        if (self.adjacency_matrix[x][y].is_alive()) and alive_neighbors < 2:
            self.adjacency_matrix[x][y].make_dead()

        if (self.adjacency_matrix[x][y].is_alive()) and alive_neighbors in [2, 3]:
            print("[2,3]")
            self.adjacency_matrix[x][y].make_alive()

        if alive_neighbors > 3:
            self.adjacency_matrix[x][y].make_dead()

        if alive_neighbors == 3:
            self.adjacency_matrix[x][y].make_alive()

    def find_neighborhood(self, x_param, y_param):
        return [(x, y) for x in range(x_param - 1, x_param + 2)
                for y in range(y_param - 1, y_param + 2)
                if (-1 < x_param < self.length and
                    -1 < y_param < self.width and
                    (x_param != x or y_param != y) and
                    (0 <= x < self.length) and
                    (0 <= y < self.width))]

    def __str__(self):
        for x in range(self.length):
            for y in range(self.width):
                print(self.adjacency_matrix[x][y], end='')
            print('')
