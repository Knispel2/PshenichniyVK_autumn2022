from logging import exception
from urllib.request import urlopen
import threading
import sys
import socket
import urllib.request
from collections import Counter
import json


def processing_url(url, s):
    s.send(bytes(url, encoding="utf-8"))
    while True:
        try:
            data = s.recv(1024)
            if data is None:
                break
            print(data.decode('utf-8'))
            break
        except Exception as e:
            print(e)
            continue


def client_process(workers_num, file, workers, s):
    print('CLient started...')
    for url in file:
        try:
            while threading.active_count() >= workers_num + 1:
                pass
            for i in workers[::-1]:
                if i is None:
                    i = threading.Thread(target=processing_url, args=(url, s))
                    i.start()
                    break
                if not i.is_alive():
                    i.join()
                    i = threading.Thread(target=processing_url, args=(url, s))
                    i.start()
                    break
        except socket.error:
            raise exception("Error Occured in server")
    for obj in workers:
        if not obj is None:
            obj.join()

def client_on(base = []):
    workers_num = 10
    if base == []:
        base = sys.argv
        if base[1].isdigit():
            workers_num = int(base[1])
        else:
            raise Exception
    file = open(base[2], 'r')
    file = [x.strip() for x in file.readlines()]
    workers = [None]*workers_num
    host = socket.gethostname()
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    client_process(workers_num, file, workers, s)

if __name__ == '__main__':
    client_on()
