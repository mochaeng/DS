import time
from threading import Lock
from multiprocessing import cpu_count
from parser import get_lines_from, get_matrix
import numpy as np
from utils import populate_numpy_array, multiply
from writing import write


if __name__ == "__main__":
    num_cpu_cores = cpu_count()

    mutex = Lock()
    path = "res/128.txt"

    lines = get_lines_from(path)
    A = get_matrix(lines)
    matrix_1 = np.zeros((A.n, A.n))
    matrix_2 = np.zeros((A.n, A.n))

    populate_numpy_array(A, matrix_1)
    populate_numpy_array(A, matrix_2)

    time_before = time.time()
    final_matrix = multiply(matrix_1, matrix_2)
    time_after = time.time()
    total_time = time_after - time_before
    print(f"Tempo para multiplicar: ({total_time} ms)")

    write(
        file_path="sol/p1/",
        file_name="classic_128.txt",
        variation="Solução p1 feita com abordagem tradicional O(n^3)",
        num_cores="Num cores: {num_cpu_cores}",
        num_clients="Num cliente: {0}",
        num_lines="Num linhas: {final_matrix.shape[0]}",
        num_columns="Num colunas: {final_matrix.shape[1]}",
        total_time="Tempo para multiplicar e juntar: {total_time} segundos",
        final_matrix=final_matrix,
    )
