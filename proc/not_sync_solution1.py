import random
from threading import Thread
import time

class Buffer:
    def __init__(self, num_values):
        self.size = 1 if num_values <= 99 else int(num_values * 0.01)  # 1% da quantidade
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

def producer(buffer):
    global is_finish
    for i in range(num_values):
        value = random.randint(0, 100)
        time.sleep(random.random())
        buffer.add(value)
        print(buffer.list)
        print(f'Valor enviado pelo produtor: {value}')

    time.sleep(2)
    is_finish = True

def consumer(buffer):
    global is_finish
    receives_count = 1
    while not is_finish:
        time.sleep(random.random())
        c = buffer.consume()
        if c != None:
            print(f'Valor recebido pelo consumidor: {c}')
        if is_finish:
            break

num_values = 1000
is_finish = False
buffer = Buffer(num_values)

tp = Thread(target=producer, args=[buffer])
tc = Thread(target=consumer, args=[buffer])
tp.start()
tc.start()

#tp.join()
tc.join()

print(f'valores perdidos: {buffer.losts}')
print(f'valores enviado: {buffer.sends}')
print(f'valores recebidos: {buffer.receives}')
