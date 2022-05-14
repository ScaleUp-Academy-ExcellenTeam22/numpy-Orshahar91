import numpy as np


def number_of_days(month, year):
    """
    Count the number of days of a specific month.
    :param month: Month.
    :param year: Year.
    :return: Number of days.
    """
    start_of_next_month = str(year) + "-" + "0" + str(month + 1) + "-" + "01"
    current_month = str(year) + "-" + "0" + str(month) + "-" + "01"
    return np.datetime64(start_of_next_month) - np.datetime64(current_month)


if __name__ == "__main__":
    print(number_of_days(2, 2016))
    print(number_of_days(2, 2017))
    print(number_of_days(2, 2018))

