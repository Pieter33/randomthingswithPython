# foreground extraction.
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('give path to image with extension')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (280,325,750,500) # x_init y_init width height

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()