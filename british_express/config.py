#!/usr/bin/env python3
"""
config.py - Configuartion variables
"""

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


class Config(object):
    FB_USERNAME = os.getenv('FB_USERNAME', None)
    FB_PASSWORD = os.getenv('FB_PASSWORD', None)
