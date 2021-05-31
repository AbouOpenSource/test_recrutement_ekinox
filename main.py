import logging

from core.io.input import Initializer
from core.models.Grid import Grid


def main():
    grid = Grid.build_from_adjacency_matrix(Initializer().get_adjacency_matrix_initial())
    # grid = Grid.build_random_grid()
    grid.live()


if __name__ == "__main__":
    main()
