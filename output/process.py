import numpy as np 
import cv2 as cv
import os 

from eigen import * 

N = # Enter N
SHAPE = (# Enter shape

def pre_process(img, shape):
	return np.array(cv.resize(img, shape, cv.INTER_AREA)).flatten()

def read_bw_flat(path):
	return pre_process(cv.imread(path, 0), SHAPE)

def read_jafe(prefix, files, N):
	X = []
	S = []
	N = min(N, len(files))

	for i in range(N):
		path = prefix + files[i] 
		X.append(read_bw_flat(path))
		S.append(1.0)
	
	return np.array(X), np.array(S)

def read_chuck(prefix, files, N):
	X = []
	S = []

	N = min(N, len(files))

	decode_s = {'f': 1.0, 'm' : 0.0}

	for i in range(N):
		path = prefix + files[i]
		X.append(read_bw_flat(path))
		S.append(decode_s[files[i][0]])

	return np.array(X), np.array(S)

def read_utk(prefix, files, N):
	X = []
	Ss = []
	Sr = []

	decode_s = {'1' : 1.0, '0' : 0.0, '2' : 2.0, '3' : 3.0, '4' : 4.0}

	N = min(N, len(files))

	for i in range(N):
		path = prefix + files[i]
		X.append(read_bw_flat(path))

		name = files[i].split('_')

		Ss.append(decode_s[name[1]])
		Sr.append(decode_s[name[2]])

	return np.array(X), np.array(Ss), np.array(Sr)

path_jafe = 'Datasets/JAFFE/' 
path_chuck = 'Datasets/CUHK/'
path_utk = 'Datasets/utk/'

jaffe = os.listdir(path_jafe)
chuck = os.listdir(path_chuck)
utk = os.listdir(path_utk)

# print(len(jaffe), jaffe[0:10])
# print(len(chuck), chuck[0:10])
# print(len(utk), utk[0:10])

# print()

# print(cv.imread(path_jafe + jaffe[0], 0).shape)
# print(cv.imread(path_chuck + chuck[0], 0).shape)
# print(cv.imread(path_utk + utk[0], 0).shape)


X_j, S_j = read_jafe(path_jafe, jaffe, N) 

X_c, S_c = read_chuck(path_chuck, chuck, N)

X_u, S_u_s, S_u_r = read_utk(path_utk, utk, N)



# print(X_j.shape, S_j.shape)
# print(X_c.shape, S_c.shape)
# print(X_u.shape, S_u_s.shape, S_u_r.shape)


print(dataset_metric(X_j, S_j, X_c, S_c, compute_sorted_coef))
print(dataset_metric(X_j, S_j, X_u, S_u_s, compute_sorted_coef))
print(dataset_metric(X_c, S_c, X_u, S_u_s, compute_sorted_coef))

