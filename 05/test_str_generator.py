# coding=windows-1251
import unittest
from io import StringIO
from mock import patch
import str_generator


class TestSTR(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = str_generator.str_generator
        self.test_data = '''а Роза упала на лапу Азора
Октябрь уж наступил — уж роща отряхает
Последние листы с нагих своих ветвей;
Дохнул осенний хлад — дорога промерзает.
Журча еще бежит за мельницу ручей,
Но пруд уже застыл; сосед мой поспешает
В отъезжие поля с охотою своей,
И страждут озими от бешеной забавы,
И будит лай собак уснувшие дубравы.'''
        self.file = StringIO(self.test_data)


    def test_empty(self):
        filter_data = []
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), [])

    def test_one(self):
        filter_data = ['роз']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), [])

    def test_two(self):
        filter_data = ['роза']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['а Роза упала на лапу Азора'])

    def test_three(self):
        filter_data = ['роЗа']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['а Роза упала на лапу Азора'])

    def test_four(self):
        filter_data = ['роза', 'бежит']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['а Роза упала на лапу Азора',
                                              'Журча еще бежит за мельницу ручей,'])
