import numpy as np


def sort_array(array):
    """
    Sort the given array along the first, and last axis.
    :param array: Given array.
    """
    print("Original array:", "\n", array)
    print("Sort along the first axis:", "\n", np.sort(array, axis=0))
    print("Sort along the last axis:", "\n", np.sort(array))


if __name__ == "__main__":
    array_to_sort = [[2, 5], [4, 4]]
    sort_array(array_to_sort)
