from models import Position
from models.State import State


class Cell:
    def __init__(self, state: State, position: Position):
        self.position = position
        self.state = state

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
