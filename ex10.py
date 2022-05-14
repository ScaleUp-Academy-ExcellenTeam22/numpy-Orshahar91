import numpy as np


def identity_matrix():
    """
    Creates the 3-D identity matrix.
    :return: The matrix.
    """
    return np.identity(3)


if __name__ == "__main__":
    print(identity_matrix())
