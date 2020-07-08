from itertools import groupby

import numpy as np
import cv2
from matplotlib import pyplot as plt
I = cv2.imread('/home/joker/Documents/cv-lab2/masoleh.jpg')
B= I[:,:,0]
G= I[:,:,1]
R= I[:,:,2]
cv2.imshow('win1',I)
green_img = np.zeros(I.shape,dtype=np.uint8)
red_img = np.zeros(I.shape)
blue_img = np.zeros(I.shape)

while 1:
    k = cv2.waitKey()
    if k == ord('o'):

        cv2.imshow('win1',I)
    elif k == ord('b'):
        blue_img[:, :, 0] = B
        cv2.imshow('win1',blue_img)
    elif k == ord('g'):
         green_img[:, :, 1]=G
         cv2.imshow('win1',green_img)
    elif k == ord('r'):
         red_img[:, :, 2] = R
         cv2.imshow('win1',red_img)
    elif k == ord('q'):
        cv2.destroyAllWindows()
        break
