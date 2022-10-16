from logging import exception
from urllib.request import urlopen
import threading
import sys
import socket
import urllib.request
from collections import Counter
import json


def processing_url(data, addr, top, conn, sem):
    while True:
        try:
            if data is None:
                break
            sem.acquire()
            with urllib.request.urlopen('https://' + data) as resp:
                sem.release()
                html = str(resp.read().decode('utf-8')).split(' ')
                words = Counter(html)
                words = dict(words.most_common(top))
                words = json.dumps(words)
                conn.sendto(bytes('https://' + data + words, encoding="utf-8"), addr)
            break
        except Exception as e:
            print(f'Error: {data}')


def server_process(conn, workers_num, workers, s, addr, top_num):
    sem = threading.Semaphore(value=5)
    url_counter = 0
    while True:
        try:
            buf_data = conn.recv(1024)
            if not buf_data:
                s.listen(1)
                conn, addr = s.accept()
                continue
            buf_data = buf_data.decode("utf-8").split('https://')
            for data in buf_data:                
                if data == '':
                    continue
                while threading.active_count() >= workers_num + 1:
                    pass
                for i in workers[::-1]:
                    if i is None:
                        i = threading.Thread(target=processing_url, args=(data, addr, top_num, conn, sem))
                        i.start()
                        url_counter += 1
                        print(f"Processed {url_counter} url's")
                        break
                    if not i.is_alive():
                        i.join()
                        i = threading.Thread(target=processing_url, args=(data, addr, top_num, conn, sem))
                        i.start()
                        url_counter += 1
                        print(f"Processed {url_counter} url's")
                        break
        except socket.error:
            raise exception("Error Occured in server")
    conn.close()

def server_on(input=[None]*5):
    workers_num = 10
    top_num = 7
    base = sys.argv if input != [None]*5 else input
    if base[1] == '-w':
        workers_num = int(base[2])
    if base[3] == '-k':
        top_num = int(base[4])
    workers = [None]*workers_num
    host = ''
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('Server started...')
    s.listen(1)
    conn, addr = s.accept()
    server_process(conn, workers_num, workers, s, addr, top_num)

if __name__ == '__main__':
    server_on()
