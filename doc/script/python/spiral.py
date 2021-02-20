'''spiral.py'''
from plothelper import *

# source: https://matplotlib.org/3.1.1/gallery/misc/transoffset.html#sphx-glr-gallery-misc-transoffset-py

title = 'Archimedes Spiral'
                                # pairs of points in polar coordinates
theta = np.arange(5, 100, .1)   #    angle in radians (1 radian ~ 57 degrees)
r = theta                       #    distance from the origin

plt.polar(theta, r, '-b')
formatspiral(title)
savegraph(title)
plt.show()

	
title = 'Logarithmic Spiral'
a = .1                          # constant, rate of increase of the spiral
e = 1.618202                    # constant, Euler's number (about 1.618282) 
                                # pairs of points in polar coordinates
theta = np.arange(50, 100, .1)  #    angle in radians (1 radian ~ 57 degrees)
r = e**(a*theta)                #    distance from the origin

plt.polar(theta, r, '-b')
formatspiral(title)
savegraph(title)
plt.show()

