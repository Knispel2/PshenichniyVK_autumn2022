from logging import exception
from urllib.request import urlopen
import threading
import sys
import socket
import urllib.request
from collections import Counter
import json


def processing_url(data, s, addr, top, conn):
    while True:
        try:
            if data is None:
                break
            with urllib.request.urlopen(data.decode("utf-8")) as resp:
                html = str(resp.read()).split(' ')
                words = Counter(html)
                words = dict(words.most_common(top))
                words = json.dumps(words)
                conn.sendto(bytes(words, encoding="utf-8"), addr)
            break
        except Exception as e:
            print(e.text)


def server_on(input=[None]*5):    
    url_counter = 0
    workers_num = 10
    top_num = 7
    base = sys.argv if input != [None]*5 else input
    if base[1] == '-w':
        workers_num = int(base[2])
    if base[3] == '-k':
        top_num = int(base[4])
    workers = [None]*workers_num
    host = ''        # Symbolic name meaning all available interfaces
    port = 8888     # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print('Server started...')
    s.listen(1)
    conn, addr = s.accept()
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            while threading.active_count() >= workers_num + 1:
                pass
            for i in workers[::-1]:
                if i is None:
                    i = threading.Thread(target=processing_url, args=(data, s, addr, top_num, conn))
                    i.start()
                    break
                if not i.is_alive():
                    i.join()
                    i = threading.Thread(target=processing_url, args=(data, s, addr, top_num, conn))
                    i.start()
                    break                
            url_counter += 1
            print(f"Processed {url_counter} url's")
        except socket.error:
            raise exception("Error Occured in server")
    conn.close()

if __name__ == '__main__':
    server_on()

server_on()
