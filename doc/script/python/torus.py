'''torus.py'''
import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import math

def coil(R,r,n):
	# R = major radius, center of torus to center of tube
	# r = minor radius, radius of the tube
	# n = num winds 
	t = np.linspace(0, 2*np.pi, 1000)

	x = (R + (r * np.cos(n * t))) * np.cos(t)
	y = (R + (r * np.cos(n * t))) * np.sin(t)
	z = r * np.sin(n * t)

	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.plot(x,y,z)
	plt.show()

coil(6,2,50)

