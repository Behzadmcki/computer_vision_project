import numpy as np
import cv2

#I = cv2.imread('branches2.jpg').astype(np.float64) / 255
I = cv2.imread('isfahan.jpg').astype(np.float64) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 1  # initial filter size,

gm = 3  # gaussian filter size

size = 9  # bilateral filter size
sigmaColor = 0.3
sigmaSpace = 75
# with m = 1 the input image will not change
filter = 'b'  # box filter

while True:

    # add noise to image
    N = np.random.rand(*I.shape) * noise_sigma
    J = I + N
    
    #delay = 3000
    
    delay = 3000
    

    if filter == 'b':
        F = np.ones((m,m), np.float64)/(m*m)
        K = cv2.filter2D(J,-1, F)
    elif filter == 'g':
        K = cv2.GaussianBlur(J,(gm,gm),0)
        pass
    elif filter == 'l':
        Jb = J.astype(np.float32)
        K = cv2.bilateralFilter(Jb,size, sigmaColor, sigmaSpace)
        pass
    elif filter == 'o':
        K = I.copy()
        pass

    # filtered image

    cv2.imshow('img', K)
    key = cv2.waitKey(delay) & 0xFF

    if key == ord('b'):
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')
        
    elif key == ord('o'):
        filter = 'o'  # showing original image
        print('Original Image')
        
    elif key == ord('+'):
        # increase m
        m = m + 2
        print('m=', m)

    elif key == ord('-'):
        # decrease m
        if m >= 3:
            m = m - 2
        print('m=', m)
    elif key == ord('u'):
        noise_sigma += 0.01
        print('Noise sigma=', noise_sigma)
        # increase noise
        pass
    elif key == ord('d') and noise_sigma-0.02 > 0:
        noise_sigma -= 0.01
        print('Noise sigma=', noise_sigma)
        # decrease noise
        pass
    elif key == ord('p'):
        sigmaColor += 0.1
        print('sigmaColor size=', sigmaColor)
        # increase gm
        pass
    elif key == ord('n'):
        if gm >= 3:
                sigmaColor = sigmaColor - 0.1
        print('sigmaColor size=', sigmaColor)
        # decrease gm
        pass
    elif key == ord('.'):
        size += 1
        print('size=', size)
        pass
    elif key == ord(',') and size > 1:
        size -= 1
        print('size=', size)
        pass
    elif key == ord('q'):
        break  # quit

cv2.destroyAllWindows()
