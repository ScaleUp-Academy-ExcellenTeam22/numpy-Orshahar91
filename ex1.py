import numpy as np


def random_values():
    """
    Create a vector of length 10 with values evenly distributed between 5 and 50.
    :return: The vector.
    """
    return np.random.randint(5, 55, 10)


if __name__ == "__main__":
    print(random_values())
