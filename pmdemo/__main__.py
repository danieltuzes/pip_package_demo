"""This is executed by `python pmdemo` from the root,
or by `python -m pmdemo` for anywhere, if installed."""

import my_helper
import pmdemo


pmdemo.my_func("Greetings from main", [2,3])
print("Now call the dependency package, which is linked as git submodule")
my_helper.my_print_f()
