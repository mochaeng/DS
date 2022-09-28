import numpy
import time
from Matrix import Matrix
from threading import Thread, Lock
import numpy as np
from parser import *
from typing import List
from utils import populate_numpy_array
from writing import write
from multiprocessing import cpu_count


def multiply_thread_safe(A: np.ndarray, B: numpy.ndarray, index: int):
    global share_memory, mutex
    a_m = A.shape[1]
    b_n = B.shape[0]

    if a_m != b_n:
        return

    # m3 = A.dot(B)

    m3 = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                m3[i][j] += A[i][k] * B[k][j]

    # print(f'Acabei: {index}')
    with mutex:
        share_memory[index].append(m3)


num_cores = cpu_count()
split_times = num_cores + 2
share_memory: List[List[np.ndarray]] = [[] for i in range(split_times)]

mutex = Lock()
path = 'res/512.txt'
lines = get_lines_from(path)

A = get_matrix(lines)
m1 = np.zeros((A.n, A.n))
m2 = np.zeros((A.n, A.n))

a_size = m1.shape
b_size = m2.shape

populate_numpy_array(A, m1)
populate_numpy_array(A, m2)

m1_lines = np.array_split(m1, split_times, axis=0)

pool = []
for idx, a_line in enumerate(m1_lines):
    t = Thread(target=multiply_thread_safe, args=[a_line, m2, idx])
    pool.append(t)

before = time.time()

for t in pool:
    t.start()

for t in pool:
    t.join()


aggregate_matrix = np.zeros((m1.shape[0], m1.shape[1]))
i_global = 0
j_global = 0
for idx, matrix in enumerate(share_memory):
    matrix_chunk = share_memory[idx][0]
    for i_local in range(matrix_chunk.shape[0]):
        for j_local in range(matrix_chunk.shape[1]):
            aggregate_matrix[i_global][j_global] = matrix_chunk[i_local][j_local]
            j_global += 1
        j_global = 0
        i_global += 1

after = time.time()
total_time = after - before

print(aggregate_matrix)

write('sol/p2/classic_512.txt\n', 'Solução p2 feita com abordagem tradicional O(3)\n', f'Num cores: {num_cores}\n',
      f'Num cliente: {0}\n',
      f'Num linhas: {aggregate_matrix.shape[0]}\n', f'Num colunas: {aggregate_matrix.shape[1]}\n',
      f'Tempo para multiplicar e juntar: {total_time} segundos\n', aggregate_matrix)
