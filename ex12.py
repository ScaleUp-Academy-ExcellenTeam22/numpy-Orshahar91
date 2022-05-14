import numpy as np


def convert_1d_into_2d(array1, array2):
    """
    Converts 2 1-D arrays into a 2-D array.
    :param array1: 1st array.
    :param array2: 2nd array.
    :return: The 2-D array.
    """
    return np.dstack((array1, array2))


if __name__ == "__main__":
    print(convert_1d_into_2d([10, 20, 30], [40, 50, 60]))
