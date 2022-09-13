'''spiraltorus.py'''
import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import math


#coil(6,2,5)
#coil(6,1,10)
#coil(6,5,20)


#HelixPlot[R_, r_, n_] := 
#
#Show[
#	# translucent tube
#	ParametricPlot3D[ 
#		{(R + r Cos[t]) Cos[u], (R + r Cos[t]) Sin[u], r Sin[t]}, 
#		{t, 0, 2 Pi}, 
#		{u, 0, 2 Pi}, 
#		PlotPoints -> 30, 
#		Mesh -> None, 
#		PlotStyle -> Opacity[0.3]
#	], 
#	
#	# wire coil
#	ParametricPlot3D[
#		{(R + r Cos[n*t]) Cos[t], (R + r Cos[n*t]) Sin[t], r Sin[n*t]}, 
#		{t, 0, 2 Pi}, 
#		PlotPoints -> 30, 
#		PlotStyle -> {Thick, Black}
#	]
#]


#t = np.linspace(-10, 10, 100)  # create array as parameter t
t = np.linspace(0, 2*math.pi, 1000)  # create array as parameter t
 
a = 6    # major radius
b = 2    # minor radius
n = 5   # num winds 

x = (a + (b * np.cos(n * t))) * np.cos(t)
y = (a + (b * np.cos(n * t))) * np.sin(t)
z = b * np.sin(n * t)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x,y,z)
plt.show()


