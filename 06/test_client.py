import unittest
from mock import patch
import client
import server
import threading
import os
from io import StringIO


class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = client.client_on

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        os.system('python server.py -w 10 -k 7')
        self.client(['client.py', '10', 'urls.txt'])
        buf = mock_stdout.getvalue().split('/n')
        self.assertEqual(len(buf), 101)
