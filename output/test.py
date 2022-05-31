import numpy as np 
import matplotlib.pyplot as plt 
from eigen import *

def _test1():
	b1 = np.array([[1, 0], [0, 1]])
	b2 = np.array([[1, 1], [-1, 1]]) / np.sqrt(2)
	b3 = np.array([[np.sqrt(3)/2, 1/2], [-1/2, np.sqrt(3)/2]])

	res1 = np.array([[1/np.sqrt(2), 1/np.sqrt(2)], [-1/np.sqrt(2), 1/np.sqrt(2)]])
	assert np.linalg.norm((b1@b2)-res1, ord=np.inf) < 1e-9 

	res2 = np.array([[np.sqrt(3)/2, 0.5], [-0.5, np.sqrt(3)/2]])
	assert np.linalg.norm((b1@b3)-res2, ord=np.inf) < 1e-9 

	assert np.abs(compute_sorted_coef([1, 1], b1, [1, 1], b2) - np.pi/2) < 1e-9
	assert np.abs(compute_sorted_coef([1, 1], b1, [1, 1], b3) - np.pi/3) < 1e-9

def _test2():
	n = 10
	d = 2
	X1 = gen_data(n, d)
	X2 = gen_data(n*2, d)
	S1 = np.random.randint(2, size=n)
	S2 = np.random.randint(2, size=n)
	print(dataset_metric(X1, S1, X2, S2, compute_sorted_coef))

def _test3():
	b1 = np.array([[1, 0], [0, 1]])
	b2 = np.array([[1, 1], [-1, 1]]) / np.sqrt(2)
	b3 = np.array([[np.sqrt(3)/2, 1/2], [-1/2, np.sqrt(3)/2]])

	assert np.abs(metric(b1, b3, compute_sorted_coef) - np.pi/3.0) < 1e-9
	assert np.abs(metric(b1, b2, compute_sorted_coef) - np.pi/2.0) < 1e-9
	assert np.abs(metric(b3, b2, compute_sorted_coef) - np.pi/6.0) < 1e-9
	assert np.abs(metric(b3, b3, compute_sorted_coef)) < 1e-9

def _test4():
	b1 = np.array([[1, 0], [0, 1]])
	b2 = np.array([[1, 1], [-1, 1]]) / np.sqrt(2)
	b3 = np.array([[np.sqrt(3)/2, 1/2], [-1/2, np.sqrt(3)/2]])
	S = np.array([1, 1])

	res1 = dataset_metric(b1, S, b2, S, compute_sorted_coef) - np.array([[1, np.pi/2]])
	assert np.linalg.norm(res1, ord=np.inf) < 1e-9

def _test5():
	n = 10
	d = 2
	X1 = gen_data(n, d)
	X2 = gen_data(n*2, d)
	C11 = covariance_matrix_slow(X1)
	C12 = covariance_matrix(X1)
	C21 = covariance_matrix_slow(X2)
	C22 = covariance_matrix(X2)

	assert np.linalg.norm(C11-C12) < 1e-9
	assert np.linalg.norm(C21-C22) < 1e-9 

_test1()
_test2()
_test3()
_test4()
_test5()