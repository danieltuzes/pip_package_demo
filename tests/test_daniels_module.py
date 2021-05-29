"""The one and only test.

Install the package, e.g. in editable mode to run the tests.
"""

import numpy
from daniels_package import daniels_module  # it is a namespace package


def test_my_func():
    """Test the one and only function in the package."""
    assert daniels_module.my_func("empty") == 0

    my_arr = numpy.array([2, 3, 1, 0])
    assert daniels_module.my_func("not empty", my_arr) == 6
