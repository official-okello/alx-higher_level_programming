#!/usr/bin/python3


"""Module that prints a text with 2 new lines after each of the characters ., ? and :"""


def text_indentation(text):
   """Function that prints a text with 2 new lines after each of the characters ., ? and :"""

    charPrinted = False
    if type(text) != str:
        raise TypeError("text must be a string")
    for letter in text:
        if charPrinted and letter == ' ':
            charPrinted = False
        else:
            if letter == '.' or letter == '?' or letter == ':':
                print(letter, end='')
                print()
                print()
                charPrinted = True
            else:
                print(letter, end='')
