import random
import logging

from models.Cell import Cell
from models.Position import Position
from models.State import State

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Grid:

    def __init__(self, adjacency_matrix=[], length=5, width=5, number_generations=5):
        self.length = length
        self.width = width
        self.number_generations = number_generations
        self.adjacency_matrix = adjacency_matrix
        logger.info(self)
        logger.info(self.adjacency_matrix[2][1])

    @classmethod
    def build_from_adjacency_matrix(cls, adjacency_matrix):
        return cls(adjacency_matrix, len(adjacency_matrix[0]), len(adjacency_matrix))

    def start(self):
        logger.info(" Starting the live of the Grid")
        for x in range(self.width):
            self.adjacency_matrix.append([])
            for y in range(self.length):
                position = Position(x, y)
                self.adjacency_matrix[x].append(Cell(State.RANDOM, position))
        logger.info(" The initial state of the petri " + str(self))

    def live(self):
        for idx in range(self.number_generations):
            logger.info("The generation :"+str(idx))
            self.next_state_of_grid()
            logger.info(self)

    def next_state_of_grid(self):
        matrix_number_alive = self.get_matrix_number_neighbour_living()
        for x in range(self.width):
            for y in range(self.length):
                self.change_state(x, y, matrix_number_alive)

    def change_state(self, x, y, matrix):
        """

        """
        if (self.adjacency_matrix[x][y].is_alive()) and (matrix[x][y] < 2 or matrix[x][y] > 3):
            self.adjacency_matrix[x][y].make_dead()

        if (self.adjacency_matrix[x][y].is_alive()) and matrix[x][y] in [2, 3]:
            self.adjacency_matrix[x][y].make_alive()

        if not self.adjacency_matrix[x][y].is_alive() and matrix[x][y] == 3:
            self.adjacency_matrix[x][y].make_alive()

    def find_neighborhood(self, x_param, y_param):
        """ Return the list of the neighbours of the element whose coordinates have been passed in parameter

        """
        return [(x, y) for x in range(x_param - 1, x_param + 2)
                for y in range(y_param - 1, y_param + 2)
                if (-1 < x_param < self.width and
                    -1 < y_param < self.length and
                    (x_param != x or y_param != y) and
                    (0 <= x < self.width) and
                    (0 <= y < self.length))]

    def get_matrix_number_neighbour_living(self):
        """
           This method return a matrix where item at the position(x,y)
           is a number of neighbours living of the cell at the position(x,y) of the petri.
        """
        matrix_alive = []
        for x in range(self.width):
            matrix_alive.append([])
            for y in range(self.length):
                alive_neighbors = 0
                neighbors = self.find_neighborhood(x, y)
                for coordinate in neighbors:
                    if self.adjacency_matrix[coordinate[0]][coordinate[1]].is_alive():
                        alive_neighbors = alive_neighbors + 1
                matrix_alive[x].append(alive_neighbors)

        return matrix_alive

    def __str__(self):
        temp = "\n"
        for x in range(self.width):
            for y in range(self.length):
                temp = temp + str(self.adjacency_matrix[x][y])
            temp = temp + "\n"
        return temp

    def __repr__(self):
        for x in range(self.width):
            for y in range(self.length):
                print(self.adjacency_matrix[x][y], end='')
            print('')
