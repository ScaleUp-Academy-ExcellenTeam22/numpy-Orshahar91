import numpy as np


def bordered_matrix():
    """
    Creates a 10x10 matrix that is bordered with 1's, and inside are 0's.
    :return: The bordered matrix.
    """
    matrix = np.ones((10, 10), dtype='int8')
    matrix[1:-1, 1:-1] = 0
    return matrix


if __name__ == "__main__":
    print(bordered_matrix())
