import unittest
import copy
import custom_list


def eq_check(a_data, b_data):
    if len(a_data) != len(b_data):
        return False
    len_data = len(a_data)
    for i in range(len_data):
        if a_data[i] != b_data[i]:
            return False
    return True


class TestClist(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_list = custom_list.Customlist

    def test_sub(self):
        a_data = self.custom_list([5, 1, 3, 7])
        b_data = self.custom_list([1, 2, 7])
        a_buf = copy.copy(a_data)
        b_buf = copy.copy(b_data)
        self.assertTrue(eq_check(a_data - b_data,
                         self.custom_list([4, -1, -4, 7])))
        self.assertTrue(eq_check(b_data - a_data,
                    self.custom_list([-4, 1, 4, -7])))
        self.assertIsInstance(a_data - b_data,
                              type(self.custom_list([4, -1, -4, 7])))
        self.assertTrue(eq_check(a_data, a_buf))
        self.assertTrue(eq_check(b_data, b_buf))

    def test_add(self):
        a_data = self.custom_list([5, 1, 3, 7])
        b_data = self.custom_list([1, 2, 7])
        a_buf = copy.copy(a_data)
        b_buf = copy.copy(b_data)
        self.assertTrue(eq_check(a_data + b_data,
                         self.custom_list([6, 3, 10, 7])))
        self.assertTrue(eq_check(b_data + a_data,
                    self.custom_list([6, 3, 10, 7])))
        self.assertIsInstance(a_data + b_data,
                              type(self.custom_list([6, 3, 10, 7])))
        self.assertTrue(eq_check(a_data, a_buf))
        self.assertTrue(eq_check(b_data, b_buf))

    def test_sub_list(self):
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        a_buf = copy.copy(a_data)
        b_buf = copy.copy(b_data)
        a_buf_list = copy.copy(a_list)
        b_buf_list = copy.copy(b_list)
        self.assertTrue(eq_check(a_data - b_list,
                         self.custom_list([4, -1, -4, 7])))
        self.assertTrue(eq_check(a_list - b_data,
                         self.custom_list([4, -1, -4, 7])))
        self.assertIsInstance(a_data - b_list,
                              type(self.custom_list([4, -1, -4, 7])))
        self.assertIsInstance(a_list - b_data,
                              type(self.custom_list([4, -1, -4, 7])))
        self.assertTrue(eq_check(a_data, a_buf))
        self.assertTrue(eq_check(b_data, b_buf))
        self.assertTrue(eq_check(a_list, a_buf_list))
        self.assertTrue(eq_check(b_list, b_buf_list))

    def test_add_list(self):
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        a_buf = copy.copy(a_data)
        b_buf = copy.copy(b_data)
        a_buf_list = copy.copy(a_list)
        b_buf_list = copy.copy(b_list)
        self.assertTrue(eq_check(a_list + b_data,
                         self.custom_list([6, 3, 10, 7])))
        self.assertTrue(eq_check(a_data + b_list,
                         self.custom_list([6, 3, 10, 7])))
        self.assertIsInstance(a_list + b_data,
                              type(self.custom_list([6, 3, 10, 7])))
        self.assertIsInstance(a_data + b_list,
                              type(self.custom_list([6, 3, 10, 7])))
        self.assertTrue(eq_check(a_data, a_buf))
        self.assertTrue(eq_check(b_data, b_buf))
        self.assertTrue(eq_check(a_list, a_buf_list))
        self.assertTrue(eq_check(b_list, b_buf_list))

    def test_str(self):
        self.assertEqual(str(self.custom_list([1, 1, 1])), "[1, 1, 1], 3")

    def test__t__(self):
        '''x < y'''
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        self.assertTrue(a_list>b_data)
        self.assertTrue(a_data>b_list)
        self.assertTrue(a_list>b_list)
        self.assertTrue(a_data>b_data)
        self.assertFalse(b_data>a_list)
        self.assertFalse(b_list>a_data)
        self.assertFalse(b_list>a_list)
        self.assertFalse(b_data>a_data)

    def test__e__(self):
        '''x ≤ y'''
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        self.assertFalse(a_list<=b_data)
        self.assertFalse(a_data<=b_list)
        self.assertFalse(a_list<=b_list)
        self.assertFalse(a_data<=b_data)
        self.assertTrue(b_data<=a_list)
        self.assertTrue(b_list<=a_data)
        self.assertTrue(b_list<=a_list)
        self.assertTrue(b_data<=a_data)

    def test__eq__(self):
        '''x == y'''
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        c_data = self.custom_list([5, 11])
        c_list = [5, 11]
        self.assertTrue(a_data == c_data)
        self.assertTrue(a_data == c_list)
        self.assertFalse(a_data == b_data)
        self.assertFalse(a_data == b_list)
        self.assertTrue(c_data == a_data)
        self.assertTrue(c_list == a_data)
        self.assertFalse(b_data == a_data)
        self.assertFalse(b_list == a_data)
        self.assertTrue(a_list == c_data)
        self.assertFalse(a_list == b_data)
        self.assertTrue(c_data == a_list)
        self.assertFalse(b_data == a_list)

    def test__ne__(self):
        '''x != y'''
        a_data = self.custom_list([5, 1, 3, 7])
        a_list = [5, 1, 3, 7]
        b_data = self.custom_list([1, 2, 7])
        b_list = [1, 2, 7]
        c_data = self.custom_list([5, 11])
        c_list = [5, 11]
        self.assertFalse(a_data != c_data)
        self.assertFalse(a_data != c_list)
        self.assertTrue(a_data != b_data)
        self.assertTrue(a_data != b_list)
        self.assertFalse(c_data != a_data)
        self.assertFalse(c_list != a_data)
        self.assertTrue(b_data != a_data)
        self.assertTrue(b_list != a_data)
        self.assertFalse(a_list != c_data)
        self.assertTrue(a_list != b_data)
        self.assertFalse(c_data != a_list)
        self.assertTrue(b_data != a_list)
