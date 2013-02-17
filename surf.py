import cv2

from PIL import Image
from numpy import *
from pylab import *


# read image

im = cv2.imread('empire.jpg')

# down sample

im_lowres = cv2.pyrDown(im)

# convert to grayscale

gray = cv2.cvtColor(im_lowres,cv2.COLOR_RGB2GRAY)

# detect feature points

s = cv2.SURF()

mask = uint8(ones(gray.shape))

keypoints = s.detect(gray,mask)

# show image and points

vis = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

for k in keypoints[::10]:

    cv2.circle(vis,(int(k.pt[0]),int(k.pt[1])),2,(0,255,0),-1)

    cv2.circle(vis,(int(k.pt[0]),int(k.pt[1])),int(k.size),(0,255,0),2)

cv2.imshow('local descriptors',vis)

cv2.waitKey()
