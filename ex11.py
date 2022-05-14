import numpy as np


def remove_single(given_shape):
    """
    Remove single-dimensional entries from a given shape.
    :param given_shape: Shape with entries.
    :return: The shape entries.
    """
    return np.squeeze(given_shape).shape


if __name__ == "__main__":
    shape = np.ones((3, 1, 4))
    print(remove_single(shape))
