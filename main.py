from models.Grid import Grid
from wr.input import Initializer


def main():
    grid = Grid.build_from_adjacency_matrix(Initializer().get_adjacency_matrix())
    #print(grid.get_matrix_number_neighbour_living())

    grid.live()

if __name__ == "__main__":
    main()
