from itertools import count
import os
import imquality.brisque as brisque
import PIL.Image
import pickle

PATH = "input_bias_testing/nist/dataset/"
print(PATH)

dir = (os.listdir(PATH + '/compressed'))

store = {}
counter = 0

def get_sex(text):
    f = open(PATH + "text/" + text)
    content = f.readlines()
    sex = content[0].split(' ')[1].strip()
    return sex

for i in dir:
    print(i, end=": ")
    label = i[:-4]
    text = label + '.txt'
    label = label.split('_')
    photo = PIL.Image.open(PATH + 'compressed/' + i)

    try:
        score = brisque.score(photo)
    except:
        os.remove(PATH + 'compressed/' + i)
        os.remove(PATH + 'text/' + text)
        print("removed ", i, ": too small")
    else:
        print(score)
        if label[0] not in store.keys():
            store[label[0]] = [get_sex(text), score]
        else:
            store[label[0]].append(score)
    counter += 1
    print(counter, '/', len(dir))
    print(store[label[0]])

pickle.dump(store, open('input_bias_testing/nist/iqa.pkl', 'wb'))
