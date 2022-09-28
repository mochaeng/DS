import numpy as np


def write(file_name, variation, num_cores, num_clients, num_lines,
          num_columns, total_time, final_matrix: np.ndarray):

    with open(file_name, 'w+') as f:
        f.write(variation)
        f.write(num_cores)
        f.write(num_clients)
        f.write(num_lines)
        f.write(num_columns)
        f.write(total_time)
        f.write('\n')

        for i in range(final_matrix.shape[0]):
            for j in range(final_matrix.shape[1]):
                f.write(str(final_matrix[i][j]) + ' ')
            f.write('\n')
