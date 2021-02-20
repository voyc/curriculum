'''plothelper.py'''
import numpy as np
import matplotlib.pyplot as plt  

plotfolder = '/home/john/webapps/curriculum/curriculum/doc/dokuwiki/data-media/'

def formatgraph(title):
	fig = plt.gcf()
	fig.set_size_inches(4,3)
	ax = plt.gca();
	ax.spines['right'].set_position('zero')
	ax.spines['top'].set_position('zero')
	ax.spines['bottom'].set_linewidth(0)
	ax.spines['left'].set_linewidth(0)
	plt.grid()
	if title:
		plt.title(title)
	plt.legend() # (loc=9) upper-center
	return;

def formatspiral(title):
	fig = plt.gcf()
	fig.set_size_inches(4,3)
	ax = plt.gca();
	ax.spines['polar'].set_visible(False)
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	plt.grid(False)
	if title:
		plt.title(title)
	return;

def savegraph(title):
	fig = plt.gcf()
	fname = title.replace(' ', '_');
	fname = fname.replace(',', '');
	fname = fname.replace('\'', '');
	fname = fname.lower();
	fname = plotfolder + fname + '.png'
	fig.savefig(fname);
	return;
