import numpy as np


def negate_range_array():
    """
     Using NumPy to create vector with values 0-20 and changing the sign
     of the numbers in the range 9-15.
     :return: The array.
    """
    array = np.arange(21)
    array[9:16] *= -1
    return array


if __name__ == "__main__":
    print(negate_range_array())
