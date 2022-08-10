from socket import socket, AF_INET, SOCK_STREAM

host = 'localhost'
port = 20000

client_socket = socket(AF_INET, SOCK_STREAM)
with client_socket as cs:
    cs.connect((host, port))
    cs.sendall(b'Hello World')
    data = cs.recv(1024)

print(f'Received: {data}')
