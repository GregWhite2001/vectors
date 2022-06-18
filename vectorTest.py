from vector import Vector
import sympy as sym

##################### MAIN ######################
t = sym.symbols('t')

print("------------------Constant Vectors---------------")
vect = Vector(1,1,1)
vect2= Vector(1,2,3.5)

print("------------------Vector Addition---------------")
vect3 = Vector.addVector(vect,vect2)

print(vect)
print(vect3)
print(Vector.dotProduct(vect,vect2))
print(Vector.isOrthogonal(vect,vect2))

vect4 = Vector(1,0,1)
vect5 = Vector(1,0,-1)

print(Vector.isOrthogonal(vect4,vect2))
vect6 = Vector.crossProduct(vect4,vect2)

print(vect6)
print(Vector.magnitude(vect6))
print(Vector.isParallel(vect4,vect5))

print(Vector.magnitude(vect6))
#print(Vector.crossProductMagnitude(vect4,vect3))
print(vect2)
print(Vector.magnitude(vect2))

print("------------------Vector Functions---------------")
x=sym.Function('x')
y=sym.Function('y')
z=sym.Function('z')
r1 = Vector(x(t),y(t),z(t))
print(r1)
r2 = Vector(sym.ln(t), sym.exp(t), sym.tan(t))
r3 = Vector(2*t**2,1,0)
print(r2)
print(r3)

print("------------------Differentiating Vector Functions---------------")
dr = Vector.differentiate(r2)
print("r'(t) =" + str(dr))
print("r'(t) = "  + str(Vector.differentiate(Vector(sym.cos(t), sym.exp(t), t))))
print("r'(t) = " + str(Vector.differentiate(Vector(t*sym.cos(t), sym.exp(t)/t, t))))

print("------------------Integrating Vector Functions---------------")
print("R(t) = " + str(Vector.integrate(Vector(t, 1, 3*t**2))))
print(Vector.magnitude(dr))
print(Vector.arcLength(dr, 0, 1))
#print('\u222B')
#print(type(vect2.z))
#s= sym.Integral(Vector.magnitude(dr))
#s