#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Shannon entropies.

Taken from https://stackoverflow.com/a/2979208/8295404.

Author: Abdul Rahman Dabbour
License: MIT
"""

import math


def shannon_entropy(string: str) -> float:
    """Calculates the Shannon entropy of a string.

    Taken from https://stackoverflow.com/a/2979208/8295404.

    Args:
        string (str): The query string.
    Returns:
        Shannon entropy of string.
    """

    prob = [
        float(string.count(c)) / len(string)
        for c in dict.fromkeys(list(string))
    ]

    entropy = -sum(p * math.log(p) / math.log(2.0) for p in prob)

    return entropy


def ideal_shannon_entropy(length: int) -> float:
    """Calculates the ideal Shannon entropy of a string with given length.

    Taken from https://stackoverflow.com/a/2979208/8295404.

    Args:
        length (int): The query length.
    Returns:
        Ideal Shannon entropy of string of given length.
    """

    prob = 1.0 / length

    return -1.0 * length * prob * math.log(prob) / math.log(2.0)
