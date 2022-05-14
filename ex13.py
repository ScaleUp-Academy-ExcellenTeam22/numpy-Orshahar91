import numpy as np


def combine_arrays(one_dimensional_array, two_dimensional_array):
    """
    Combine a one and a two-dimensional array together and display their elements.
    :param one_dimensional_array: One dimensional array.
    :param two_dimensional_array: Two dimensional array.
    """
    array_iterator = np.nditer([one_dimensional_array, two_dimensional_array])
    for x, y in array_iterator:
        print(x, ":", y)


if __name__ == "__main__":
    array1 = [0, 1, 2, 3]
    array2 = [[0, 1, 2, 3], [4, 5, 6, 7]]
    print("One dimensional array:", "\n", array1)
    print("Two dimensional array:", "\n", array2)
    combine_arrays(array1, array2)
