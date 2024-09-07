from Matrix import Matrix
import numpy as np
import time
from multiprocessing import Pool


def populate_numpy_array(A: Matrix, M: np.array):  # type: ignore
    for i in range(A.n):
        for j in range(A.m):
            M[i][j] = A.matrix[i][j]


def multiply(A: np.ndarray, B: np.ndarray):
    a_m = A.shape[1]
    b_n = B.shape[0]

    if a_m != b_n:
        raise ValueError("error: impossible to calculate")

    m3 = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                m3[i][j] += A[i][k] * B[k][j]

    return m3


def multiply_thread_safe(t: tuple) -> np.ndarray:
    a_m = t[0].shape[1]
    b_n = t[1].shape[0]

    if a_m != b_n:
        raise ValueError("Impossível multiplicar")

    m3 = np.zeros((t[0].shape[0], t[1].shape[1]))
    for i in range(t[0].shape[0]):
        for j in range(t[1].shape[1]):
            for k in range(t[0].shape[1]):
                m3[i][j] += t[0][i][k] * t[1][k][j]

    return m3


def multiply_with_processes(
    matrix_1: np.ndarray, matrix_2: np.ndarray, split_times: int
) -> tuple[np.ndarray, float]:
    pieces = []

    matrix_1_lines = np.array_split(matrix_1, split_times, axis=0)
    for idx, matrix_1_line in enumerate(matrix_1_lines):
        pieces.append((matrix_1_line, matrix_2, idx))

    with Pool(split_times) as p:
        before = time.time()
        results = p.map(multiply_thread_safe, pieces)

        aggregate_matrix = np.zeros((matrix_1.shape[0], matrix_1.shape[1]))
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

    return aggregate_matrix, total_time
