# m2_columns = np.array_split(m2, split_times, axis=1)

# thread_idx_i = 0
# thread_idx_j = 0
# for a_line in m1_lines:
#     thread_idx_j = 0
#     for b_line in m2_columns:
#         t = Thread(target=multiply_thread_safe, args=[a_line, b_line, thread_idx_i, thread_idx_j])
#         pool.append(t)
#         thread_idx_j += 1
#     thread_idx_i += 1
# print(f'Thread index: {thread_idx}')
