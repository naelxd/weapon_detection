import cv2
import numpy as np

img = cv2.imread('test.png')

cv2.imshow('Result', img)
cv2.waitkey(0)