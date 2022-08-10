from threading import Thread
import random
import sys

NUM_VALUES = 12
NUM_THREADS = 4

threaded_total = 0
values = [i * random.randint(0, 100) for i in range(NUM_VALUES)]
sequential_total = sum(values)

class Soma:
    sub_toal = 0

def run_thread(t_number, soma):
    range_start = int(t_number * NUM_VALUES / NUM_THREADS)
    range_end = int(((t_number + 1) * NUM_VALUES / NUM_THREADS) - 1)

    for i in range(range_start, range_end):
        soma.sub_toal += values[i]
        print(f'Subtotal for thread {t_number}: {soma.sub_toal} (from {range_start} to {range_end})')

    # return soma
    threaded_total += soma.sub_toal
        
print(f'Sequential total: {sequential_total}')

def invoke(thread):
    thread.start()

threads = [Thread(target=run_thread, args=[i, Soma()]) for i in range(NUM_THREADS)] 
for thread in threads:
    thread.start()

print(threads)

