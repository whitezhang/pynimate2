from typing import Union
import numpy as np


def human_readable(num: Union[float, int], precision: int = 2, *args) -> str:
    """Converts large numeric values(>10^3) into human readable strings.
    `ie. 1000 -> 1k`,
    `1000000 -> 1M`, etc. `args` are passed to function formatter

    Parameters
    ----------
    num : Union[float, int]
        Numeric value
    precision : int, optional
        Rounding precision, by default 2

    Returns
    -------
    str
        Human readable numeric string
    """
    if num == np.nan:
        return ""
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return f'{np.round(num, 2)}{["", "K", "M", "B", "T", "Q"][magnitude]}'
