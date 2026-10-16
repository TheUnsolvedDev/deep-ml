def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	eig = np.linalg.eigvals(matrix)
	return np.array(eig, dtype = int)