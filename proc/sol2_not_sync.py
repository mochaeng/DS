import random
from threading import Thread, Semaphore
import time
from math import ceil

class Buffer:
    def __init__(self, num_values):
        self.size = ceil(num_values * 0.01)  # 1% da quantidade
        self.list = []
        self.sends = []
        self.receives = []
        self.losts = []

    def add(self, value):
        self.sends.append(value)
        if len(self.list) < self.size:
            return self.list.insert(0, value)
        self.losts.append(value)

    def consume(self):
        if len(self.list):
            value = self.list.pop()
            self.receives.append(value)
            return value

    def __str__(self):
        return str(self.list)

def producer():
    global end_line, buffer
    for i in range(num_values):
        ociosas_sem.acquire()

        value = random.randint(0, 1000)  # valores aleatórios entre 0 e 1000
        time.sleep(random.random())
        buffer.add(value)

        ocupadas_sem.release()
        print(f'Valor enviado pelo produtor: {value}')
    
    ociosas_sem.acquire()
    time.sleep(2)
    end_line = "fim"
    ocupadas_sem.release()

def consumer():
    global end_line, buffer
    while end_line != "fim":
        ocupadas_sem.acquire()

        time.sleep(random.random())
        c = buffer.consume()

        ociosas_sem.release()

        if c != None:
            print(f'Valor recebido pelo consumidor: {c}')

num_values = 10
end_line = ""
buffer = Buffer(num_values)

ociosas_sem = Semaphore(buffer.size)  # Semáforo com quantidade de vagas livres buffer
ocupadas_sem = Semaphore(0)  # Semáforo com quantidade de vagas ocupadas no buffer

tp = Thread(target=producer)
tc = Thread(target=consumer)
tp.start()
tc.start()

#tp.join()
tc.join()

print('\n--------------------------------')
print(f'valores enviados: {buffer.sends}')
print(f'valores recebidos: {buffer.receives}')
print(f'valores perdidos: {buffer.losts}')
