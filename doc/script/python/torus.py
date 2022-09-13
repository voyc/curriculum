'''torus.py'''
import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
import math


#coil(6,2,5)
#coil(6,1,10)
#coil(6,5,20)



#t = np.linspace(-10, 10, 100)  # create array as parameter t
t = np.linspace(0, 2*math.pi, 1000)  # create array as parameter t
 
a = 6    # major radius
b = 2    # minor radius
n = 5   # num winds 

x = (a + (b * np.cos(n * t))) * np.cos(t)
y = (a + (b * np.cos(n * t))) * np.sin(t)
z = b * np.sin(n * t)


x = ( (((R+r)/2) + ((R+r)/2)) * (np.cos({αt} \right ) \cos{βt} \\
y = ( \frac{R+r}{2} + \frac{R−r}{2} \cos{αt} \right ) \sin{βt} \\
z = \frac{R−r}{2} \sin{αt} \\

def coil(R,r,n):
    # R = major radius, center of torus to center of tube
    # r = minor radius, radius of the tube
    # n = num winds 
    t = np.linspace(0, 2*np.pi, 1000)
    x = (R + (r * np.cos(n * t))) * np.cos(t)
    y = (R + (r * np.cos(n * t))) * np.sin(t)
    z = r * np.sin(n * t)
    s = '_'+str(R)+'_'+str(r)+'_'+str(n)
    sObj = 'CurveObj'+s
    sCurve = 'Curve'+s
    return makePolyLine(sObj, sCurve, x,y,z)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x,y,z)
plt.show()


