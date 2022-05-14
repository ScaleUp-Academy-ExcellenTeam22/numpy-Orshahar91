import numpy as np


def add_vector(matrix, vector):
    """
    Adds a given vector to each row of a given matrix.
    :param matrix: The original matrix.
    :param vector: The vector to add to each row.
    :return: The altered matrix.
    """
    return np.asarray(matrix) + np.asarray(vector)


if __name__ == "__main__":
    original_matrix = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
    vector_to_add = [1, 0, 1]
    print(add_vector(original_matrix, vector_to_add))
