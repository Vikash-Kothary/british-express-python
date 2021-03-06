#!/usr/bin/env python3
"""
views.py - Serve webpages
"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def root():
    """Root for website"""
    title = 'British Express'
    return render_template("index.html", title=title)
