import unittest
import sys
import os
import Custom_list

class Test_Clist(unittest.TestCase):
    def setUp(self) -> None:
        self.Custom_list = Custom_list.Custom_list

    def test_sub(self):
        self.assertEqual(self.Custom_list([5, 1, 3, 7]) - self.Custom_list([1, 2, 7]), self.Custom_list([4, -1, -4, 7]))
        self.assertIsInstance(self.Custom_list([5, 1, 3, 7]) - self.Custom_list([1, 2, 7]), type(self.Custom_list([4, -1, -4, 7])))

    def test_add(self):
        self.assertEqual(self.Custom_list([5, 1, 3, 7]) + self.Custom_list([1, 2, 7]), self.Custom_list([6, 3, 10, 7]))
        self.assertIsInstance(self.Custom_list([5, 1, 3, 7]) + self.Custom_list([1, 2, 7]), type(self.Custom_list([6, 3, 10, 7])))


    def test_sub_list(self):
        self.assertEqual(self.Custom_list([5, 1, 3, 7]) - [1, 2, 7], self.Custom_list([4, -1, -4, 7]))
        self.assertEqual([5, 1, 3, 7] - self.Custom_list([1, 2, 7]), self.Custom_list([4, -1, -4, 7]))
        self.assertIsInstance(self.Custom_list([5, 1, 3, 7]) - [1, 2, 7], type(self.Custom_list([4, -1, -4, 7])))
        self.assertIsInstance([5, 1, 3, 7] - self.Custom_list([1, 2, 7]), type(self.Custom_list([4, -1, -4, 7])))

    def test_add_list(self):
        self.assertEqual([5, 1, 3, 7] + self.Custom_list([1, 2, 7]), self.Custom_list([6, 3, 10, 7]))
        self.assertEqual(self.Custom_list([5, 1, 3, 7]) + [1, 2, 7], self.Custom_list([6, 3, 10, 7]))
        self.assertIsInstance([5, 1, 3, 7] + self.Custom_list([1, 2, 7]), type(self.Custom_list([6, 3, 10, 7])))
        self.assertIsInstance(self.Custom_list([5, 1, 3, 7]) + [1, 2, 7], type(self.Custom_list([6, 3, 10, 7])))

    def test_str(self):
        self.assertEqual(str(self.Custom_list([1,1,1])), "[1, 1, 1], 3")