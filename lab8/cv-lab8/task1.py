import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G,220,255,cv2.THRESH_BINARY_INV)

nc1,CC1 = cv2.connectedComponents(T)

corners=0

for k in range(1,nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1;
    Ck = cv2.GaussianBlur(Ck,(5,5),0)
    Ck = cv2.cvtColor(Ck,cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck
    Ck = np.float32(Ck)
    window_size = 5
    soble_kernel_size  = 3 # kernel size for gradients
    alpha = 0.03
    H = cv2.cornerHarris(G,window_size,soble_kernel_size,alpha)
    H=cv2.dilate(H,None)
    H = H / H.max()
    C = np.uint8(H > 0.001) * 255
    nc,CC = cv2.connectedComponents(C);
    corners=nc
    for x in range(1,nc,1):
       Ck[CC==x] = [0,0,255]

    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(Ck,'There are %d vertices!'%corners,(20,30), font, 1,(0,0,255),1)

    
    cv2.imshow('corners',Ck)
    cv2.waitKey(0) # press any key



