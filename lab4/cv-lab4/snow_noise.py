import numpy as np
import cv2

I = cv2.imread('isfahan.jpg', cv2.IMREAD_GRAYSCALE);
I = I.astype(np.float) / 255

sigma = 0.04 # initial standard deviation of noise
J = I

while True:
    
 # change this line so J is the noisy image
    
    cv2.imshow('snow noise',J)
    print(sigma)
    # press any key to exit
    key = cv2.waitKey(33)
    N = np.random.randn(*I.shape) * sigma
    J = I + N
    if key & 0xFF == ord('u'):
        # if 'u' is pressed
        sigma=sigma+0.1
        if sigma>1 :
            sigma=1
       # N = np.random.randn(*I.shape) * sigma
        #J = I + N

        pass # increase noise
    elif key & 0xFF == ord('d'):  # if 'd' is pressed
        sigma=sigma-0.1
        if sigma<0 :
            sigma=0
       # N = np.random.randn(*I.shape) * sigma
        #J = I + N

        pass # decrease noise 
    elif key & 0xFF == ord('q'):  # if 'q' is pressed then 
        break # quit
    
cv2.destroyAllWindows()
