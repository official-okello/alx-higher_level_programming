#!/usr/bin/python3


"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for Unittest"""

    def test_normal_list(self):
        """tests a normal list"""

        lista = [1, 2, 3, 4]
        self.assertEqual(max_integer(lista), 4)
        self.assertEqual(max_integer([[1230], [2321], [6534], [5432]]), [6534])

    def test_with_string(self):
        """tests with integer"""

        with self.assertRaises(TypeError):
            lista = [1, "andrea", 3, 4]
            max_integer(lista)
        with self.assertRaises(TypeError):
            max_integer(4, 5)
        with self.assertRaises(TypeError):
            max_integer(["Yupi", 11, 4, -21.5, "7"])

    def test_with_negative(self):
        """tests with negative number"""

        lista = [1, 2, 3, -4]
        self.assertEqual(max_integer(lista), 3)
        self.assertEqual(max_integer([-1, -2, -5, -7]), -1)
        self.assertEqual(max_integer([7, -7, -7, 7]), 7)

    def empty_list(self):
        """tests with empty list"""

        lista = []
        self.assertIsNone(max_integer(lista))

    def test_OneElement(self):
        """tests with one element"""

        self.assertEqual(max_integer([33]), 33)
