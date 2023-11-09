#!/usr/bin/python3
""" Defines a function for reading file content"""


def read_file(filename=""):
    """print the contents with utf encoding to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
