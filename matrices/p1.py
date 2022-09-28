import time
from threading import Lock
from multiprocessing import cpu_count
from parser import *
from Matrix import *
import numpy as np
from utils import populate_numpy_array
from writing import write


def multiply(A: np.ndarray, B: np.ndarray):
    a_m = A.shape[1]
    b_n = B.shape[0]

    if a_m != b_n:
        return

    m3 = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                m3[i][j] += A[i][k] * B[k][j]

    return m3


num_cpu_cores = cpu_count()

mutex = Lock()
path = 'res/4_int_better.txt'

lines = get_lines_from(path)
A = get_matrix(lines)
m1 = np.zeros((A.n, A.n))
m2 = np.zeros((A.n, A.n))

populate_numpy_array(A, m1)
populate_numpy_array(A, m2)

before = time.time()
final_matrix = multiply(m1, m2)
after = time.time()
total_time = after - before

print(final_matrix)
print(f'Tempo para multiplicar: ({total_time} ms)')


write('sol/p1/classic_4.txt\n', 'Solução p1 feita com abordagem tradicional O(3)\n', f'Num cores: {num_cpu_cores}\n',
      f'Num cliente: {0}\n',
      f'Num linhas: {final_matrix.shape[0]}\n', f'Num colunas: {final_matrix.shape[1]}\n',
      f'Tempo para multiplicar e juntar: {total_time} segundos\n', final_matrix)
