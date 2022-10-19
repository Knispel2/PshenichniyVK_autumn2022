import socket
import unittest
from unittest.mock import MagicMock
import mock
from mock import patch
import server
from io import StringIO

test_data = "b'404 error: https://otvet.mail.ru/question/230876528' test"

class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_server_on(self, mock_stdout):
        with patch('socket.socket.send'), patch('socket.socket.bind'):
            with patch('socket.socket.recv') as resv_mock, patch('socket.socket.accept') as acc_mock:
                with patch('socket.socket.listen'), patch('socket.socket.listen'), patch('server.server_process'):
                    acc_mock.return_value = [1, 1]
                    resv_mock.side_effect = [b'https://otvet.mail.ru/question/230876528'] + [None]*2
                    server.server_on(['server.py', '-w', '10', '-k', '7'])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_processing_url(self, mock_stdout):
        test_obj = MagicMock()
        test_obj.sendto = print
        server.processing_url('https://otvet.mail.ru/question/230876528', 'test', 7, test_obj)
        buf = mock_stdout.getvalue().strip('\n')
        self.assertEqual(test_data, buf)
