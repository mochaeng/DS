from socket import socket, AF_INET, SOCK_STREAM
from variables import server_port
from threading import Thread, Lock
import numpy as np
from parser import *

path = 'res/4_int_better.txt'
connected_clients_target = 2
client_connections = []
clients_connected = 0


def populate_numpy_array(A: Matrix, M: np.array):
    for i in range(A.n):
        for j in range(A.m):
            M[i][j] = A.matrix[i][j]


def parser_and_create_matrices():
    lines = get_lines_from(path)

    A = get_matrix(lines)
    m1 = np.zeros((A.n, A.n))
    m2 = np.zeros((A.n, A.n))

    populate_numpy_array(A, m1)
    populate_numpy_array(A, m2)

    m1_in_lines = np.array_split(m1, connected_clients_target, axis=0)

    return m1_in_lines, m2


def send_matrices_through_network(m1_in_lines, B):
    for idx, line in enumerate(m1_in_lines):
        with client_connections[idx][0] as conn:
            conn.sendall((line, B))


def send_files_through_network():
    # with open('res/4_int_better.txt') as file:
    #     for client_conn, _ in client_connections:
    #         with client_conn:
    #             # client_conn.sendfile(file)
    #             client_conn.sendall()
    ...


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

            connection_socket.sendall(str(clients_connected).encode())

            print(f'{addr} conectou-se ao servidor')
            print(f'{len(client_connections)} clientes conectados ao servidor\n')

            if clients_connected == connected_clients_target:
                break

        a, b = parser_and_create_matrices()
        send_matrices_through_network(a, b)


Thread(target=start()).start()
