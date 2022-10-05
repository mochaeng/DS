import time
import numpy as np
from parser import *
from utils import populate_numpy_array
from writing import write
from multiprocessing import cpu_count, Pool


def multiply_thread_safe(t: tuple) -> np.ndarray:
    a_m = t[0].shape[1]
    b_n = t[1].shape[0]

    if a_m != b_n:
        raise 'Impossível multiplicar'

    # m3 = A.dot(B)

    m3 = np.zeros((t[0].shape[0], t[1].shape[1]))
    for i in range(t[0].shape[0]):
        # print(f'Hi - {t[2]}\n')
        for j in range(t[1].shape[1]):
            for k in range(t[0].shape[1]):
                m3[i][j] += t[0][i][k] * t[1][k][j]

    return m3


num_cores = cpu_count()
split_times = int(num_cores / 2)

path = 'res/2048.txt'
lines = get_lines_from(path)

A = get_matrix(lines)
m1 = np.zeros((A.n, A.n))
m2 = np.zeros((A.n, A.n))

a_size = m1.shape
b_size = m2.shape

populate_numpy_array(A, m1)
populate_numpy_array(A, m2)

m1_lines = np.array_split(m1, split_times, axis=0)

pieces = []
for idx, a_line in enumerate(m1_lines):
    pieces.append((a_line, m2, idx))

with Pool(split_times) as p:
    before = time.time()
    results = p.map(multiply_thread_safe, pieces)

    aggregate_matrix = np.zeros((m1.shape[0], m1.shape[1]))
    i_global = 0
    j_global = 0
    for idx, array in enumerate(results):
        for i_local in range(array.shape[0]):
            for j_local in range(array.shape[1]):
                aggregate_matrix[i_global][j_global] = array[i_local][j_local]
                j_global += 1

            j_global = 0
            i_global += 1

    after = time.time()
    total_time = after - before
    print(aggregate_matrix)
    print(f'Tempo para calcular: {total_time}')

write('sol/p4/process/res_2048.txt\n', 'Solução p4 feita usando Pool de processos\n', f'Num cores: {num_cores}\n',
      f'Num cliente: {0}\n',
      f'Num linhas: {aggregate_matrix.shape[0]}\n', f'Num colunas: {aggregate_matrix.shape[1]}\n',
      f'Tempo para multiplicar e juntar: {total_time} segundos\n', aggregate_matrix)
