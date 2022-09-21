import time 
from Matrix import *

def get_lines_from(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def get_matrix(lines):
    row_length, columnm_length = lines[0].split(' ')
    matrix = Matrix(int(row_length), int(columnm_length))
    for i in range(1, int(row_length) + 1):
        line = lines[i].strip().split(' ')
        for j in range(len(line)):
            matrix.matrix[i-1][j] = float(line[j])
    return matrix

def multiply(A: Matrix, B: Matrix) -> Matrix:
    if A.m != B.n:
        return
    C = Matrix(A.n, B.m)
    m = A.m
    print(f'size: {m}')
    for i in range(A.n):
        for j in range(B.m):
            for k in range(m):
                C.matrix[i][j] += A.matrix[i][k] * B.matrix[k][j]
    return C

path = '4_int_better.txt'
lines = get_lines_from(path)

A = get_matrix(lines)
B = get_matrix(lines)

# before = time.time()
# result = multiply(A, B)
# after = time.time()
split_times = 2

a_in_lines = create_from_lists(A.split_by_lines(2))
b_in_lines = create_from_lists(B.split_by_columns(2))

print(a_in_lines[0])
print(b_in_lines[0])
print(multiply(A, B))
print(multiply(a_in_lines[0], b_in_lines[0]))

# print(result)
# print(f'Tempo para multiplicar: ({after - before})')
# A = parser_lines(lines)
# print(lines)
