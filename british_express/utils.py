#!/usr/bin/env python3
"""
utils.py - Helper functions
"""
import os


def find_file(name):
    for root, dirs, files in os.walk('./'):
        if name in files:
            return os.path.join(root, name)


def save_json_to_file(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    pass
