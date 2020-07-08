import numpy as np
import cv2

#img = cv2.imread('branches2.jpg').astype(np.float32) / 255
img= cv2.imread('isfahan.jpg').astype(np.float32) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 1  # initial filter size,

gm = 3  # gaussian filter size


# with m = 1 the input image will not change
filter = 'b'  # box filter


sigma_color = 0.5
sigma_space = 81



while True:

    # add noise to image
    N = np.random.rand(*img.shape) * noise_sigma
    J = img + N

    if filter == 'b':
        blur = cv2.blur(J, (m,m))
        # filter with a box filter
    elif filter == 'g':
        # filter with a Gaussian filter
        blur = cv2.GaussianBlur(J, (gm, gm), 0)
        pass
    elif filter == 'l':
        blur = cv2.bilateralFilter(J,m, sigma_color, sigma_space)
        #cv2.bilateralFilter(J, blur,size, sigma_color, sigma_space)
        # filter with a bilateral filter
        pass

    # filtered image

    cv2.imshow('img', blur)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')

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
        # increase noise
        noise_sigma=noise_sigma+0.1
        if noise_sigma>1 :
            noise_sigma=1
        print('noise_sigma=', noise_sigma)
        pass
    elif key == ord('d'):
        # decrease noise
        noise_sigma=noise_sigma-0.1
        if noise_sigma<0 :
            noise_sigma=0
        print('noise_sigma=',noise_sigma)
        pass
    elif key == ord('p'):
        # increase gm
        gm=gm+2
        print('gussian_sigma=', gm)
        pass
    elif key == ord('n'):
        # decrease gm
        gm=gm-2
        if gm<1 :
            gm=1
        print('gussian_sigma=',gm)
        pass
    elif key == ord('>'):
        # increase size
        size=size+1
        print('size=', size)
        pass
    elif key == ord('<'):
        # decrease size
        size=size-1
        if size<1 :
            size=1
        print('size=',size)
        pass
    elif key == ord('q'):
        break  # quit

cv2.destroyAllWindows()
