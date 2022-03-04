import os
import imquality.brisque as brisque
import PIL.Image
import pickle

#dir = (os.listdir("datasets/test/"))
dir = (os.listdir("/home/team/BiasAI/sd18/single/f1_p0"))

imgQuals = []
store = {}

#for i in dir:
    #label = i[:-4]
    #label = label.split('_')
    #photo = PIL.Image.open("datasets/test/" + i)

    #score = (brisque.score(photo)) # FLOAT!!
        
    #print(photo, score)   
    #store[i] = [score, label[1], label[2]] # iqa, sex, race

#pickle.dump(store, open('iqa.pkl', 'wb'))

for i in dir:
    if i[-3:] == 'png':
        photo = PIL.Image.open("/home/team/BiasAI/sd18/f1_p0/" + i)
        score = (brisque.score(photo))
        print(photo, score)

        txt = i[:-3] + 'txt'
        f = open(txt, "r")
        sex = (f.read(9))[-1:]

        store[i] = [score, sex]

pickl.dump(store, open('iqa.pkl', 'wb'))