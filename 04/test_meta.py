import unittest
import meta_class


class TestMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.meta = meta_class.CustomMeta

        class CustomClass(metaclass=self.meta):
            x = 50

            def __init__(self, val=99):
                self.val = val

            def line(self):
                return 100

            def __str__(self):
                return "Custom_by_metaclass"

        self.test_class = CustomClass()
        self.test_classs = CustomClass

    def test_cls_attr(self):
        self.assertEqual(self.test_class.custom_x, 50)

    def test_inst_attr(self):
        self.assertEqual(self.test_class.custom_val, 99)

    def test_clsmeth_attr(self):
        self.assertEqual(self.test_class.custom_line(), 100)

    def test_clss_attr(self):
        self.assertEqual(self.test_classs.custom_x, 50)

    def test_str(self):
        self.assertEqual(str(self.test_class), "Custom_by_metaclass")

    def test_dynamic(self):
        dynamic_test = self.test_classs()
        dynamic_test.dynamic = "added later"
        self.assertEqual(dynamic_test.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            print(dynamic_test.dynamic)

    def test_errors(self):
        with self.assertRaises(AttributeError):
            print(self.test_class.x)
            print(self.test_class.val)
            print(self.test_class.line())
            print(self.test_class.yyy)
            print(self.test_classS.x)
