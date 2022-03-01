import os

from importlib_metadata import distribution

dir = (os.listdir("datasets/part1"))

def make_list(list):
    distribution = []
    for i in range(len(list)):
        distribution.append(0.0)
    return distribution

GLOBAL_SEX = [.504, .496] # male, female
distribution_sex = make_list(GLOBAL_SEX)

# 100-(60.1+12.2+5.6+0.7) = 21.4
GLOBAL_RACE = [0.601, 0.122, 0.056, 0.007, 0.214] # white, black, asian, indian (country), others
distribution_race = make_list(GLOBAL_RACE)

# CHECK IF ALL VALUES ARE PRESETN FOR NIST
for i in dir:
    label = i[:-4]
    label = label.split('_')

    sex = int(label[1])
    distribution_sex[sex] += 1

    race = int(label[2])
    distribution_race[race] += 1

print('white: ', distribution_race[0], ', black: ', distribution_race[1], ', asian: ', distribution_race[2], ', indian: ', distribution_race[3], 'others: ', distribution_race[4])
print('male: ', distribution_sex[0], ', female: ', distribution_sex[1])