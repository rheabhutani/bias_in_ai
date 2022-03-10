import pickle
from distribution import *

pkl = pickle.load(open('input_bias_testing/nist/iqa.pkl', 'rb'))
iqa_sex = make_list(GLOBAL_SEX)

for i in pkl:
    sex = 0
    if(pkl[i][0] == 'F'):
        sex = 1
    qual = 0
    n = 0
    for iqa in range(1, len(pkl[i])):
        print(pkl[i][iqa])
        qual += pkl[i][iqa]
        n += 1
    single_iqa = qual / n
    iqa_sex[sex] += single_iqa


    # iqa_sex[sex] += qual

iqa_sex = [i / j for i, j in zip(iqa_sex, distribution_sex)]
print(iqa_sex)

# for i in iqa:
#     qual = int(iqa[i][0])
#     sex = iqa[i][1]

#     if sex == 'M':
#         iqa_sex[0] += qual
#     elif sex == 'F':
#         iqa_sex[1] += qual

# iqa_sex = [i / j for i, j in zip(iqa_sex, distribution_sex)]
