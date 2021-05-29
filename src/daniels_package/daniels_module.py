"""Create a small example for the pip package demo.

Tests and documentation are available.
"""

import sys
import numpy

__version__ = "1.0.13"  # the version info for the package used by setup.cfg


def my_func(my_text: str = "", my_arr: numpy.ndarray = None) -> int:
    """Print out some debug info and return the sum of the array or 0 if none.

    Parameters
    ----------
    my_text : str, optional
        A text that is printed out, by default ""
    my_arr : numpy.ndarray, optional
        The sum of the array is printed out if set, by default None

    Returns
    -------
    int
        The sum of my_arr if set, 0 otherwise.

    """
    print(f"sys.argv = {sys.argv}")
    print(f"sys.path = {sys.path}")
    print(f"Function input = {my_text}")
    if my_arr is not None:
        arr_sum = numpy.sum(my_arr)
        print(f"Sum: {arr_sum}")
        return arr_sum

    return 0


if __name__ == "__main__":
    my_func("From main", numpy.array([1, 1, 1, 1]))
