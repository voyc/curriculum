'''helix.py'''
from plothelper import *
from mpl_toolkits.mplot3d import Axes3D

# draw one circle
# draw four circles
# vary the z axis -> helix
# vary the xy axes -> spiral
# vary both -> helical spiral

def calc_spiral_radius(r, theta, spiralstyle='archimedes', varyxy=0):
	rs = r
	if spiralstyle == 'archimedes':
		rs = theta
	elif spiralstyle == 'logarithmic':
		rs = r ** (varyxy * theta)  # required: 0 < varyxy < 1
	elif spiralstyle == 'parabolic':
		rs = varyxy * (theta ** .5)  # required: varyxy a=> 0
	elif spiralstyle == 'hyperbolic':
		rs = varyxy / theta  # Required: theta > 0 
	return rs

def drawspiral(nDim=2, nRings=1, nArms=1, r=1, spiralstyle='archimedes', varyz=0, varyxy=0):
	n_one = 360
	n_max = n_one * nRings
	theta_one = 2 * np.pi
	theta_max = nRings * theta_one
	theta = np.linspace(1, theta_max, n_max)

	rs = calc_spiral_radius(r,theta,spiralstyle,varyxy)
	x = rs * np.cos(theta)
	y = rs * np.sin(theta)
	z = varyz * theta

	fig = plt.figure()
	#ax = fig.add_subplot(111, projection='3d')
	ax = fig.add_subplot(111)

	if nArms == 2:
		x = np.concatenate((x, 0 - x))
		y = np.concatenate((y, 0 - y))
		z = np.concatenate((z, z))

	#ax.plot(x,y,z)
	ax.plot(x,y)

	plt.show()


drawspiral( nRings=4,nArms=2,r=10,spiralstyle='archimedes')
drawspiral( nRings=4,nArms=2,r=10,spiralstyle='logarithmic', varyxy=.01)
drawspiral( nRings=4,nArms=2,r=5,spiralstyle='parabolic', varyxy=.1)
drawspiral( nRings=4,nArms=2,r=5,spiralstyle='hyperbolic', varyxy=45)
quit()
drawspiral( 4,10,spiralstyle='circle')
drawspiral( 4,10,spiralstyle='circle', varyz=.1)
drawspiral(44, 5,spiralstyle='circle', varyz=.1)
drawspiral( 4,10,spiralstyle='archimedes')
drawspiral( 4,10,spiralstyle='archimedes', varyz=.1)
drawspiral( 4,10,spiralstyle='logarithmic', varyxy=.01)
drawspiral( 4,10,spiralstyle='logarithmic', varyz=.1, varyxy=.01)
drawspiral( 4, 5,spiralstyle='parabolic', varyxy=.1)
drawspiral( 4, 5,spiralstyle='parabolic', varyz=.1, varyxy=.1)
drawspiral( 4, 5,spiralstyle='hyperbolic', varyxy=45)
drawspiral( 4, 5,spiralstyle='hyperbolic', varyz=.1, varyxy=45)

