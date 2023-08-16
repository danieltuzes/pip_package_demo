"""Create a small example for the pip package demo.

Tests and documentation are available. This text is in the file
`my_mod.py`.
"""

import sys
import numpy

__version__ = "2.0.0"  # the version info for the package used by setup.cfg


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
    print(f"Function str input = {my_text}")
    with open("mydata.txt", encoding="utf-8") as ifile:
        for line in ifile:
            print(line)
    if my_arr is not None:
        arr_sum = numpy.sum(my_arr)
        print(f"Sum: {arr_sum}")
        return arr_sum

    return 0
