import unittest
import custom_list


class TestClist(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list = custom_list.Customlist

    def test_sub(self):
        self.assertEqual(self.custom_list([5, 1, 3, 7]) -
                         self.custom_list([1, 2, 7]),
                         self.custom_list([4, -1, -4, 7]))
        self.assertIsInstance(self.custom_list([5, 1, 3, 7]) -
                              self.custom_list([1, 2, 7]),
                              type(self.custom_list([4, -1, -4, 7])))

    def test_add(self):
        self.assertEqual(self.custom_list([5, 1, 3, 7]) +
                         self.custom_list([1, 2, 7]),
                         self.custom_list([6, 3, 10, 7]))
        self.assertIsInstance(self.custom_list([5, 1, 3, 7]) +
                              self.custom_list([1, 2, 7]),
                              type(self.custom_list([6, 3, 10, 7])))

    def test_sub_list(self):
        self.assertEqual(self.custom_list([5, 1, 3, 7]) - [1, 2, 7],
                         self.custom_list([4, -1, -4, 7]))
        self.assertEqual([5, 1, 3, 7] - self.custom_list([1, 2, 7]),
                         self.custom_list([4, -1, -4, 7]))
        self.assertIsInstance(self.custom_list([5, 1, 3, 7]) - [1, 2, 7],
                              type(self.custom_list([4, -1, -4, 7])))
        self.assertIsInstance([5, 1, 3, 7] - self.custom_list([1, 2, 7]),
                              type(self.custom_list([4, -1, -4, 7])))

    def test_add_list(self):
        self.assertEqual([5, 1, 3, 7] + self.custom_list([1, 2, 7]),
                         self.custom_list([6, 3, 10, 7]))
        self.assertEqual(self.custom_list([5, 1, 3, 7]) + [1, 2, 7],
                         self.custom_list([6, 3, 10, 7]))
        self.assertIsInstance([5, 1, 3, 7] + self.custom_list([1, 2, 7]),
                              type(self.custom_list([6, 3, 10, 7])))
        self.assertIsInstance(self.custom_list([5, 1, 3, 7]) + [1, 2, 7],
                              type(self.custom_list([6, 3, 10, 7])))

    def test_str(self):
        self.assertEqual(str(self.custom_list([1, 1, 1])), "[1, 1, 1], 3")
