from socket import socket, AF_INET, SOCK_STREAM
from variables import server_ip, server_port
from threading import Thread


def start():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect((server_ip, server_port))
        while True:
            matrix = cs.recv(1024)
            print(matrix)


Thread(target=start()).start()
