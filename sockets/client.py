from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

server_port = 20001
server_ip = 'localhost'

def send():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect((server_ip, server_port))
        while True:
            sentence = input('Input lower case: ')
            cs.sendall(sentence.encode())
            modified_sentence = cs.recv(1024)
            if modified_sentence == "FIM":
                break
            print(f'From server: {modified_sentence.decode()}')

print('acabamos amigos')
client_thread = Thread(target=send)
client_thread.start()

# client_socket.close()
