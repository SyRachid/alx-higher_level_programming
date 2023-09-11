#!/usr/bin/python3
""" this module returns a list of available attributes and methods
    of an object"""


def lookup(obj):
    """return a list of attributes and methods of
    an object"""
    return [name for name in dir(obj)]
