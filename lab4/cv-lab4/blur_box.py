import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255;
J=I
# display the original image
cv2.imshow('original',I)
cv2.waitKey()

# creating a box filter

ksize = (5, 5)

# create an m by m box filter
image = cv2.blur(I, ksize,cv2.BORDER_REFLECT)
cv2.boxFilter(I, 0, (7,7),J, (-1,-1), False, cv2.BORDER_DEFAULT)

# Now, filter the image
cv2.imshow('blurred1',image)
cv2.waitKey()
cv2.imshow('blurred2',J)

cv2.waitKey()

cv2.destroyAllWindows()
