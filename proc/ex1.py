from threading import Thread
import sys
import time
import multiprocessing

def pingPong(nome):
    count = 0
    while count <= 10:
        # sys.stdout.write(nome + " Vez: " + str(count) + "\n")
        # sys.stdout.flush()
        print(f'Thread name: {nome} Vez: {count}')
        count += 1
        # time.sleep(time_to_sleep)

cores = multiprocessing.cpu_count()
print('cores: {cores}')

threadBag = []

for i in range(0, cores):
    print(i)
    threadBag.append(Thread(target=pingPong, args=[i]))

for thread in threadBag:
    thread.start()

# t1 = Thread(target=pingPong, args=["PING", 1.3])
# t2 = Thread(target=pingPong, args=["PONG", 1.7])
#
# t1.start()
# t2.start()
