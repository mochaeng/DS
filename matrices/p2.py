import numpy as np
from parser import get_lines_from, get_matrix
from utils import populate_numpy_array, multiply_with_processes
from writing import write
from multiprocessing import cpu_count


if __name__ == "__main__":
    num_cores = cpu_count()
    split_times = num_cores

    path = "res/128.txt"
    lines = get_lines_from(path)

    A = get_matrix(lines)
    matrix_1 = np.zeros((A.n, A.n))
    matrix_2 = np.zeros((A.n, A.n))
    populate_numpy_array(A, matrix_1)
    populate_numpy_array(A, matrix_2)

    aggregate_matrix, total_time = multiply_with_processes(
        matrix_1, matrix_2, split_times
    )

    print(f"Tempo para calcular: {total_time}")

    write(
        file_path="sol/p2/process",
        file_name="res_2048.txt",
        variation="Solução p4 feita usando Pool de processos",
        num_cores=f"Num cores: {num_cores}",
        num_clients=f"Num cliente: {0}",
        num_lines=f"Num linhas: {aggregate_matrix.shape[0]}",
        num_columns=f"Num colunas: {aggregate_matrix.shape[1]}",
        total_time=f"Tempo para multiplicar e juntar: {total_time} segundos",
        final_matrix=aggregate_matrix,
    )
