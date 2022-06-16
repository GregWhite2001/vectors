################################################
#name: Gregory Whitehurst
#file: vectors.py
#description: a python class to emulate
# vectors and their operations
################################################

#might need this, don't know yet
from cmath import sqrt
from math import asin, sin
import sympy as sym
COMPONENT_FORM = True
sym.init_printing(use_unicode=True)
#making t global for referencing it everywhere
global t
t = sym.symbols('t')
class Vector:

    
    #constructor
    #default vector is the zero vector
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z

    #accessor for x
    @property
    def x(self):
        return self.x

    #mutator for x
    @x.setter
    def x(self, value):
        self._x = value

    #accessor for y
    @property
    def y(self):
        return self.y

    #mutator for y
    @y.setter
    def y(self, value):
        self._y = value

    #accessor for z
    @property
    def z(self):
        return self.z

    #mutator for z
    @z.setter
    def z(self, value):
        self._z = value

    #magic string function
    #has the option for unit vector component form
    def __str__(self):
        if COMPONENT_FORM == False:
            return f"({self._x})i+({self._y})j+({self._z})k"
        return f"<{self._x},{self._y},{self._z}>"

    #vector addition
    def addVector(self, other):
        new_vect = Vector()
        new_vect.x = self._x + other._x
        new_vect.y = self._y + other._y
        new_vect.z = self._x + other._z
        return new_vect

    #vector subtraction
    def subtractVector(self, other):
        new_vect = Vector()
        new_vect.x = self._x - other._x
        new_vect.y = self._y - other._y
        new_vect.z = self._x - other._z
        return new_vect

    #dot product, returns scalar value
    def dotProduct(self,other):
        return self._x*other._x + self._y*other._y + self._z*other._z

    #vector cross product, returns a vector
    def crossProduct(self, other):
        new_vect = Vector()
        new_vect._x = self._y * other._z - self._z * other._y
        new_vect._x = self._z * other._x - self._x * other._z
        new_vect._x = self._x * other._y - self._y * other._x
        return new_vect

    #checks if two vectors are orthogonal if the dot product of
    #two vectors is 0, returns boolean
    def isOrthogonal(self,other):
        if Vector.dotProduct(self,other) == 0:
            return True
        else:
            return False

    def magnitude(self):
        return sym.sqrt((self._x)**2 + (self._y)**2 + (self._z)**2)
        #working on this
        '''if mag > int(mag) and mag < int(mag)+1:
            return mag
        else:
            return int(mag)'''
        
    #checking if two vectors are parallel by checking if their cross product
    #is equal to the zero vector
    def isParallel(self, other):
        test_vect = Vector.crossProduct(self, other)
        if(test_vect._x == 0 and test_vect._y == 0 and test_vect._z == 0):
            return True
        else:
            return False

    #also working on this 
    '''def crossProductMagnitude(self, other):
        return (Vector.magnitude(self) * Vector.magnitude(other)) * sin(
            asin(Vector.magnitude(Vector.crossProduct(self,other))/
            (Vector.magnitude(other)*Vector.magnitude(self))))'''

    #differentiate a vector function
    def differentiate(self):
        Dr = Vector()
        Dr._x = sym.diff(self._x)
        Dr._y = sym.diff(self._y)
        Dr._z = sym.diff(self._z)
        return Dr

    #integrate a vector function
    def integrate(self):
        R = Vector()
        R._x = sym.integrate(self._x,t)
        R._y = sym.integrate(self._y,t)
        R._z = sym.integrate(self._z,t)
        return R

    def arcLength(self, a, b):
        return (sym.integrate(sym.simplify(Vector.magnitude(self)),(t,a,b)))