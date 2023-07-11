#!/usr/bin/python3
"""The write_file module container"""


def write_file(filename="", text=""):
    """ Writes a string to a text file """

    with open(filename, "w", encoding="utf-8") as file:
        files = file.write(text)
        return (files)
