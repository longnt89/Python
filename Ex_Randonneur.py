# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:17:08 2016

@author: LongNT
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def lire_header(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    out = {} # It is the declaration of an empty dictionary.
    for line in lines:
        if "=" in line:
            key = line.split("=")[0].split()[0]
            if key in ["lines", "samples"]:
                out[key] = int(line.split("=")[1])
    return out
    
def read_data(path):
    f = open(path, "rb")
    #data = f.read()
    out = np.fromfile(f, dtype = np.float32)
    f.close()
    #out = struct.unpack(data, "<")
    return out

header_path = "img/BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data_path = "img/BossonsDEM_ll8m"
data = read_data(data_path)

dx = 1.03112519e1
dy = 7.19750606e1

nx = header["samples"]
ny = header["lines"]
x = np.arange(nx) * dx
y = np.arange(ny) * dy

X, Y = np.meshgrid(x, y)
Z = data.reshape(ny, nx)

fig = plt.figure(0)
plt.clf()
plt.contourf(X, Y, Z, 100, cmap= matplotlib.cm.terrain)
cbar = plt.colorbar()
cbar.set_label = ("Attitude, $z$ [m]")
plt.contour(X, Y, Z, 20, colors = "k")
plt.grid()
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")
plt.show()