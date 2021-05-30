from models import Position
from models.State import State


class Cell:
    def __init__(self, state: State, position: Position):
        self.position = position
        self.state = state
        self.id = id(self)

    def is_alive(self):
        if self.state == State.ALIVE:
            return True
        return False

    def make_alive(self):
        self.state = State.ALIVE

    def make_dead(self):
        self.state = State.DEAD

    def __str__(self):
        return str(self.state)

    #TODO : two cells aren't equals if they have the same state. but if they have the same id. We have to change it
    def __eq__(self, other):
        return self.state == other.state
