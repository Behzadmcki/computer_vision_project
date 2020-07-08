""" Write a program that reads the images from the dataset and randomly displays four
examples of each Persian digit.
"""
import numpy as np
import cv2
import glob
import random

list=[]
fnames = glob.glob('digit_dataset/train/1/I_1_*.png')
fnames.sort()
for fname in fnames:
     I=cv2.imread(fname)
     list.append(I)
print(len(list))
#print(list)
while 1:
  for x in range(4):
    b=random.randrange(1,120,1)
    print(b)	
    cv2.imshow('J',list[b])
    cv2.waitKey()
  print("END , if u want to resume press any key except	 'q' ")
  key =  cv2.waitKey()
  if key & 0xFF == ord('q'):
    exit()



        

    
