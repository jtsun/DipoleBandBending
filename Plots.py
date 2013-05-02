#!/usr/bin/env python
"""
You can control the axis tick and grid properties
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pylab
from matplotlib.patches import Polygon


# Define the Dipole function
def double_sigma(x):
  return 1/(sigma*sqrt(2*np.pi))*exp(-(x-mu1)**2/(2*sigma**2))-1/(sigma*sqrt(2*np.pi))*exp(-(x-mu2)**2/(2*sigma**2))

# MATLAB style
xticklines = getp(gca(), 'xticklines')
yticklines = getp(gca(), 'yticklines')
xgridlines = getp(gca(), 'xgridlines')
ygridlines = getp(gca(), 'ygridlines')
xticklabels = getp(gca(), 'xticklabels')
yticklabels = getp(gca(), 'yticklabels')

setp(xticklines, 'linewidth', 3)
setp(yticklines, 'linewidth', 3)
#setp(xgridlines, 'linestyle', '-')
#setp(ygridlines, 'linestyle', '-')
setp(yticklabels, 'color', 'b', fontsize='medium')
setp(xticklabels, 'color', 'b', fontsize='medium')

plt.xlabel('Displacement in z',fontsize='large')
plt.ylabel('V(z)',fontsize='large')


x=arange(-6,6,0.02)

# Define the vacuum/capacitor region for shading
ix=arange(-1.75, 1.75, 0.02)
iy = ix/ix
verts = [(-1.75,-1)] + list(zip(ix,iy)) + [(1.75,-1)]
poly = Polygon(verts, facecolor='0.8', edgecolor='k')


# Functions y1 (Dipole) y3 (Oringinal bands) y4 (Modified bands)

y3=0.5*abs(x)/x
# Define the regions where y is hidden
ym3=ma.masked_where(x > -1.75, y3)
yp3=ma.masked_where(x < 1.75, y3)


#PLOT
plt.title('Band Alingnment')
plt.plot(x,ym3,x,yp3,'-',lw=2,color='r')
plt.grid(True)
ax = subplot(111)
ax.add_patch(poly)
pylab.ylim([-0.6001,0.6001])
# Define dashed lines for band edges in gap
ax.axhline(y=0.5,xmin=0.354,xmax=0.645,color='black',linestyle='dashed',lw=2)
ax.axhline(y=-0.5,xmin=0.354,xmax=0.645,color='black',linestyle='dashed',lw=2)
# Insert offset arrow
ax.arrow(0, -0.5, 0, 1, head_width=0.2, head_length=0.05, fc='k', ec='k' , length_includes_head=True)
ax.arrow(0, 0.5, 0, -1, head_width=0.2, head_length=0.05, fc='k', ec='k' , length_includes_head=True)
#plt.show()
plt.savefig('BareBands.png', bbox_inches=0)

# Dipole plot
mu1 = -0.5
mu2 = 0.5
sigma=0.75

y1 = double_sigma(x)

plt.title('Thin Film Dipole')
plt.plot(x,y1,'-',lw=2,color='r')
plt.grid(True)
# Define the vacuum/capacitor region for shading
cx = subplot(111)
cx.add_patch(poly)
# Set Limits
pylab.ylim([-0.6001,0.6001])
plt.xlabel('Displacement in z',fontsize='large')
plt.ylabel('V(z)',fontsize='large')
#plt.show()
plt.savefig('BareDipole.png', bbox_inches=0)

y4=y3+y1

plt.title('Modified Band Alingnment')
# Define the regions where y is hidden
ym4=ma.masked_where(x > -1.75, y4)
yp4=ma.masked_where(x < 1.75, y4)
# Define the vacuum/capacitor region for shading
bx = subplot(111)
bx.add_patch(poly)
# Define dashed lines for band edges in gap
gamma = -0.5+double_sigma(-1.75)
beta  = 0.5+double_sigma(1.75)
plt.axhline(y=gamma,xmin=0.354,xmax=0.645,color='black',linestyle='dashed',lw=2)
plt.axhline(y=beta,xmin=0.354,xmax=0.645,color='black',linestyle='dashed',lw=2)

plt.plot(x,ym4,x,yp4,x,y1,lw=2)
plt.grid(True)
pylab.ylim([-0.6001,0.6001])
plt.xlabel('Displacement in z',fontsize='large')
plt.ylabel('V(z)',fontsize='large')
# Insert offset arrow
plt.arrow(0, gamma, 0, beta-gamma, head_width=0.2, head_length=0.05, fc='k', ec='k' , length_includes_head=True)
plt.arrow(0, beta, 0, gamma-beta, head_width=0.2, head_length=0.05, fc='k', ec='k' , length_includes_head=True)
#plt.show()
plt.savefig('BentBands.png',bbox_inches=0)
