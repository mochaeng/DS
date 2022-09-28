from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Semaphore, Lock
import time
import random

server_port = 20001
empty = Semaphore(0)
mutex = Lock()


def welcoming():
    server_socket = socket(AF_INET, SOCK_STREAM)
    with server_socket as ss:
        ss.bind(('', server_port))
        ss.listen(1)
        print('Server is ready to receive')
        while True:
            connection_socket, addr = ss.accept()
