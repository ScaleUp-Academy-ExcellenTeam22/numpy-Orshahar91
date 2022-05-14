import numpy as np


def get_median(array):
    """
    Compute the median of a given array.
    :param array: A given array.
    :return: Median.
    """
    return np.median(array)


if __name__ == "__main__":
    random_array = np.random.randint(0, 100, 10)
    print(random_array)
    print(get_median(random_array))
