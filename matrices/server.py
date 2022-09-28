from socket import socket, AF_INET, SOCK_STREAM
from variables import server_port
import time
from Matrix import Matrix
from threading import Thread, Lock
import numpy as np
from parser import *
from typing import List


path = 'res/4_int_better.txt'
connected_clients_target = 2
client_connections = []
clients_connected = 0


def populate_numpy_array(A: Matrix, M: np.array):
    for i in range(A.n):
        for j in range(A.m):
            M[i][j] = A.matrix[i][j]


def parser_and_create_matrix():
    lines = get_lines_from(path)

    A = get_matrix(lines)
    m1 = np.zeros((A.n, A.n))
    m2 = np.zeros((A.n, A.n))

    a_size = m1.shape
    b_size = m2.shape

    populate_numpy_array(A, m1)
    populate_numpy_array(A, m2)

    m1_in_lines = np.array_split(m1, connected_clients_target, axis=0)
    m2_in_columns = np.array_split(m2, connected_clients_target, axis=1)

    return m1_in_lines, m2_in_columns


def send_matrices_through_network(m1_lines: np.ndarray, m2_columns: np.ndarray):
    idx_client = 0
    for m1_line in m1_lines:
        to_send = [m1_line]
        for m2_column in m2_columns:
            to_send.append(m2_column)

        with client_connections[idx_client][0] as connection:
            connection.sendfile(to_send)

        idx_client += 1


def start():
    global clients_connected
    server_socket = socket(AF_INET, SOCK_STREAM)
    with server_socket as ss:
        ss.bind(('', server_port))
        ss.listen(1)
        print('Servidor já está rodando!!\n')
        while True:
            connection_socket, addr = ss.accept()
            client_connections.append((connection_socket, addr))
            clients_connected += 1

            print(f'{addr} conectou-se ao servidor')
            print(f'{len(client_connections)} clientes conectados ao servidor\n')

            if clients_connected == connected_clients_target:
                break

        m1, m2 = parser_and_create_matrix()
        send_matrices_through_network(m1, m2)


Thread(target=start()).start()
