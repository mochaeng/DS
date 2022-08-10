from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Semaphore, Lock
import time
import random

server_port = 20001
empty = Semaphore(0)
mutex = Lock()

def serve():
    global server_connections
    while True:
        empty.acquire()
        # mutex.acquire()
        if len(server_connections) > 0:
            connection = server_connections.pop()
            # mutex.release()
            sentence = connection.recv(1024).decode()
            capitalized_sentece = sentence.upper()
            connection.sendall(capitalized_sentece.encode())
            print(capitalized_sentece)
            connection.close()

def serve_unique(connection):
    with connection as conn:
        print('hallo')
        while True:
            print(conn)
            sentence = conn.recv(1024).decode()
            if sentence == 'fim':
                print('time to exit')
                conn.sendall(sentence.encode())
                break
            print(f'From server {sentence}')
            capitalized_sentece = sentence.upper()
            conn.sendall(capitalized_sentece.encode())
            print(capitalized_sentece)

def welcoming():
    server_socket = socket(AF_INET, SOCK_STREAM)
    with server_socket as ss:
        ss.bind(('', server_port))
        ss.listen(1)
        print('Server is ready to receive')
        while True:
            connection_socket, addr = ss.accept()
            # with connection_socket as conn:
                # server_connections.insert(0, connection_socket)
                # serve_client_thread = Thread(target=serve)
                # server_threads.append(serve_client_thread)
                # serve_client_thread.start()
                # empty.release()
                # print(connection_socket)
            Thread(target=serve_unique, args=[connection_socket]).start()
                # thread_for_client.start()
                # server_client_thread = Thread();
                # sentence = connection_socket.recv(1024).decode()
                # capitalized_sentece = sentence.upper()
                # connection_socket.send(capitalized_sentece.encode())
                # connection_socket.close()

welcome_thread = Thread(target=welcoming)
# serve_thread = Thread(target=serve)
welcome_thread.start() 
# serve_thread.start()
# while True:
#     connection_socket, addr = server_socket.accept()
#     sentence = connection_socket.recv(1024).decode()
#     capitalized_sentece = sentence.upper()
#     connection_socket.send(capitalized_sentece.encode())
#     connection_socket.close()

