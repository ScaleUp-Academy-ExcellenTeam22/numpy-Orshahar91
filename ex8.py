import numpy as np


def multiply_arrays(array1, array2):
    """
    Multiply two given arrays of same size element-by-element.
    :param array1: 1st array.
    :param array2: 2nd array.
    :return: The result of the multiplication.
    """
    return np.multiply(array1, array2)


if __name__ == "__main__":
    print(multiply_arrays([1, 2, 3], [2, 3, 4]))
