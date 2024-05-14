"""
This module is intended to use in testing pylint.

We create simple functions to simulate enviroment in which we would use pylint.
"""

import pandas as pd
import numpy as np


def generateRandomDfPoisson(
    dfLen: int,
    poissLambda: float = 1,
    someLongParameterToTestBlack: list[list[str]] = None,
) -> pd.DataFrame:
    """
    This function generates random pandas.DataFrame with dimesions dfLen x 1.
    Used distribution is Poisson with lambda = poissLambda

    Args:
    dfLen
        number of rows to generate
    poissLambda
        lambda parameter to use in Poisson
    """
    _arr = np.random.poisson(lam=poissLambda, size=dfLen)
    someLongParameterToTestBlack = [["one", "two", "three"], ["four", "five", "six"]]

    for myString in someLongParameterToTestBlack:
        print(f"Printing my string: {myString}")
        
    print("lalalalla")
    print("lalalalla")
    print("lalalalla")
    print("lalalalla")
    print("lalalalla")
    print("lalalalla")

    _output = pd.DataFrame({"col1": _arr})
    return _output


if __name__ == "__main__":
    print(generateRandomDfPoisson(10, 1))
    print("elo")
