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
    title2 = 'The Only Intelligent Photo Gallery you need.'
    img = [{'./amazon.png'}, {'./mcdonalds.png'}, {'./yahoo.jpg'}]
    return render_template("index.html", title=title, title2=title2, img1=img)
