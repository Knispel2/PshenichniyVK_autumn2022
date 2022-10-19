import socket
import unittest
from mock import patch
import client
from io import StringIO



class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_processing_url(self, mock_stdout):
        with patch('socket.socket.send') as send_mock:
            with patch('socket.socket.recv') as resv_mock:
                send_mock.return_value = b'{}'
                resv_mock.return_value = b'{}'
                client.processing_url('', socket.socket())
                buf = mock_stdout.getvalue().strip('\n')
                self.assertEqual('{}', buf)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_client_on(self, mock_stdout):
        with patch('socket.socket.send') as send_mock:
            with patch('socket.socket.recv') as resv_mock:
                with patch('socket.socket.connect'):
                    send_mock.return_value = b'{}'
                    resv_mock.return_value = b'{}'
                    client.client_on(['client.py', '10', 'urls_test.txt'])
