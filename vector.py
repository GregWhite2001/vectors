################################################
#name: Gregory Whitehurst
#file: vectors.py
#description: a python class to emulate
# vectors and their operations
################################################


import sympy as sym
from sympy.plotting import plot3d_parametric_line, plot3d_parametric_surface
COMPONENT_FORM = True
sym.init_printing(use_unicode=True)
#making t global for referencing it everywhere
t = sym.symbols('t')
u = sym.symbols('u')
v = sym.symbols('v')
x = sym.symbols('x')
y = sym.symbols('y')
z = sym.symbols('z')
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
    #has the option for unit vector notation
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
        new_vect.z = self._z - other._z
        return new_vect

    #dot product, returns scalar value
    def dotProduct(self,other):
        return self._x*other._x + self._y*other._y + self._z*other._z

    #vector cross product, returns a vector
    def crossProduct(self, other):
        new_vect = Vector()
        new_vect._x = self._y * other._z - self._z * other._y
        new_vect._y = self._z * other._x - self._x * other._z
        new_vect._z = self._x * other._y - self._y * other._x
        return new_vect

    #checks if two vectors are orthogonal if the dot product of
    #two vectors is 0, returns boolean
    def isOrthogonal(self,other):
        if Vector.dotProduct(self,other) == 0:
            return True
        return False

    #determines the magnitude of a vector
    def magnitude(self):
        return sym.simplify(sym.sqrt((self._x)**2 + (self._y)**2 + (self._z)**2))
        
    #checking if two vectors are parallel by checking if their cross product
    #is equal to the zero vector
    def isParallel(self, other):
        test_vect = Vector.crossProduct(self, other)
        if(test_vect._x == 0 and test_vect._y == 0 and test_vect._z == 0):
            return True
        return False


#vector function subclass that inherits from the vector class
class VectorFunction(Vector):
    def __init__(self,xt=0, yt=0, zt=0):
        super(VectorFunction, self).__init__(xt,yt,zt)

    #differentiate a vector function
    def differentiate(self):
        print(f"D(r(t)) = <D({self._x}),D({self._y}),D({self._z})>")
        Dr = Vector()
        Dr._x = sym.diff(self._x, t)
        Dr._y = sym.diff(self._y, t)
        Dr._z = sym.diff(self._z, t)
        return Dr

    #integrate a vector function
    def integrate(self):
        C = sym.symbols('C')
        print(f"\u222Br(t)dt = <\u222B{self._x}dt,\u222B{self._y}dt,\u222B{self._z}dt>")
        R = Vector()
        R._x = sym.integrate(self._x,t) + C
        R._y = sym.integrate(self._y,t) + C
        R._z = sym.integrate(self._z,t) + C
        return R

    #calculates arclength of a curve on [a,b] parameterized by r(t)
    def arcLength(self, a, b):
        return sym.integrate(Vector.magnitude(self),(t, a, b))

    def plotCurve(self):
        if self._z == 0:
            sym.plot_parametric((self._x,self._y), (t,-5,5))
        else:
            plot3d_parametric_line(self._x, self._y,self._z, (t, -5, 5))

#parametric surface 
class ParametricSurface(Vector):
    def __init__(self,xuv=0,yuv=0,zuv=0):
        super(ParametricSurface, self).__init__(xuv,yuv,zuv)


    def differentiate(self, var):
        print(f"D{var}(r(u,v)) = <D{var}({self._x}),D{var}({self._y}),D{var}({self._z})>")
        Dr = Vector()
        Dr._x = sym.diff(self._x, var)
        Dr._y = sym.diff(self._y, var)
        Dr._z = sym.diff(self._z, var)
        return Dr

    def integrate(self, var):
        C = sym.symbols('C')
        print(f"\u222Br(u,v)d{var} = <\u222B{self._x}d{var},\u222B{self._y}d{var},\u222B{self._z}d{var}>")
        R = Vector()
        R._x = sym.integrate(self._x,var) + C
        R._y = sym.integrate(self._y,var) + C
        R._z = sym.integrate(self._z,var) + C
        return R

    def surfaceArea(self, a, b, c, d):
        r_u = ParametricSurface.differentiate(self, u)
        r_v = ParametricSurface.differentiate(self, v)
        jac = Vector.magnitude(Vector.crossProduct(r_u,r_v))
        return sym.integrate(jac, (u, a, b), (v, c, d))

    def plotSurface(self):
        plot3d_parametric_surface(self._x,self._y,self._z,(u,-5,5),(v,-5,5))

class VectorField(Vector):
    def __init__(self,p=0,q=0,r=0):
        super(VectorField, self).__init__(p,q,r)

    def divergence(self):
        return sym.diff(self._x,x)+sym.diff(self._y,y)+sym.diff(self._z,z)

    #compute the curl of a vector field
    #due to limitations of sympy, you can't really
    #do the built in curl if there is one for use with my vector class
    def curl(self):
        curl_F = VectorField()
        curl_F._x = sym.diff(self._z,y) - sym.diff(self._y,z)
        curl_F._y = sym.diff(self._x,z) -  sym.diff(self._z,x)
        curl_F._z = sym.diff(self._y,x) - sym.diff(self._x,y)
        return curl_F

    #use curl to determine if a vector field is conservative
    #the curl of a conservative vector field is the zero vector
    def isConservative(self):
        curl_F = VectorField.curl(self)
        if curl_F._x == 0 and curl_F._y == 0 and curl_F._z == 0:
            return True
        return False

    #find a function f such that (gradient)*f = F
    def findFunction(self):
        C = sym.symbols("C")
        if VectorField.isConservative(self):
            fx = sym.integrate(self._x, x)
            fy = sym.integrate(self._y, y)
            fz = sym.integrate(self._z, z)
            return fx + fy + fz + C
        return "Not conservative"

    #work in progress
    #in its current state, it's extremely ineffecient and has it's own set of prpblems
    #need to find a better way to do this
    def composition(self,other):
        VF = VectorField(self._x, self._y, self._z)
         #composing r(t) at P
         #going to find a better way to do this
         #hopefully :)
        if type(self._x) != int:
            if sym.compose(self._x,other._x) != 0:
                VF._x = sym.compose(VF._x, other._x)
            if sym.compose(self._x,other._y) != 0:
                VF._x = sym.compose(VF._x, other._y)
            if sym.compose(self._x,other._z) != 0:
                VF._x = sym.compose(VF._x, other._z)
        #composing r(t) at Q
        if type(self._y) != int:
            if sym.compose(self._y,other._x) != 0:
                VF._y = sym.compose(VF._y, other._x)
            if sym.compose(self._y,other._y) != 0:
                VF._y = sym.compose(VF._y, other._y)
            if sym.compose(self._y,other._z) != 0:
                VF._y = sym.compose(VF._y, other._z)
        #composing r(t) at R
        if type(self._z) != int:
            if sym.compose(self._z,other._x) != 0:
                VF._z = sym.compose(VF._z, other._x)
            if sym.compose(self._z,other._y) != 0:
                VF._z = sym.compose(VF._z, other._y)
            if sym.compose(self._z,other._z) != 0:
                VF._z = sym.compose(VF._z, other._z)
        return VF

    #work in progress
    def workLineIntegral(self, other,a,b):
        return sym.integrate(Vector.dotProduct(
            VectorField.composition(self,other), VectorFunction.differentiate(other)),(t,a,b))
