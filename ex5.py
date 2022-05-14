import numpy as np
import matplotlib.pyplot as plt


def plot_points_sine_curve(x):
    """
    Compute the x and y coordinates for points on a sine curve and plot
    the points.
    :param x: Array of x-axis values.
    """
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    x_axis_coordinates = np.arange(0, 10, 0.3)
    plot_points_sine_curve(x_axis_coordinates)
