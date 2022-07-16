#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Local tester for debug purposes.

Creates a flask endpoint to generate an xkcd-ish password.

Author: Abdul Rahman Dabbour
License: MIT
"""

from flask import Flask, request
import main

app = Flask(__name__)


@app.get("/generate_password")
def generate_password() -> None:
    """Reroutes a request to the main file."""
    return main.generate_password(request)
