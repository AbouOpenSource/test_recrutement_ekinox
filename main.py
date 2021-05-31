from core.io.input import Initializer
from core.models.Grid import Grid

NUMBER_GEN = 5


def main():
    grid = Grid.build_from_adjacency_matrix(Initializer().get_adjacency_matrix_initial(), NUMBER_GEN)

    # Example with the random state in the grid and the random size of the grid

    # grid = Grid.build_random_grid(NUMBER_GEN)
    grid.live()


if __name__ == "__main__":
    main()
