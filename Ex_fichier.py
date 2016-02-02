# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:25:27 2016

@author: LongNT
"""

import numpy as np

data = np.random.rand(100, 4)

f = open("data.dat", "w")
for i in xrange(len(data)):
    for j in xrange(len(data[i])):
        f.write("{0:.2f} ".format(data[i, j]))
    f.write("\n")
        
f.close()