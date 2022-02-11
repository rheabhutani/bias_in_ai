import os
import imquality.brisque as brisque
import PIL.Image

dir = (os.listdir("Desktop/part3"))

for pic in dir:
    photo = Image.PIL.open(pic)