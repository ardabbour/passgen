#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""xkcd-ish Password Generator Function. https://xkcd.com/936/

Generates an xkcd-ish style of password.

    Typical usage example:

    pass = passgen() # customized xkcd style
    pass = passgen(4, " ", False, False) # xkcd style

Author: Abdul Rahman Dabbour
License: MIT
"""

import secrets
import string

import words


def passgen(
    word_count: int = 2,
    delimiter: str = "-",
    contains_number: bool = True,
    title_case: bool = True,
) -> str:
    """xkcd-ish Password Generator Function. https://xkcd.com/936/
    Args:
        word_count (int): Number of words must be 1 > word_count > 9.
        delimiter (str): Delimiter between words; must be empty space or in
                         `string.punctuation`.
        contains_number (bool): Adds a number in the range [0, 100) if true.
        title_case (bool): Makes each word in the password Title Case.
    Returns:
        The generated password
    """

    assert isinstance(word_count, int)
    assert isinstance(delimiter, str)
    assert isinstance(contains_number, bool)
    assert isinstance(title_case, bool)

    if word_count < 1 or word_count > 9:
        raise ValueError("Number of words in range (1, 10)!")

    if len(delimiter) != 1:
        raise ValueError("Delimiter must be a single character!")

    if delimiter not in string.punctuation + " ":
        raise ValueError(
            "Delimiter must be empty space or `string.punctuation`!"
        )

    base_pass = [secrets.choice(words.WORDS) for _ in range(word_count)]

    if title_case:
        base_pass = [x.title() for x in base_pass]

    if contains_number:
        pos = round(word_count / 2.0)
        base_pass[pos:pos] = [str(secrets.randbelow(100))]

    return delimiter.join(base_pass)
