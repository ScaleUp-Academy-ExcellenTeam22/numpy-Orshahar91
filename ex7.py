import numpy as np


def replace_numbers(array, number):
    """
    Replace all numbers in a given array which is equal, less or greater to a given number.
    :param array: The original array.
    :param number: The given number.
    """
    replacement_number = -1
    print(np.where(array == number, replacement_number, array))
    print(np.where(array < number, replacement_number, array))
    print(np.where(array > number, replacement_number, array))


if __name__ == "__main__":
    random_array = np.random.randint(0, high=10, size=10)
    print(random_array, "\n")
    replace_numbers(random_array, 5)
