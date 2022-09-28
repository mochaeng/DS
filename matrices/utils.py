from Matrix import Matrix
import numpy as np


def populate_numpy_array(A: Matrix, M: np.array):
    for i in range(A.n):
        for j in range(A.m):
            M[i][j] = A.matrix[i][j]
