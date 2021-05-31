from core.models.Position import Position
from core.models.State import State


class Cell:
    def __init__(self, state: State, position: Position):
        self.position = position
        self.state = state
        self.id = id(self)

    def is_alive(self):
        """ Check if the cell is alive or not
            :return Boolean
        """
        if self.state == State.ALIVE:
            return True
        return False

    def make_alive(self):
        """Make the cell alive
        """
        self.state = State.ALIVE

    def make_dead(self):
        """Make the cell dead
        """
        self.state = State.DEAD

    def __str__(self):
        return str(self.state)

    def __eq__(self, other):
        """
        DISCLAIMER I put this one for the unit test.
        We suppose that if two cells have the same state, they are equals.
        But in real live, it isn't the case.
        """
        return self.state == other.state
