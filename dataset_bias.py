import os
import imquality.brisque as brisque
import PIL.Image

dir = (os.listdir("datasets/test"))

GLOBAL = [.504, .496]
BIAS_LIMIT = 5

distribution = [0.0, 0.0]
imgQuals = [0.0, 0.0]

for i in dir:
    label = i[:-4]
    label = label.split('_')
    distribution[1] += int(label[1])

    photo = PIL.Image.open("datasets/test/" + i)
    
    score = (brisque.score(photo)) # FLOAT!!
    print(photo, score)
    imgQuals[int(label[1])] += score

distribution[0] = len(dir) - distribution[1]
#imgQuals = imgQuals/distribution
imgQuals = [i / j for i, j in zip(imgQuals, distribution)]

print("representation: ", distribution[0] * 100 / len(dir), distribution[1] * 100 / len(dir))
print("image quality indices: ", imgQuals)
print("total sampled population: ", len(dir))



