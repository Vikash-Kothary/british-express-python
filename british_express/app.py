#!/usr/bin/env python3
"""
app.py - Creates the flask web server
"""

from flask import Flask
import os


def create_app():
    """
    """
    app = Flask(__name__, static_folder='static', static_url_path='')
    return app
