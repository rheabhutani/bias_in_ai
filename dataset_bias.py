import os
from multinomial_pdf import *
import imquality.brisque as brisque
import PIL.Image

dir = (os.listdir("datasets/part1"))

GLOBAL = [.504, .496]

distribution = [0.0, 0.0]
imgQuals = [0.0, 0.0]

for i in dir:
    label = i[:-4]
    label = label.split('_')
    distribution[1] += int(label[1])

    photo = PIL.Image.open("datasets/part1/" + i)
    score = float(brisque.score(photo)) # might be a string, might be an int, not sure
    imgQuals[int(label[1])] += score

distribution[0] = len(dir) - distribution[1]
imgQuals = imgQuals/distribution

print("representation: ", distribution[0] * 100 / len(dir), distribution[1] * 100 / len(dir))
print("image quality indices: ", imgQuals)
print("total sampled population: ", len(dir))


bias = PDF(distribution, GLOBAL, len(dir))
if bias > 0.05:
    print('data is biased')
else:
    print('data is unbiased congratulations!')
