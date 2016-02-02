# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 09:13:06 2016

@author: LongNT
"""

import numpy as np

class MetaPoint(object):
    def __init__(self, x = 0., y = 0., z = 0.):
        self.coords = np.array([x, y, z])
        
class Point(MetaPoint):
    def __repr__(self):
        c = self.coords
        return "<Point: ({0}, {1}, {2})>".format(c[0], c[1], c[2])

class Vector(MetaPoint):
    def __init__(self, x = 0., y = 0., z = 0.):
        self.coords = np.array([x, y, z])
        
    def __repr__(self):
        c = self.coords        
        return "<Vector: {0} {1} {2}>".format(c[0], c[1], c[2])
    
    def norme(self):
        return (self.coords**2).sum()**.5
    
    def normaliser(self):
        n = self.norme()
        self.coords /= n
    
    def __mul__(self, other):
        out = Vector()
        if isinstance(other, Vector):
            out.coords = np.cross(self.coords, other.coords)
        else:
            out.coords = self.coords * other
        return out
        
    __rmul__ = __mul__
    
u = Vector(1, 0, 0)
v = Vector(4., 5., -1.)