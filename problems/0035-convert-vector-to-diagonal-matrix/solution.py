import numpy as np

def make_diagonal(x):
	# Your code here
	new_x = np.eye(len(x))
	for i in range((len(x))):
		new_x[i][i] = x[i]
	return new_x