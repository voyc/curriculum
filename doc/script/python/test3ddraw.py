import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-10, 10, 100)  # create array as parameter t
x = -1 + -1*t    # create vector x for parameter t
y = 2 + -1*t
z = 7 + 3*t

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x,y,z)
plt.show()
