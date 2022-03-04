import os

from importlib_metadata import distribution

# directory for NIST mugshot database (using folder of photos with 1 front view and 0 profile views for each person)
dir = (os.listdir("/home/team/BiasAI/sd18/single/f1_p0"))

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

# CHECK IF ALL VALUES ARE PRESENT FOR NIST
for i in dir:
    #label = i[:-4]
    #label = label.split('_')

    if (i[-3:] == 'png'):
        #open associated txt file to see demographic info
        txt = i[:-3] + 'txt'
        f = open(txt, "r")

        #M or F
        sex = (f.read(9))[-1:]
        if (sex == 'M'):
            distribution_sex[0] += 1
        elif (sex == 'F'):
            distribution_sex[1] += 1

    #sex = int(label[1])
    #distribution_sex[sex] += 1

    #race = int(label[2])
    #distribution_race[race] += 1

#print('white: ', distribution_race[0], ', black: ', distribution_race[1], ', asian: ', distribution_race[2], ', indian: ', distribution_race[3], 'others: ', distribution_race[4])
print('Number of males: ', distribution_sex[0], ', Number of females: ', distribution_sex[1])