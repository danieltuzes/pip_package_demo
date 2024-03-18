from pmdemo import my_mod
import pandas as pd


def test_my_mod():
    my_mod.my_func("tests/mytable.csv", 2, "tests/myres.csv")
    dat = pd.read_csv("tests/mytable.csv")
    truth = pd.read_csv("tests/myres.csv")
    pd.testing.assert_series_equal(
        dat["A"]+2*dat["B"], truth["result"].astype("int64").rename(None))
