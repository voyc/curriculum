''' ispiral.py  - interactive spiral '''

import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons
import copy

# spiral equation
style = 'arithmetic'
a = .5
b = .5

# spiral drawing
radius = 0
nPoints = 40
nRings = 4
nArmsCW = 1
nArmsCCW = 0

# view settings
polar = True 
matrix = True
spin = 31
flip = 9

fig = plt.figure(figsize=(10,8))
plt.subplots_adjust(bottom=0.25,top=0.98,left=0.04,right=0.98)

specf = fig.add_gridspec(ncols=1, nrows=1)
spect = fig.add_gridspec(ncols=3, nrows=1, width_ratios = [0.2, 0.4, 0.3])
specp = fig.add_gridspec(ncols=2, nrows=1, width_ratios = [0.4, 0.6])
specm = fig.add_gridspec(ncols=2, nrows=1, width_ratios = [0.6, 0.3])

axp = fig.add_subplot(spect[0], projection='polar')
axc = fig.add_subplot(spect[1], projection='3d')
axd = fig.add_subplot(spect[2]) # matrix

axd.spines['bottom'].set_linewidth(0)
axd.spines['left'].set_linewidth(0)
axd.spines['top'].set_linewidth(0)
axd.spines['right'].set_linewidth(0)

def showViews():
	axp.set_visible(polar)
	axd.set_visible(matrix)
	axp.set_position(spect[0].get_position(fig))

	if polar and matrix:
		axc.set_position(spect[1].get_position(fig))
	elif polar:
		axc.set_position(specp[1].get_position(fig))
		axp.set_position(specp[0].get_position(fig))
	elif matrix:
		axc.set_position(specm[0].get_position(fig))
	else:	
		axc.set_position(specf[0].get_position(fig))

def showEquation():
	eq = {
		'arithmetic':  'r = (a * theta) + b',
		'circle':      'r = (a * theta) + b where a=0',
		'logarithmic': 'r = a * (e ** (b * theta))',
		'parabolic':   'r = a * (theta ** .5)',
		'hyperbolic':  'r = a / theta'
	}
	eqt = eq[style]

	axeq.cla()
	axeq.text(0,.5,eqt)
	axeq.set_xticklabels([])
	axeq.set_yticklabels([])
	axeq.set_xticks([])
	axeq.set_yticks([])
                
def calc_polar_r(style, theta, a, b):
	r = False
	if style == 'arithmetic':
		r = (a * theta) + b  
		# a is a scalar times theta, 
		# b is a constant in units of the radius

	elif style == 'circle':
		a = 0
		r = (a * theta) + b  
		# a special case of arithmetic spiral where a=0 and b is the radius

	elif style == 'r=theta':
		a = 1
		b = 0
		r = (a * theta) + b
		# special case of arithmetic spiral where r = theta

	elif style == 'logarithmic':
		r = a * (np.e ** (b * theta))  # required: 0 < varyxy < 1

	elif style == 'parabolic':
		r = a * (theta ** .5)  # required: varyxy => 0

	elif style == 'hyperbolic':
		r = a / theta  # Required: theta > 0 

	else:
		print('unrecognized style')
		quit()
	return r

def drawspiral():
	start = 0
	if style == 'hyperbolic':
		start = 1
	theta = np.linspace(start, nRings*2*np.pi, nRings*nPoints)
	r = calc_polar_r(style, theta, a, b)

	# redraw polar
	if polar:
		axp.cla()
		axp.plot(theta,r)
	
	# redraw cartesian
	if True:
		global flip,spin
		flip = axc.elev
		spin = axc.azim
		x = r * np.cos(theta)
		y = r * np.sin(theta)
		z = theta # range(0, len(theta),1)
		axc.cla()  # clear axes
		axc.plot(x,y,z)
		axc.view_init(flip, spin)
		if radius > 0: # zero indicaates auto radius to fit graph
			axc.set_xlim([-radius,radius])
			axc.set_ylim([-radius,radius])
		else:
			axc.set_xlim(auto=True)
			axc.set_ylim(auto=True)

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
			row_text = [f'{theta[i]:.2f}',f'{r[i]:.2f}',f'{x[i]:.2f}',f'{y[i]:.2f}']
			cell_text.append(row_text)
		col_labels = ('theta', 'r', 'x', 'y')
		axd.cla()
		axd.table(cell_text, loc='center', colLabels=col_labels)
		axd.set_xticklabels([])
		axd.set_yticklabels([])
		axd.set_xticks([])
		axd.set_yticks([])

	axa.set_visible(style != 'circle')
	axb.set_visible(style not in ('parabolic', 'hyperbolic'))
	plt.draw()

# anime - rotate the axes and update
#	for angle in range(0, 360):
#		ax.view_init(angle, angle)
#		plt.draw()
#		plt.pause(.001)
# https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
# https://matplotlib.org/2.2.5/gallery/mplot3d/rotate_axes3d.html

# setup UI
axcolor = 'lightgoldenrodyellow'
axeq    = plt.axes([0.25, 0.24, 0.30, 0.03])
axa     = plt.axes([0.25, 0.20, 0.30, 0.03], facecolor=axcolor)
axb     = plt.axes([0.25, 0.16, 0.30, 0.03], facecolor=axcolor)
axradius= plt.axes([0.25, 0.10, 0.30, 0.03], facecolor=axcolor)
axpoints= plt.axes([0.25, 0.06, 0.30, 0.03], facecolor=axcolor)
axcwarm = plt.axes([0.70, 0.06, 0.25, 0.03], facecolor=axcolor)
axrings = plt.axes([0.25, 0.02, 0.30, 0.03], facecolor=axcolor)
axccwarm= plt.axes([0.70, 0.02, 0.25, 0.03], facecolor=axcolor)

axstyle = plt.axes([0.025, 0.12, 0.15, 0.15], facecolor=axcolor)
axpolar = plt.axes([0.025, 0.02, 0.15, 0.09], facecolor=axcolor)

axeq.spines['bottom'].set_linewidth(0)
axeq.spines['left'].set_linewidth(0)
axeq.spines['top'].set_linewidth(0)
axeq.spines['right'].set_linewidth(0)

sliderpoints = Slider(axpoints, 'Points', 1, 50, valinit=nPoints, valfmt='%i')
def setpoints(n):
	global nPoints
	nPoints = int(n)
	drawspiral()
sliderpoints.on_changed(setpoints)

sliderrings = Slider(axrings, 'Rings', 1, 50, valinit=nRings, valfmt='%i')
def setrings(n):
	global nRings
	nRings = int(n)
	drawspiral()
sliderrings.on_changed(setrings)

slidercwarm = Slider(axcwarm, 'CW Arms', 0, 10, valinit=nArmsCW, valfmt='%i')
def setcwarm(n):
	global nArmsCW
	nArmsCW = int(n)
	drawspiral()
slidercwarm.on_changed(setcwarm)

sliderccwarm = Slider(axccwarm, 'CCW Arms', 0, 10, valinit=nArmsCCW, valfmt='%i')
def setccwarm(n):
	global nArmsCCW
	nArmsCCW = int(n)
	drawspiral()
sliderccwarm.on_changed(setccwarm)

sliderradius = Slider(axradius, 'Radius', 0, 50, valinit=radius, valfmt='%i')
def setradius(value_selected):
	global radius 
	radius = int(value_selected)
	drawspiral()
sliderradius.on_changed(setradius)

slidera = Slider(axa, 'a', 0, 1, valinit=a, valfmt='%f')
def seta(value_selected):
	global a 
	a = value_selected
	drawspiral()
slidera.on_changed(seta)

sliderb = Slider(axb, 'b', 0, 1, valinit=b, valfmt='%f')
def setb(value_selected):
	global b 
	b = value_selected
	drawspiral()
sliderb.on_changed(setb)

radiostyle = RadioButtons(axstyle, ('circle', 'arithmetic', 'logarithmic', 'parabolic', 'hyperbolic'), active=1)
def setstyle(value_selected):
	global style
	style = value_selected
	showEquation()
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
showEquation()
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

