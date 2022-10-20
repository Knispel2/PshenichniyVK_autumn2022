import threading
import sys
import socket


def processing_url(url, s_sock):
    s_sock.send(bytes(url, encoding="utf-8"))
    while True:
        try:
            data = s_sock.recv(1024)
            if data is None:
                break
            print(data.decode('utf-8'))
            break
        except Exception as e_err:
            print(e_err)
            continue


def client_process(workers_num, file, workers, s_sock):
    print('CLient started...')
    for url in file:
        try:
            while threading.active_count() >= workers_num + 1:
                pass
            for i in workers[::-1]:
                if i is None:
                    i = threading.Thread(target=processing_url,
                                         args=(url, s_sock))
                    i.start()
                    break
                if not i.is_alive():
                    i.join()
                    i = threading.Thread(target=processing_url,
                                         args=(url, s_sock))
                    i.start()
                    break
        except socket.error:
            break
    for obj in workers:
        if obj is not None:
            obj.join()


def client_on(base=None):
    workers_num = 10
    if base is None:
        base = sys.argv
        if base[1].isdigit():
            workers_num = int(base[1])
        else:
            raise Exception
    with open(base[2], 'r', encoding='utf-8') as file:
        file = [x.strip() for x in file.readlines()]
        workers = [None]*workers_num
        host = socket.gethostname()
        port = 8888
        s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_sock.connect((host, port))
        client_process(workers_num, file, workers, s_sock)


if __name__ == '__main__':
    client_on()
