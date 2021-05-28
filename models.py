from enum import Enum
import random


class Grid:

    def __init__(self, length=5, width=5, number_generations=5):
        self.length = length
        self.width = width
        self.number_generations = number_generations
        self.array_payload = [None] * width * length
        self.payload = {}

    def start(self):
        for x in range(self.length):
            for y in range(self.width):
                position = Position(x, y)
                self.payload[position] = Cell(random.choice(list(State)), position)

    def live(self):
        for idx in range(self.number_generations):
            self.next_state_grid()

    def next_state_grid(self):
        for pos in self.payload.keys():
            self.change_state(pos)

    def change_state(self, position):
        alive_neighbors = 0
        neighbors = self.find_neighborhood(position)
        print("For the position :" + str(position) + "Numbres : "+str(len(neighbors)))
        for neighbor in neighbors:
            print(neighbor)
            #print(self.payload[neighbor])
            #alive_neighbors = alive_neighbors + 1 if self.payload[neighbor].state == State.ALIVE else 0
            #print(alive_neighbors)
        """
        for neighbor in neighbors:
            alive_neighbors += 1 if self.payload[neighbor].state == State.ALIVE else 0
        print(alive_neighbors)
        if (self.payload[Position(position.x, position.y)].state == State.ALIVE) and alive_neighbors < 2:
            self.payload[Position(neighbor.x, neighbor.y)].state = State.DEAD

        if (self.payload[Position(position.x, position.y)].state == State.ALIVE) and alive_neighbors in [2, 3]:
            self.payload[Position(neighbor.x, neighbor.y)].state = State.ALIVE

        if alive_neighbors > 3:
            self.payload[Position(neighbor.x, neighbor.y)].state = State.DEAD

        if alive_neighbors == 3:
            self.payload[Position(neighbor.x, neighbor.y)].state = State.ALIVE
        """

    def find_neighborhood(self, position):
        return [Position(x, y) for x in range(position.x - 1, position.x + 2)
                for y in range(position.y - 1, position.y + 2)
                if (-1 < position.x <= self.length and
                    -1 < position.y <= self.width and
                    (position.x != x or position.y != y) and
                    (0 <= x <= self.length) and
                    (0 <= y <= self.width))]

    def __str__(self):
        for x in range(self.length):
            for y in range(self.width):
                print(self.payload[Position(x, y)].state, end='   ')
            print()


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Position is x: {0} and y: {1}'.format(self.x, self.y)

    def __hash__(self):
        return hash(self.x + self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class State(Enum):
    DEAD = 0,
    ALIVE = 1

    def __str__(self):
        if self.value == 0:
            return '.'
        return '#'


class Cell:
    def __init__(self, state: State, position: Position):
        self.position = position
        self.state = state

    def __str__(self):
        return 'Cell at position {0}, in state {1}'.format(self.position, self.state)
