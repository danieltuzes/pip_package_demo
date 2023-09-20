"""Create a small example for the pip package demo.

Tests and documentation are available. This text is in the file
`my_mod.py`.
"""

import pandas as pd


def my_func(table_path: str, factor: float, ofile: str) -> None:
    """Process the input file with factor and write results.

    Parameters
    ----------
    table_path : str
        The path to the csv file storing columns A and B.
    factor : float
        A parameter read in from a config file.
    ofile : str
        The path to the result file.

    Returns
    -------
    pd.DataFrame
        The processed file the result.
    """
    data = pd.read_csv(table_path, dtype=float)
    data["result"] = data["A"]+factor*data["B"]
    data.to_csv(ofile, index=False)
