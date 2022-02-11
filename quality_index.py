# https://pypi.org/project/image-quality/ for basic code to extract a brisque score from any image (lines 4-5, 10- )

import imquality.brisque as brisque
import PIL.Image

imgQuals = [0.0, 0.0]
numPeople = [0, 0]

for pic in dir:
    photo = PIL.Image.open(pic)
    score = brisque.score(photo) # might be a string, might be an int, not sure
    
    manOrWoman = int(label[1])

    oldNum = imgQuals[manOrWoman] * numPeople[manOrWoman] # # of men or women based on previous % stored in imgQuals
    numPeople[manOrWoman] += 1 # increment numPeople[0] by 1 if label[1] shows it's a man, otherwise increment women
    imgQuals[manOrWoman] = (oldNum + score) / numPeople[manOrWoman] # find new average quality with new score added in

if imgQuals[0] - imgQuals[1] > 0.05:
    print('data is biased based on quality')
else:
    print('data is not biased based on quality')