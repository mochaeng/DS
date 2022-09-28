import time

import numpy
import time
from Matrix import Matrix
from threading import Thread, Lock
import numpy as np
from matrices.Matrix import Matrix
from parser import *
from typing import List


def multiply_thread_safe(A: np.ndarray, B: numpy.ndarray, index: int):
    global share_memory, mutex
    a_m = A.shape[1]
    b_n = B.shape[0]

    if a_m != b_n:
        return

    m3 = A.dot(B)

    # m3 = np.zeros((A.shape[0], B.shape[1]))
    # for i in range(A.shape[0]):
    #     for j in range(B.shape[1]):
    #         for k in range(A.shape[1]):
    #             m3[i][j] += A[i][k] * B[k][j]

    print(f'Acabei: {index}')
    with mutex:
        share_memory[index].append(m3)


def populate_numpy_array(A: Matrix, M: np.array):
    for i in range(A.n):
        for j in range(A.m):
            M[i][j] = A.matrix[i][j]


split_times = 2
share_memory: List[List[np.ndarray]] = [[] for i in range(split_times)]
# share_memory: List[List[List[np.ndarray]]] = [[[]] for i in range(split_times * split_times)]


mutex = Lock()
path = 'res/128.txt'
lines = get_lines_from(path)

A = get_matrix(lines)
m1 = np.zeros((A.n, A.n))
m2 = np.zeros((A.n, A.n))

a_size = m1.shape
b_size = m2.shape

populate_numpy_array(A, m1)
populate_numpy_array(A, m2)

m1_lines = np.array_split(m1, split_times, axis=0)
# m2_columns = np.array_split(m2, split_times, axis=1)

pool = []
for idx, a_line in enumerate(m1_lines):
    t = Thread(target=multiply_thread_safe, args=[a_line, m2, idx])
    pool.append(t)

# thread_idx_i = 0
# thread_idx_j = 0
# for a_line in m1_lines:
#     thread_idx_j = 0
#     for b_line in m2_columns:
#         t = Thread(target=multiply_thread_safe, args=[a_line, b_line, thread_idx_i, thread_idx_j])
#         pool.append(t)
#         thread_idx_j += 1
#     thread_idx_i += 1
# print(f'Thread index: {thread_idx}')

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
print('\nMatriz final')
print(aggregate_matrix)
print(f'Tempo total para calcular e juntar: {after - before}')

