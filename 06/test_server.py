import unittest
from mock import patch
import client
import server
import threading
import os
from io import StringIO

test_data = '''CLient started...
404 error: otvet.mail.ru/question/230876505
https://otvet.mail.ru/question/230876538{"": 7892, "=": 175, "<span": 130, "<a": 91, "</span>\n": 72, "\u0438": 70, "<div": 68}
404 error: fubiewbfiwufbuiewb
404 error: 1321421321'''

class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        self.client = client.client_on

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):        
        self.server_test = threading.Thread(target=server.server_on, args=(['server.py', '-w', '10', '-k', '7']))
        self.server_test.start()
        self.client(['client.py', '10', 'urls_test.txt'])
        self.assertEqual(mock_stdout.getvalue(), test_data)

