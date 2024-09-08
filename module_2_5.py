def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(3, 4, 7)
result_2 = get_matrix(6, 3, 87)
result_3 = get_matrix(9, 2, 57)
print(f'Первая матрица {result_1}')
print(f'Вторая матрица {result_2}')
print(f'Третья матрица {result_3}')