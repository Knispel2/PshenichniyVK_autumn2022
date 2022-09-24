import unittest
import sys
import os
import Custom_list


class TestJSON(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_sub(self):
        self.assertEqual(Custom_list([5, 1, 3, 7]) - Custom_list([1, 2, 7]), Custom_list([4, -1, -4, 7]))

    def test_add(self):
        self.assertEqual(Custom_list([5, 1, 3, 7]) - Custom_list([1, 2, 7]), Custom_list([6, 3, 10, 7]))

    def test_not_is(self):

    def test_sub_list(self):

    def test_add_list(self):

    def test_not_is(self):
