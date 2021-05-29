

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Position is x: {0} and y: {1}'.format(self.x, self.y)

    def __hash__(self):
        return hash(str(self.x)+str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

