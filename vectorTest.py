#from numpy import gradient
from vector import ParametricSurface, Vector, VectorField, VectorFunction
import sympy as sym

##################### MAIN ######################
sym.init_printing(use_unicode=True)
t = sym.symbols('t')
u = sym.symbols('u')
v = sym.symbols('v')


print("------------------Constant Vectors---------------")
vect1 = Vector(1,1,1)
vect2 = Vector(1,2,3.5)
print(f"Here is a constant vector: vect1: {str(vect1)}")
print(f"Here is another constant vector: vect2: {str(vect2)}")

print("------------------Vector Addition---------------")
vect3 = Vector.addVector(vect1,vect2)
print(f"vect1 + vect2 = {str(vect1)} + {str(vect2)} = {str(vect3)}")
vect4 = Vector(1,0,1)
vect5 = Vector(1,0,-1)

print("------------------Vector Subtraction---------------")
print(f"vect4 - vect5 = {str(vect4)} - {str(vect5)} = {str(Vector.subtractVector(vect4,vect5))}")
print(f"vect5 - vect4 = {str(vect5)} - {str(vect4)} = {str(Vector.subtractVector(vect5,vect4))}")
print("------------------Dot Product---------------")
print(f"vect \u2022 vect2 = {Vector.dotProduct(vect1,vect2)}")
print(f"The vectors vect4 and vect2 are orthogonal. ({Vector.isOrthogonal(vect4,vect2)})")
print(f"The vectors vect and vect2 are orthogonal. ({Vector.isOrthogonal(vect1,vect2)})")

print("-----------------Cross Product---------------")
vect6 = Vector.crossProduct(vect4,vect2)
print(f"vect4 \u00D7 vect2 = {str(vect6)}")
print(f"The magnitude of the cross product of vect4 and vect2 is:{Vector.magnitude(vect6)}")
print(f"The vectors and vect4 and vect5 are parallel. ({Vector.isParallel(vect4,vect5)})")
print(f"The magnitude of vect6 is: {str(Vector.magnitude(vect6))}")
print(f"vect2 = {str(vect2)}")
print(f"The magnitude of vect2 is: {str(Vector.magnitude(vect2))}")

print("------------------Vector Functions---------------")
x=sym.Function('x')
y=sym.Function('y')
z=sym.Function('z')
r1 = VectorFunction(x(t),y(t),z(t))
print(f"r(t) = {str(r1)}")
r2 = VectorFunction(sym.ln(t), sym.exp(t), sym.tan(t))
r3 = VectorFunction(2*t**2,1,0)
print(f"r(t) = {str(r2)}")
print(f"r(t) = {str(r3)}")

print("------------------Differentiating Vector Functions---------------")
dr = VectorFunction.differentiate(r3)
print(f"r'(t) = {str(dr)}")
print(f"r'(t) = {str(VectorFunction.differentiate(VectorFunction(sym.cos(t), sym.exp(t))))}")
print(f"r'(t) = {str(VectorFunction.differentiate(VectorFunction(t*sym.cos(t), sym.exp(t)/t, t)))}")

print("------------------Integrating Vector Functions---------------")
print(f"R(t) = {str(VectorFunction.integrate(VectorFunction(t, 1, 3*t**2)))}")
print(Vector.magnitude(dr))
print(f"Arclength (\u222B_c ds), S, on interval [0,1] of C: r(t) = {str(r3)}: S = {VectorFunction.arcLength(dr, 0, 1)}")

print("------------------Vector Fields---------------")
#TODO
x = sym.symbols('x')
y = sym.symbols('y')
z = sym.symbols('z')

VF1 = VectorField(x*y,x**2*z,y*z)
print(VF1)
print(VectorField.divergence(VF1))
print(VectorField.curl(VF1))
VF2 = VectorField(2*x,2*y,2*z)
print(VectorField.findFunction(VF2))
print("------------------Parametric Surfaces---------------")
rs1 = ParametricSurface(u, v, u+v)
print(f"Parametric surface r(u,v) = {str(rs1)}")
rs1_u = ParametricSurface.differentiate(rs1, u)
print(f"Partial derivative of r(u,v) with respect to u: r_u = {str(rs1_u)}")
rs1_v = ParametricSurface.differentiate(rs1,v)
print(f"Partial derivative of r(u,v) with respect to v: r_v = {str(rs1_v)}")
print(f"The cross product of r_u \u00D7 r_v = {Vector.crossProduct(rs1_u,rs1_v)}")
print(f"The surface area (\u222C_s dS), of the surface S parameterized by r(u,v) = rs1 over the rectangular region [0,1] \u00D7 [0,1] : {ParametricSurface.surfaceArea(rs1,0,1,0,1)}")
print(f"Ru(u,v) = {ParametricSurface.integrate(rs1,u)}")
print(f"Rv(u,v) = {ParametricSurface.integrate(rs1,v)}")