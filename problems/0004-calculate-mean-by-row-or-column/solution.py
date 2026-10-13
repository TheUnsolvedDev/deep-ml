def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])
    means = []

    if mode == 'row':
        for row in matrix:
            means.append(sum(row) / cols)
            
    elif mode == 'column':
        for col in range(cols):
            col_sum = sum(matrix[row][col] for row in range(rows))
            means.append(col_sum / rows)

    return means