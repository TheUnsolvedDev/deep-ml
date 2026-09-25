import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	current_shape = (len(a),len(a[0]))
	if current_shape[0]*current_shape[1] != new_shape[0]*new_shape[1]:
		return []

	reshape_matrix = []
	flatten = []
	for row in range(current_shape[0]):
		for col in range(current_shape[1]):
			flatten.append(a[row][col])

	temp = []
	for ind in range(len(flatten)):
		temp.append(flatten[ind])
		if (ind + 1) % new_shape[1] == 0:
			reshape_matrix.append(temp)
			temp = []
		

	return reshape_matrix