import os
import imquality.brisque as brisque
import PIL.Image
import pickle

dir = (os.listdir("datasets/test/"))

imgQuals = []
store = {}

for i in dir:
    label = i[:-4]
    label = label.split('_')
    photo = PIL.Image.open("datasets/test/" + i)
    
    score = (brisque.score(photo)) # FLOAT!!

    print(photo, score)
    store[i] = [score, label[1], label[2]] # iqa, sex, race

pickle.dump(store, open('iqa.pkl', 'wb'))