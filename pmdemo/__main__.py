"""This is executed by `python pmdemo` from the root,
or by `python -m pmdemo` for anywhere, if installed."""

import logging
import sys
import time

import pmdemo
import my_helper


def main():
    """So that the main can be called after importing this module."""
    args = pmdemo.utils.parse_args(sys.argv[1:])
    conf = pmdemo.utils.parse_conf(args.Master_Config)
    pmdemo.utils.set_log(conf["outputs"]["log"])
    logging.info("Program ready to run, version %s", pmdemo.__version__)
    my_helper.my_print_f()

    params = pmdemo.utils.parse_conf(conf["inputs"]["params"])
    factor = params.getfloat("top", "factor")
    pmdemo.my_mod.my_func(conf["inputs"]["tables"],
                          factor,
                          conf["outputs"]["res"])
    sleep = int(params.get("top", "sleep", fallback="20"))

    for i in range(sleep):
        logging.info("asleep %d", i)
        time.sleep(1)

    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
