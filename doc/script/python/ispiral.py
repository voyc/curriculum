''' 
ispiral.py  - interactive spiral

polar equation for spiral = r, theta, where r = radius
equation for circle = x**2 + y**2 = r**2
circle = spiral with no delta r
helix = circle with delta z
'''

import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons

ax  = False  # ax for 3d view
axp = False  # axp for polar view

# sine wave
#t = np.arange(0.0, 1.0, 0.001)
#a0 = 5
#f0 = 3
#delta_f = 5.0
#s = a0 * np.sin(2 * np.pi * f0 * t)
#l, = plt.plot(t, s, lw=2)
#ax.margins(x=0)

# spiral settings
nRings = 4
nArmscw = 1
nArmsccw = 0
radius = 10
theta = 1
style = 'arithmetic'
deltaz = 1
deltar = .01

# view settings
polar = False
spin = 31
flip = 9

def setupview():
	print('setupview')
	fig = plt.figure()
	fig.set_size_inches(8,8)
	plt.subplots_adjust(bottom=0.25)
	if polar:
		axp = fig.add_subplot(121, projection='polar')
		ax  = fig.add_subplot(122, projection='3d')
	else:
		ax = fig.add_subplot(111, projection='3d')
	return ax

def calc_polar_r(r, theta, spiralstyle, a):
	rs = False
	if spiralstyle == 'circle':
		rs = r
	elif spiralstyle == 'arithmetic':
		rs = theta
	elif spiralstyle == 'logarithmic':
		rs = r ** (a * theta)  # required: 0 < varyxy < 1
	elif spiralstyle == 'parabolic':
		rs = a * (theta ** .5)  # required: varyxy => 0
	elif spiralstyle == 'hyperbolic':
		rs = a / theta  # Required: theta > 0 
	else:
		print('unrecognized spiral type')
		quit()
	return rs

def drawspiral():
	theta = np.linspace(1, nRings*2*np.pi, nRings*360)

	rs = calc_polar_r(radius,theta,style,deltar)
	x = rs * np.cos(theta)
	y = rs * np.sin(theta)
	z = deltaz * theta

	ax.cla()  # clear axes
	ax.plot(x,y,z)


	# plot a second arm in the reverse direction
	if False: #nArms == 2:
		x = 0 - x
		y = 0 - y
		ax.plot(x,y,z)

	#ax.plot(x,y,z)

	# rotate the axes and update
#	for angle in range(0, 360):
#		ax.view_init(angle, angle)
#		plt.draw()
#		plt.pause(.001)
	ax.view_init(flip, spin)
	plt.draw()


ax = setupview()

# setup UI
axcolor = 'lightgoldenrodyellow'
axrings = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
axradius= plt.axes([0.25, 0.16, 0.65, 0.03], facecolor=axcolor)
axdeltar= plt.axes([0.25, 0.12, 0.65, 0.03], facecolor=axcolor)
axspin  = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor=axcolor)
axflip  = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor=axcolor)

axstyle = plt.axes([0.025, 0.12, 0.15, 0.15], facecolor=axcolor)
axpolar  = plt.axes([0.025, 0.02, 0.15, 0.09], facecolor=axcolor)

sliderrings = Slider(axrings, 'Rings', 1, 50, valinit=nRings, valfmt='%i')
def setrings(n):
	global nRings
	nRings = int(n)
	drawspiral()
sliderrings.on_changed(setrings)

sliderradius = Slider(axradius, 'Radius', 1, 20, valinit=radius, valfmt='%i')
def setradius(value_selected):
	global radius 
	radius = int(value_selected)
	drawspiral()
sliderradius.on_changed(setradius)

sliderdeltar = Slider(axdeltar, 'Delta R', 0.01, 0.09, valinit=deltar, valfmt='%f')
def setdeltar(value_selected):
	global deltar 
	deltar = value_selected
	drawspiral()
sliderdeltar.on_changed(setdeltar)

sliderspin = Slider(axspin, 'Spin', -180, 180, valinit=spin, valfmt='%i')
def setspin(value_selected):
	global spin
	spin = value_selected
	drawspiral()
sliderspin.on_changed(setspin)

sliderflip = Slider(axflip, 'Flip', -180, 180, valinit=flip, valfmt='%i')
def setflip(value_selected):
	global flip
	flip = value_selected
	drawspiral()
sliderflip.on_changed(setflip)

radiostyle = RadioButtons(axstyle, ('circle', 'arithmetic', 'logarithmic', 'parabolic', 'hyperbolic'), active=1)
def setstyle(value_selected):
	global style
	style = value_selected
	drawspiral()
radiostyle.on_clicked(setstyle)

checkboxpolar = CheckButtons(axpolar, ('polar',), (polar,))
def setpolar(value_selected):
	global polar
	polar = not polar
	print(polar)
	setupview()
	drawspiral()
checkboxpolar.on_clicked(setpolar)

drawspiral()
plt.show() # block




quit()
drawspiral( nRings=4,nArms=2,r=10,spiralstyle='arithmetic', varyz=.1)
drawspiral( nRings=4,nArms=2,r=10,spiralstyle='logarithmic', varyz=.1, a=.01)
drawspiral( nRings=4,nArms=2,r=5,spiralstyle='parabolic', varyz=.1, a=.1)
drawspiral( nRings=4,nArms=2,r=5,spiralstyle='hyperbolic', varyz=.1, a=45)
quit()
drawspiral( 4,10,spiralstyle='circle')
drawspiral( 4,10,spiralstyle='circle', varyz=.1)
drawspiral(44, 5,spiralstyle='circle', varyz=.1)
drawspiral( 4,10,spiralstyle='arithmetic')
drawspiral( 4,10,spiralstyle='arithmetic', varyz=.1)
drawspiral( 4,10,spiralstyle='logarithmic', a=.01)
drawspiral( 4,10,spiralstyle='logarithmic', varyz=.1, a=.01)
drawspiral( 4, 5,spiralstyle='parabolic', a=.1)
drawspiral( 4, 5,spiralstyle='parabolic', varyz=.1, a=.1)
drawspiral( 4, 5,spiralstyle='hyperbolic', a=45)
drawspiral( 4, 5,spiralstyle='hyperbolic', varyz=.1, a=45)

