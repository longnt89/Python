# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 16:08:15 2016

@author: LongNT
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = np.linspace(0., 10., 1000)
y = np.sin(2. * np.pi * x)

fig = plt.figure("Animation!")

plt.clf()
line, = plt.plot([], [])
plt.grid()
plt.xlim(0., 10.)
plt.ylim(-1., 1.)

def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,
    
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 1000, interval = 20, blit = True)

plt.show()