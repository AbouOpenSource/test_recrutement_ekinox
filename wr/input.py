from models.Cell import Cell
from models.Position import Position
from models.State import State, StateBuilder


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Initializer(metaclass=Singleton):

    def __init__(self):
        self.payload_initial = open("data/initiale.txt")
        self.payload_final = open("data/final.txt")
        self.lines_initial = self.payload_initial.readlines()
        self.lines_final = self.payload_final.readlines()

    def get_length(self):
        return len(self.lines_initial[0].rstrip('\n'))

    def get_width(self):
        return len(self.lines_initial)

    def get_adjacency_matrix(self):
        builder = StateBuilder()
        matrix = []
        for x in range(self.get_width()):
            matrix.append([])
            for y in range(self.get_length()):
                position = Position(x, y)
                matrix[x].append(Cell(builder.build_with_indice(self.lines_initial[x][y]), position))
        return matrix

    def get_adjacency_matrix_final(self):
        builder = StateBuilder()
        matrix = []
        for x in range(self.get_width()):
            matrix.append([])
            for y in range(self.get_length()):
                position = Position(x, y)
                matrix[x].append(Cell(builder.build_with_indice(self.lines_final[x][y]), position))
        return matrix