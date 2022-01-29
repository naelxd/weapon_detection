import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test_imgs/test3.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

weapons = cv2.CascadeClassifier('cascade.xml')

results = weapons.detectMultiScale(gray_img, 1.3, 20, minSize=(100, 100))

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)


cv2.imshow('Result', img)
cv2.waitKey(0)
