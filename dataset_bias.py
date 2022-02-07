import os

from multinomial_pdf import *

dir = (os.listdir("datasets/part1"))

GLOBAL = [.504, .496]

distribution = [0.0, 0.0]

for i in dir:
    label = i[:-4]
    label = label.split('_')
    distribution[1] += int(label[1])

distribution[0] = len(dir) - distribution[1]

print(distribution[0] * 100 / len(dir), distribution[1] * 100 / len(dir))
print(len(dir))


bias = PDF(distribution, GLOBAL, len(dir))
if bias > 0.05:
    print('data is biased')
else:
    print('data is unbiased congratulations!')
