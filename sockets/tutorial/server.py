from socket import socket, AF_INET, SOCK_STREAM

host = 'localhost'
port = 20000

server_socket = socket(AF_INET, SOCK_STREAM)
with server_socket as ss:
    ss.bind((host, port))   
    ss.listen()
    connection, addr = ss.accept()
    with connection as con:
        print(f'Connect by {addr}')
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)

