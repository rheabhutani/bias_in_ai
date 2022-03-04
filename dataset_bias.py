import pickle
from distribution import *

iqa = pickle.load(open('./iqa.pkl', 'rb'))
iqa_sex = make_list(GLOBAL_SEX)
iqa_race = make_list(GLOBAL_RACE)

#for i in iqa:
    #qual = int(iqa[i][0])
    #sex = int(iqa[i][1])
    #race = int(iqa[i][2])

    #iqa_sex[sex] += qual
    #iqa_race[race] += qual

#iqa_sex = [i / j for i, j in zip(iqa_sex, distribution_sex)]
#iqa_race = [i / j for i, j in zip(iqa_race, distribution_race)]

for i in iqa:
    qual = int(iqa[i][0])
    sex = iqa[i][1]

    if sex == 'M':
        iqa_sex[0] += qual
    elif sex == 'F':
        iqa_sex[1] += qual

iqa_sex = [i / j for i, j in zip(iqa_sex, distribution_sex)]
