# coding=windows-1251
import unittest
from io import StringIO
from mock import patch
import str_generator


class TestSTR(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = str_generator.str_generator
        self.test_data = '''� ���� ����� �� ���� �����
������� �� �������� � �� ���� ��������
��������� ����� � ����� ����� ������;
������ ������� ���� � ������ ����������.
����� ��� ����� �� �������� �����,
�� ���� ��� ������; ����� ��� ���������
� �������� ���� � ������ �����,
� �������� ����� �� ������� ������,
� ����� ��� ����� �������� �������.'''
        self.file = StringIO(self.test_data)


    def test_empty(self):
        filter_data = []
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), [])

    def test_one(self):
        filter_data = ['���']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), [])

    def test_two(self):
        filter_data = ['����']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['� ���� ����� �� ���� �����'])

    def test_three(self):
        filter_data = ['����']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['� ���� ����� �� ���� �����'])

    def test_four(self):
        filter_data = ['����', '�����']
        with patch('str_generator.open') as open_mock:
            open_mock.return_value = self.file
            test_obj = self.generator(self.file, filter_data)
            self.assertEqual(list(test_obj), ['� ���� ����� �� ���� �����',
                                              '����� ��� ����� �� �������� �����,'])
