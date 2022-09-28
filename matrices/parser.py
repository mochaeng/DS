from Matrix import Matrix


def get_lines_from(path):
    with open(path) as f:
        lines = f.readlines()
    return lines


def get_matrix(lines):
    row_length, column_length = lines[0].split(' ')
    matrix = Matrix(int(row_length), int(column_length))
    for i in range(1, int(row_length) + 1):
        line = lines[i].strip().split(' ')
        for j in range(len(line)):
            matrix.matrix[i-1][j] = float(line[j])
    return matrix
