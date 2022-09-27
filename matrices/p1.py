import time 
from Matrix import *
from threading import Thread, Lock
import numpy as np


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


def multiply_thread_safe(A: Matrix, B: Matrix, index: int) -> Matrix:
    global share_memory, mutex
    if A.m != B.n:
        return

    C = Matrix(A.n, B.m)
    m = A.m
    print(f'size: {m}')
    for i in range(A.n):
        for j in range(B.m):
            for k in range(m):
                C.matrix[i][j] += A.matrix[i][k] * B.matrix[k][j]

    print(f'Acabei: {index}')
    with mutex:
        share_memory[index].append(C)

def mount_matrix():
    global share_memory

mutex = Lock()
split_times = 2

path = 'res/4_int_better.txt'
lines = get_lines_from(path)


A = get_matrix(lines)
B = get_matrix(lines)

share_memory = [[] for i in range(split_times * split_times)]

# before = time.time()
result = multiply(A, B)
# after = time.time()
print(result)

a_in_lines = create_from_lists(A.split_by_lines(split_times))
b_in_columns = create_from_lists(B.split_by_columns(split_times))

# print(f'a em linhas {a_in_lines}')
#
# results = []
# print(len(a_in_lines))
# print('----- Lines && Columns ----------')
# # print(a_in_lines[0])
# # print(b_in_columns[0])
# t = multiply(A, B)
# print(t)

# print(multiply(a_in_lines[0], b_in_columns[0]))

pool = []
thread_idx = 0
for a_line in a_in_lines:
    for b_line in b_in_columns:
        t = Thread(target=multiply_thread_safe, args=[a_line, b_line, thread_idx])
        pool.append(t)
        thread_idx += 1
print(f'Thread index: {thread_idx}')

for t in pool:
    t.start()

for t in pool:
    t.join()


print(share_memory[0][0])
# print(f'Tempo para multiplicar: ({after - before})')
# A = parser_lines(lines)
# print(lines)
