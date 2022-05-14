import numpy as np
import matplotlib.pyplot as plt


def french_flag():
    """
    Creates the French flag using NumPy, and convert it to an image.
    """
    blue = [0, 0, 255]
    white = [255, 255, 255]
    red = [255, 0, 0]
    mask = np.zeros((400, 600), dtype=int)
    mask[:, 200:400] = 1
    mask[:, 400:] = 2
    flag = np.full((400, 600, 3), 255, dtype=np.uint8)
    flag[mask == 0] = blue
    flag[mask == 1] = white
    flag[mask == 2] = red
    plt.imshow(flag)
    plt.show()
    plt.imsave("French_Flag.png", flag)


if __name__ == "__main__":
    french_flag()
