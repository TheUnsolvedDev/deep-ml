def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows = len(a)
    columns = len(a[0])
    
    transpose = []
    for col in range(columns):
        transpose_sub = []
        for row in range(rows):
            transpose_sub.append(a[row][col])
        transpose.append(transpose_sub)
    return transpose
