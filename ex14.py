import numpy as np


def three_dimension():
    """
    Creates a three-dimension array with unsigned integers (0-255)
    :return: The array.
    """
    return np.random.randint(0, 255, size=(300, 400, 5), dtype=np.uintc)


if __name__ == "__main__":
    print(three_dimension())
