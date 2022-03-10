import os
import pickle

pkl = pickle.load(open('input_bias_testing/nist/iqa.pkl', 'rb'))

def make_list(list):
    distribution = []
    for i in range(len(list)):
        distribution.append(0.0)
    return distribution

GLOBAL_SEX = [.504, .496] # male, female
distribution_sex = make_list(GLOBAL_SEX)


for i in pkl:
    sex = pkl[i][0]
    if (sex == 'M'):
        distribution_sex[0] += 1
    else:
        distribution_sex[1] += 1

print('Number of males: ', distribution_sex[0], ', Number of females: ', distribution_sex[1])