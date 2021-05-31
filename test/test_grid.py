import unittest



from core.io.input import Initializer
from core.models.Grid import Grid


class TestGrid(unittest.TestCase):

    def test_number_aliving_neighbour_matrix(self):
        expected_matrix = [[3, 4, 3, 2, 0, 2, 2, 3, 2, 1],
                           [3, 5, 3, 3, 2, 3, 2, 3, 5, 4],
                           [3, 5, 3, 3, 2, 3, 5, 5, 3, 1],
                           [1, 1, 2, 2, 1, 3, 2, 2, 3, 2]
                           ]
        grid = Grid.build_from_adjacency_matrix(Initializer().get_adjacency_matrix_initial())
        matrix = grid.get_matrix_number_neighbour_living()
        self.assertListEqual(matrix, expected_matrix)

    def test_example_given(self):
        grid = Grid.build_from_adjacency_matrix(Initializer().get_adjacency_matrix_initial())
        grid.live()
        self.assertListEqual(grid.adjacency_matrix, Initializer().get_adjacency_matrix_final())


if __name__ == '__main__':
    unittest.main()
