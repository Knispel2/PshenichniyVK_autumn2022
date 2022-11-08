import unittest
from io import StringIO
import asyncio
from mock import patch
import client


class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_processing_url(self, mock_stdout):
        with patch('socket.socket.send') as send_mock:
            with patch('socket.socket.recv') as resv_mock:
                send_mock.return_value = b'{}'
                resv_mock.return_value = b'{}'
                workers_num = 10
                client.fetch('', asyncio.Semaphore(workers_num))
                buf = mock_stdout.getvalue().strip('\n')
                self.assertEqual('', buf)

    def test_client_on(self):
        with patch('socket.socket.send') as send_mock:
            with patch('socket.socket.recv') as resv_mock:
                with patch('socket.socket.connect'):
                    send_mock.return_value = b'{}'
                    resv_mock.return_value = b'{}'
                    client.client_on(['client.py', '10', 'urls_test.txt'])
