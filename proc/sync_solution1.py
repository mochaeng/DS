import random
from threading import Thread
import time

num_values = 100

buffer = []  # buffer com tamanho 1
turn = 0 # (turn 0 == produtor) e (turn 1 == consumer)

def producer(buffer):
    global turn
    for i in range(num_values):
        while (turn != 0): 
            ...
        value = random.random()
        time.sleep(random.random())
        buffer.append(value)
        print(f'{i+1}° valor')
        print(f'Valor enviado pelo produtor: {value}')
        turn = 1

    while (turn != 0):
        ...
    buffer.append("fim")
    turn = 1

def consumer(buffer):
    global turn
    while True:
        while (turn != 1):
            ...
        time.sleep(random.random())
        value = buffer.pop()
        if (value == "fim"):
            break
        print(f'Valor recebido pelo consumidor: {value}')
        turn = 0

tp = Thread(target=producer, args=[buffer])
tc = Thread(target=consumer, args=[buffer])
tp.start()
tc.start()
