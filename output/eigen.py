import numpy as np 
import matplotlib.pyplot as plt 

def mean_normalize(X):
	return X-np.mean(np.transpose(X), axis=1)

def covariance_matrix_slow(X):
	X = np.array(X)
	n, d = X.shape

	cov = np.zeros((d, d))
	
	for component_x in range(d):
		for component_y in range(d):
			cov[component_x][component_y] = np.dot(X[:, component_x], X[:, component_y]) / n
	
	return cov 

def covariance_matrix(X):
	X = np.array(X)
	n, d = X.shape

	cov = np.dot(X.T, X) / n

	return cov 

def inverse_cosine_distance(vec1, vec2):
	return np.arccos(np.dot(vec1, vec2) / (np.linalg.norm(vec1, ord=2) * np.linalg.norm(vec2, ord=2)))

def compute_sorted_coef(lambda1, vector1, lambda2, vector2):
	_lambda1 = np.argsort(lambda1)
	_lambda2 = np.argsort(lambda2)

	dif = 0 

	d = min(len(lambda1), len(lambda2))

	for i in range(d):
		dif += inverse_cosine_distance(vector1[:, _lambda1[i]], vector2[:, _lambda2[i]])

	return dif 

def metric(A, B, _dif_func):

	cov_A = covariance_matrix(mean_normalize(A))
	cov_B = covariance_matrix(mean_normalize(B))
	_lam_a, _vec_a = eigen(cov_A)
	_lam_b, _vec_b = eigen(cov_B)

	# print(_lam_a)
	# print(_lam_b)

	return np.absolute(_dif_func(_lam_a, _vec_a, _lam_b, _vec_b))

# def covariance_matrix(X):
# 	return np.cov(X)

def eigen(A):
	return np.linalg.eig(A)

def gen_data(n, d):
	return np.random.normal(size=(n,d))

def partition_data(X, S):
	_parts = {}

	for i in range(len(S)):
		if S[i] not in _parts:
			_parts[S[i]] = []

		_parts[S[i]].append(X[i])

	return _parts

def dataset_metric(X_a, S_a, X_b, S_b, _dif_func):
	_partition_a = partition_data(X_a, S_a)
	_partition_b = partition_data(X_b, S_b)

	result = []

	for subgroup_a in _partition_a:
		if subgroup_a in _partition_b:
			result.append([subgroup_a, metric(_partition_a[subgroup_a], _partition_b[subgroup_a], _dif_func)])

	return np.array(result)

def plot(X):
	plt.scatter(X[:, 0], X[:,1])
	plt.show() 
