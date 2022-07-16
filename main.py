#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Google Functions executor for password generator.

Creates a flask endpoint to generate an xkcd-ish password using Google Functions.

Author: Abdul Rahman Dabbour
License: MIT
"""

import flask
import functions_framework

import passgen
import entropy


def str_to_bool(string: str) -> bool:
    """Converts argument parsed as str to a bool.
    Args:
        query_str (str): Argument as str.
    Returns:
        Argument as bool.
    """

    if string.lower() in ["true", "t", "1"]:
        return True
    if string.lower() in ["false", "f", "0"]:
        return False
    raise ValueError(f"Could not parse '{string}' to bool type.")


def valid_delimited(string: str) -> bool:
    """Converts argument parsed as str to a bool.
    Args:
        query_str (str): Argument as str.
    Returns:
        Argument as bool.
    """

    if string.lower() in ["true", "t", "1"]:
        return True
    if string.lower() in ["false", "f", "0"]:
        return False
    raise ValueError(f"Could not parse '{string}' to bool type.")


@functions_framework.http
def generate_password(request: flask.Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    word_count = request.args.get("word_count", default=2, type=int)
    delimiter = request.args.get("delimiter", default="-", type=str)
    contains_number = request.args.get(
        "contains_number", default=True, type=str_to_bool
    )
    title_case = request.args.get("title_case", default=True, type=str_to_bool)
    report_params = request.args.get("report_params", default=False, type=str_to_bool)
    report_entropies = request.args.get(
        "report_entropies", default=False, type=str_to_bool
    )

    password = passgen.passgen(
        word_count=word_count,
        delimiter=delimiter,
        contains_number=contains_number,
        title_case=title_case,
    )

    res = {"password": password}

    if report_entropies:
        res.update(
            {
                "entropy": entropy.shannon_entropy(password),
                "ideal_entropy": entropy.ideal_shannon_entropy(len(password)),
            }
        )

    if report_params:
        res.update(
            {
                "settings": {
                    "word_count": word_count,
                    "delimiter": delimiter,
                    "contains_number": contains_number,
                    "title_case": title_case,
                    "report_params": report_params,
                    "report_entropies": report_entropies,
                }
            }
        )

    return res
