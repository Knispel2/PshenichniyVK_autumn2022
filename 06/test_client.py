import unittest
from mock import patch
import client
import server
import threading
from io import StringIO


class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = client.client_on
        self.server_test = threading.Thread(target=server.server_on, args=(['server.py', '-w', '10', '-k', '7']))

    @patch('sys.stdout', new_callable=StringIO)
    def main_test(self, mock_stdout):
        self.server_test.start()
        self.client(['client.py', '10', 'urls.txt'])
        buf = mock_stdout.getvalue().split('/n')
        self.assertEqual(len(buf), 101)
