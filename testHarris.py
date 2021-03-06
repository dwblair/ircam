from PIL import Image
from numpy import *
from pylab import *


import harris
import time

im1 = array(Image.open('wave1.jpg').convert('L'))
im2 = array(Image.open('wave2.jpg').convert('L'))

wid = 5

t=time.time()
harrisim = harris.compute_harris_response(im1,5)

print "t for harrisim=", time.time()-t
t=time.time()

filtered_coords1 = harris.get_harris_points(harrisim,wid+1)

print "t for get_harris_points=", time.time()-t
t=time.time()

d1 = harris.get_descriptors(im1,filtered_coords1,wid)

print "t for get_descriptors=", time.time()-t
t=time.time()

harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print 'starting matching'
matches = harris.match_twosided(d1,d2)

figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()

"""
im = array(Image.open('empire.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im, filtered_coords)
"""
