import numpy as np
import os


def write(
    file_path,
    file_name,
    variation,
    num_cores,
    num_clients,
    num_lines,
    num_columns,
    total_time,
    final_matrix: np.ndarray,
):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with open(file_path + file_name, "w+") as f:
        f.write(variation + "\n")
        f.write(num_cores + "\n")
        f.write(num_clients + "\n")
        f.write(num_lines + "\n")
        f.write(num_columns + "\n")
        f.write(total_time + "\n")
        f.write("\n")

        for i in range(final_matrix.shape[0]):
            for j in range(final_matrix.shape[1]):
                f.write(str(final_matrix[i][j]) + " ")
            f.write("\n")
