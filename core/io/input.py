from core.models.Cell import Cell
from core.models.Position import Position
from core.models.State import StateFactory


class Singleton(type):
    """:return
        Singleton helper
        Having the list of the instances, once we requested for a Singleton ELement, if the
        element is already instantiated, we will return the previous instance from _instances
        dictionary
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


INITIAL_STEP = "INITIAL"
FINAL_STEP = "FINAL"


class Initializer(metaclass=Singleton):

    def __init__(self):
        file_init = open("data/initiale.txt", "r")
        file_final = open("data/final.txt", "r")
        self.payload = {
            INITIAL_STEP: file_init.readlines(),
            FINAL_STEP: file_final.readlines()
        }
        file_final.close()
        file_init.close()
        self.length = len(self.payload[FINAL_STEP][0].rstrip('\n'))
        self.width = len(self.payload[INITIAL_STEP])

    def get_length(self):
        return len(self.payload[FINAL_STEP][0].rstrip('\n'))

    def get_width(self):
        return len(self.payload[INITIAL_STEP])

    def get_adjacency_matrix(self, level):
        factor = StateFactory()
        matrix = []
        for x in range(self.get_width()):
            matrix.append([])
            for y in range(self.get_length()):
                position = Position(x, y)
                matrix[x].append(Cell(factor.create(self.payload[level][x][y]), position))
        return matrix

    def get_adjacency_matrix_initial(self):
        return self.get_adjacency_matrix(INITIAL_STEP)

    def get_adjacency_matrix_final(self):
        return self.get_adjacency_matrix(FINAL_STEP)
