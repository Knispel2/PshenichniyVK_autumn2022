from __future__ import with_statement
import asyncio
import socket
from collections import Counter
import json
import aiohttp


async def server_process(client, top_num, flag=False):
    async with aiohttp.ClientSession() as session:
        loop = asyncio.get_event_loop()
        request = 'Start'
        while request is not None:
            request = (await loop.sock_recv(client, 1024)).decode('utf8')
            async with session.get(request) as resp:
                html = await resp.read()
                words = Counter(html)
                words = dict(words.most_common(top_num))
                response = json.dumps(words)
                if flag:
                    print(response)
                    break
            await loop.sock_sendall(client, response.encode('utf8'))
        client.close()


async def server_on():
    workers_num = 10
    top_num = 7
    # base = sys.argv if input_data is None else input_data
    # if base[1] == '-c':
    # workers_num = int(base[2])
    host = ''
    port = 8888
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock.bind((host, port))
    s_sock.setblocking(False)
    print('Server started...')
    s_sock.listen(workers_num)
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(s_sock)
        loop.create_task(server_process(client, top_num))


if __name__ == '__main__':
    asyncio.run(server_on())
