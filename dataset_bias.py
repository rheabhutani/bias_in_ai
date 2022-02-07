import os

dir = (os.listdir("datasets/part1"))

GLOBAL = [50.4, 49.6]

distribution = [0, 0]

for i in dir:
    label = i[:-4]
    label = label.split('_')
    distribution[1] += int(label[1])

distribution[0] = len(dir) - distribution[1]

print(distribution[0] * 100 / len(dir), distribution[1] * 100 / len(dir))
print(len(dir))
