from enum import Enum


class State(Enum):
    DEAD = 0,
    ALIVE = 1

    def __str__(self):
        if self.value == 0:
            return '.'
        return '#'
