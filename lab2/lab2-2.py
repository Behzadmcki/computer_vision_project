import cv2
import numpy as np
I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')
print(I.shape)
print(J.shape)
# K = I.copy()
# K[::3,::3,:] = J[::3,::3,:]
# K = I//2+J//2
K = (0*I + 1*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.1*I + 0.9*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.15*I + 0.85*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.2*I + 0.8*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.25*I + 0.75*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.3*I + 0.7*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.35*I + 0.65*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.4*I + 0.6*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.45*I + 0.55*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.5*I + 0.5*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.55*I + 0.45*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.6*I + 0.4*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.65*I + 0.35*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.7*I + 0.3*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.75*I + 0.25*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.8*I + 0.2*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.85*I + 0.15*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.9*I + 0.1*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (0.95*I + 0.05*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)
K = (1*I + 0*J).astype(np.uint8)
cv2.imshow("Blending", K)
cv2.waitKey(150)

cv2.destroyAllWindows()
