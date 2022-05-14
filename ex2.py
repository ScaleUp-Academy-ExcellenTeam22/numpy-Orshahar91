import numpy as np


def get_rows_and_columns(matrix):
    """
    Finds the number of rows and columns of a given matrix.
    In case of a vector it finds the number of columns.
    :param matrix: Given matrix.
    :return: Dictionary containing rows and columns.
    """

    matrix = np.asarray(matrix)

    if matrix.ndim == 1:
        return {"Rows": 1, "Columns": matrix.shape[0]}

    rows, cols = matrix.shape
    return {"Rows": rows, "Columns": cols}


if __name__ == "__main__":
    print(get_rows_and_columns([[5, 6], [1, 2], [9, 7]]))
    print(get_rows_and_columns([5, 6, 7, 9]))
