import cv2
import numpy as np

I = cv2.imread('karimi.jpg',0)

# centre of the image
c = np.array([[I.shape[1]/2.0], [I.shape[0]/2.0]])
print(c)

for theta in range(0,360):
    th = theta * np.pi / 180 # convert to radians

    R = np.array([[np.cos(th),-np.sin(th)],
                  [np.sin(th), np.cos(th)]])

             # you need to change this!
    t1=np.dot(R,c)
    t=c-t1    
    # concatenate R and t to create the 2x3 transformation matrix

    R1 = np.array([[1,0],[0,1]])
    t1 = c 
    N = np.hstack([R,t])
    J = cv2.warpAffine(I,N, (I.shape[1], I.shape[0]) )



    cv2.imshow('J',J)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

