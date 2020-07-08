from sys import builtin_module_names

import numpy as np
import cv2

buffer = []

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # height of the frame

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # choose codec

out = cv2.VideoWriter('eggs-reverse.avi', fourcc, 30.0, (w, h))

while True:
    ret, I = cap.read()
    if ret == False:  # end of video (or error)
        break
    buffer.append(I)   # add frame I at the end of the buffer
    buffer.reverse()
for frame in buffer:
    out.write(frame)
cap.release()
out.release()