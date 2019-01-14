import cv2
from keras.applications.densenet import DenseNet121
from keras.models import Sequential
import numpy as np
import datetime

print(datetime.datetime.now())
img = cv2.imread('style.jpg', 1)
print(img)
print(datetime.datetime.now())
img = cv2.resize(img, (224, 224))
print(datetime.datetime.now())

model = Sequential()
print(datetime.datetime.now())

model.add(DenseNet121(include_top=False, weights='imagenet', pooling='avg'))
print(datetime.datetime.now())
image_vector = np.squeeze(model.predict(np.expand_dims(img, axis=0)))
print(datetime.datetime.now())

image_vector.shape
print(datetime.datetime.now())
print(image_vector)
