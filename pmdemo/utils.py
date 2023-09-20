import argparse
from configparser import ConfigParser, ExtendedInterpolation
import logging
import os
import sys

from typing import List

import pmdemo


def parse_args(arg_list: List[str]) -> argparse.Namespace:
    """Define the arguments and parse the input.

    Parameters
    ----------
    arg_list : List[str]
        The string to parse, e.g. the argv passed to the program.

    Returns
    -------
    argparse.Namespace
        The object from where the expected values can be read.
    """
    parser = argparse.ArgumentParser(description=("This is pmdemo, version "
                                                  f"{pmdemo.__version__}"))

    parser.add_argument('--Master_Config',
                        help=('The file that stores the '
                              'input and output files. '
                              '(default: %(default)s)'),
                        default="config/MasterConfig.cfg",
                        metavar="path_to/MasterConfig.cfg")

    logging.info("Arguments are parsed")
    return parser.parse_args(arg_list)


def parse_conf(path: str) -> ConfigParser:
    """Read in a python cfg file using ExtendedInterpolation."""
    conf = ConfigParser(os.environ,
                        interpolation=ExtendedInterpolation())
    with open(path, 'r', encoding="utf-8") as ifile:
        conf.read_file(ifile)

    logging.info("Config file %s is parsed", path)
    return conf


def set_log(fname: str):
    """Set logging and tee to a file.

    Parameters
    ----------
    fname : str
        The file where the log should go.
    """
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(fname),
                            logging.StreamHandler()
                        ])

    def _excepthook(type_, value, traceback):
        """Capturing exceptions."""
        logging.critical("Uncaught exception",
                         exc_info=(type_, value, traceback))

    sys.excepthook = _excepthook
    logging.info("Logging and the logfile is set up.")
