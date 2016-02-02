# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:37:11 2016

@author: LongNT
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import PIL

img = PIL.Image.open("img/Gijon.jpg")
R, G, B = img.split()
R = np.array(R)
G = np.array(G)
B = np.array(B)

his = img.histogram()

fig = plt.figure("Ma figure");
plt.clf()
ax = fig.add_subplot(2, 2, 1)
ax.set_title("Red")
plt.imshow(R, cmap = cm.gray)
plt.grid()
plt.colorbar()

#ax = fig.add_subplot(2, 2, 2)
#ax.set_title("Green")
#plt.imshow(G)
#plt.grid()
#plt.colorbar()
#
#
#ax = fig.add_subplot(2, 2, 3)
#ax.set_title("Blue")
#plt.imshow(B)
#plt.grid()
#plt.colorbar()

ax = fig.add_subplot(2, 2, 2)
ax.set_title("Red filtered > 100")
plt.imshow(R > 100, cmap = cm.gray)
plt.grid()
plt.colorbar()

ax = fig.add_subplot(2, 2, 3)
ax.set_title("Histogram")
plt.hist(R.flatten(), bins = 250)
plt.grid()
plt.colorbar()

plt.show()