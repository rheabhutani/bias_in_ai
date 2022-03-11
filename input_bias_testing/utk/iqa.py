import os
import imquality.brisque as brisque
import PIL.Image
import pickle

PATH = "input_bias_testing/utk/dataset/compressed/"

dir = (os.listdir(PATH))
#dir = (os.listdir("/home/team/BiasAI/sd18/single/f1_p0"))

imgQuals = []
store = {}
counter = 0

for i in dir:
    print(i, end=': ')
    label = i[:-4]
    label = label.split('_')
    photo = PIL.Image.open(PATH + i)

    try:
        score = (brisque.score(photo)) # FLOAT!!
    except:
        os.remove(PATH + i)
        print("removed ", i, ": too small")
    else:
        counter += 1  
        print(score)   
        store[i] = [score, label[1], label[2]] # iqa, sex, race
        print(counter, "/", len(dir))

pickle.dump(store, open('input_bias_testing/utk/iqa.pkl', 'wb'))