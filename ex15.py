import numpy as np


def sort_by_height(students_id, students_height):
    """
    Sort the given arrays by the height of the students, print the integer indices that describes the sort
    order, and the sorted data.
    :param students_id: The array of the student's id.
    :param students_height: The array of the student's height
    """
    indices = np.lexsort((students_id, students_height))
    print("Indices:", "\n", indices)
    sorted_data = [(students_id[index], students_height[index]) for index in indices]
    print("Sorted data:", "\n", sorted_data)


if __name__ == "__main__":
    student_id = np.array([20657778, 9754381, 12347263, 3467912])
    student_height = np.array([195, 167, 183, 203])
    sort_by_height(student_id, student_height)
