import imquality.brisque as brisque
from PIL import Image, ImageFilter

photo = Image.open("datasets/test/85_0_0_20170111205957066.jpg")
score = (brisque.score(photo)) # FLOAT!!
print(photo, score)

blur = photo.filter(ImageFilter.BLUR)
print(blur, (brisque.score(blur)))

photo.show()
blur.show()