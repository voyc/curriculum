''' ispiral.py  - interactive spiral '''

import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons
import copy

# spiral settings
nPoints = 6
nRings = 4
nArmscw = 1
nArmsccw = 0
radius = 10
theta = 1
style = 'arithmetic'
deltaz = 1
deltar = .01

# view settings
polar = True 
matrix = True
spin = 31
flip = 9

fig = plt.figure(figsize=(10,8))
plt.subplots_adjust(bottom=0.25,top=0.98,left=0.02,right=0.98)

specf = fig.add_gridspec(ncols=1, nrows=1)
spect = fig.add_gridspec(ncols=3, nrows=1, width_ratios = [0.2, 0.4, 0.3])
specp = fig.add_gridspec(ncols=2, nrows=1, width_ratios = [0.2, 0.7])
specm = fig.add_gridspec(ncols=2, nrows=1, width_ratios = [0.6, 0.3])

axp = fig.add_subplot(spect[0], projection='polar')
axc = fig.add_subplot(spect[1], projection='3d')
axd = fig.add_subplot(spect[2]) # matrix

#axd.spines['bottom'].set_linewidth(0)
#axd.spines['left'].set_linewidth(0)
axd.set_xticklabels([])
axd.set_yticklabels([])
axd.set_xticks([])
axd.set_yticks([])

def showViews():
	axp.set_visible(polar)
	axd.set_visible(matrix)

	if polar and matrix:
		axc.set_position(spect[1].get_position(fig))
	elif polar:
		axc.set_position(specp[1].get_position(fig))
	elif matrix:
		axc.set_position(specm[0].get_position(fig))
	else:	
		axc.set_position(specf[0].get_position(fig))

def calc_polar_r(r, theta, spiralstyle, a):
	rs = False
	if spiralstyle == 'circle':
		rs = r + theta - theta  # make an array the same dim as theta
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
	theta = np.linspace(1, nRings*2*np.pi, nRings*nPoints)
	rs = calc_polar_r(radius,theta,style,deltar)

	# redraw polar
	if polar:
		axp.cla()
		axp.plot(theta,rs)
	
	# redraw cartesian
	if True:
		x = rs * np.cos(theta)
		y = rs * np.sin(theta)
		#z = deltaz * theta
		z = range(0, len(theta),1)
		axc.cla()  # clear axes
		axc.plot(x,y,z)
		axc.view_init(flip, spin)

		# plot a second arm in the reverse direction
		if False: #nArms == 2:
			x = 0 - x
			y = 0 - y
			axc.plot(x,y,z)

	
	# redraw matrix - very slow
	if matrix:
		cell_text = []
		nrows = min(len(theta)-1,30)
		for i in range(0,nrows):
			row_text = [f'{theta[i]:.2f}',f'{rs[i]:.2f}',f'{x[i]:.2f}',f'{y[i]:.2f}']
			cell_text.append(row_text)
		col_labels = ('theta', 'r', 'x', 'y')
		axd.table(cell_text, loc='center', colLabels=col_labels)

	plt.draw()

# anime - rotate the axes and update
#	for angle in range(0, 360):
#		ax.view_init(angle, angle)
#		plt.draw()
#		plt.pause(.001)

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

checkboxpolar = CheckButtons(axpolar, ('polar','matrix'), (polar,matrix,))
def setview(value_selected):
	global polar,matrix
	if value_selected == 'polar':
		polar = not polar
	if value_selected == 'matrix':
		matrix = not matrix
	drawspiral()
	showViews()
checkboxpolar.on_clicked(setview)

drawspiral()
showViews()
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

