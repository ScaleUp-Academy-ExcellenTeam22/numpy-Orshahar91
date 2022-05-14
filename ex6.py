import numpy as np


def swap_rows(array):
    """
    Creates a new array from the given array by swapping first and last rows.
    :param array: The original array.
    :return: The new array.
    """
    return array[::-1]


if __name__ == "__main__":
    random_array = np.random.randint(100, size=(4, 4))
    print(random_array, "\n")
    print(swap_rows(random_array))
