import random
import enum


class RANDOM_ATTR(enum.EnumMeta):
    @property
    def RANDOM(self):
        return random.choice([State.ALIVE, State.DEAD])


class State(enum.Enum, metaclass=RANDOM_ATTR):
    DEAD = 0,
    ALIVE = 1

    def __str__(self):
        if self.name == "DEAD":
            return "."
        if self.name == "ALIVE":
            return "#"

    def __eq__(self, other):
        return self.name == other.name or self.value == other.value

class StateBuilder:

    @classmethod
    def build_with_indice(self, indice):
        if indice == '#':
            return State.ALIVE
        if indice == '.':
            return State.DEAD
