import unittest
import desc_work


class TestDesc(unittest.TestCase):
    def setUp(self) -> None:
        self.desc_class = desc_work.Data

    def test_num(self):
        test_obj = self.desc_class()
        with self.assertRaises(ValueError):
            test_obj.num = 'test'
        test_obj.num = 5
        self.assertEqual(test_obj.num, 5)

    def test_name(self):
        test_obj = self.desc_class()
        with self.assertRaises(ValueError):
            test_obj.name = 3
        test_obj.name = 'test'
        self.assertEqual(test_obj.name, 'test')

    def test_price(self):
        test_obj = self.desc_class()
        with self.assertRaises(ValueError):
            test_obj.price = 'test'
            test_obj.price = -2
        test_obj.price = 5
        self.assertEqual(test_obj.price, 5)
