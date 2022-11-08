import sys
import socket
import asyncio


async def fetch(url, sem):
    async with sem:
        host = socket.gethostname()
        port = 8888
        s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_sock.connect((host, port))
        s_sock.send(bytes(url, encoding="utf-8"))
        while True:
            try:
                data = s_sock.recv(1024)
                if data is None:
                    break
                print(data.decode('utf-8'))
                break
            except ValueError as e_err:
                print(e_err)
                continue


async def client_on(base=None):
    workers_num = 10
    if base is None:
        base = sys.argv
        if base[1].isdigit():
            workers_num = int(base[1])
        else:
            raise Exception
    with open(base[2], 'r', encoding='utf-8') as file:
        file = [x.strip() for x in file.readlines()]
        sem = asyncio.Semaphore(workers_num)
        tasks = [
            asyncio.create_task(fetch(url, sem))
            for url in file
        ]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(client_on())
