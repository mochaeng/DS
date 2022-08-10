import random
from threading import Thread, Semaphore
import time

num_values = 10
memoria_compartilhada = None  
con_sem = Semaphore(0)  # semáforo consumidor
pro_sem = Semaphore(1)  # semáforo produtor

def producer():
    global memoria_compartilhada
    for i in range(num_values):
        pro_sem.acquire()

        value = random.random()
        time.sleep(random.random())
        memoria_compartilhada = value
        print(f'{i+1}° valor')
        print(f'Valor enviado pelo produtor: {value}')

        con_sem.release()

    pro_sem.acquire()
    time.sleep(2)
    memoria_compartilhada = "fim"
    con_sem.release()

def consumer():
    global memoria_compartilhada
    while True:
        con_sem.acquire()

        time.sleep(random.random())
        value = memoria_compartilhada
        if (value == "fim"):
            break
        print(f'Valor recebido pelo consumidor: {value}')
        
        pro_sem.release()

tp = Thread(target=producer, args=[])
tc = Thread(target=consumer, args=[])
tp.start()
tc.start()

tc.join()


