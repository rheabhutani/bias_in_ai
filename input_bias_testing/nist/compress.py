import os
import math
from PIL import Image

PATH = 'input_bias_testing/nist/dataset/'

images = os.listdir(PATH + 'complete/')


for img in images:
    print(img)
    i = Image.open(PATH + 'complete/' + img)
    if (i.mode == 'RGBA'): # remove corrupted images
        os.remove(PATH + 'complete/' + img)
    else:
        x, y = i.size
        x, y = math.floor(x / 5), math.floor(y / 5)
        photo = i.resize((x, y), Image.ANTIALIAS)
        print(i.size, photo.size)
        photo.save(PATH + "compressed/" + img, quality = 95)