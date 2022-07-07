from vector import Vector, VectorFunction, VectorField, ParametricSurface
#might need this, don't know yet
from cmath import acos
from math import asin, sin, cos
from sympy.plotting import plot3d_parametric_line, plot3d_parametric_surface
import sympy as sym

COMPONENT_FORM = True
sym.init_printing(use_unicode=True)
#making t global for referencing it everywhere
global t
global u
global v
t = sym.symbols('t')
u = sym.symbols('u')
v = sym.symbols('v')
x = sym.symbols('x')
y = sym.symbols('y')
z = sym.symbols('z')

def graphCurve(r):
    if r._z == 0:
        sym.plot_parametric((r._x,r._y), (t,-5,5))
    else:
        plot3d_parametric_line(r._x, r._y,r._z, (t, -5, 5))

def graphSurface(r):
    plot3d_parametric_surface(r._x,r._y,r._z,(u,-5,5),(v,-5,5))



r1 = VectorFunction(sym.cos(t),sym.sin(t),t)
r2 = ParametricSurface(u,v,u+v)
r3 = ParametricSurface(u*sym.cos(v),u*sym.sin(v),u**2,)
graphCurve(r1)
graphSurface(r2)
graphSurface(r3)

