"""The one and only test.

Install the package to run the tests.
"""

import numpy
import pmdemo


def test_my_func():
    """Test the one and only function in the package."""
    assert pmdemo.my_func("empty") == 0

    my_arr = numpy.array([2, 3, 1, 0])
    assert pmdemo.my_func("not empty", my_arr) == 6
