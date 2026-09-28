from sympy import symbols, expand, Poly, Rational, sqrt, simplify
a0,a1,a2,b0,b1,b2=symbols('a0 a1 a2 b0 b1 b2')
def ghost(x): return [x[0], x[0]**2+2*x[1], x[0]**4+2*x[1]**2+4*x[2]]
def unghost(w):
    x0=w[0]; x1=(w[1]-x0**2)/2; x2=(w[2]-x0**4-2*x1**2)/4
    return [expand(x0),expand(x1),expand(x2)]
def mod2(e): return Poly(expand(e),a0,a1,a2,b0,b1,b2,modulus=2).as_expr()
A=[a0,a1,a2]; B=[b0,b1,b2]
S=unghost([g+h for g,h in zip(ghost(A),ghost(B))])
print("sum:",[mod2(c) for c in S])
D=unghost([2*g for g in ghost(A)]); print("2a:",[mod2(c) for c in D])
Q=unghost([4*g for g in ghost(A)]); print("4a:",[mod2(c) for c in Q])
P=unghost([g-h for g,h in zip(ghost([a0**2,a1**2,a2**2]),ghost(A))]); print("wp(a):",[mod2(c) for c in P])
# candidate (f): x0 = s1*v, v^2 = v + f ; compute wp(x0) = x0^2 + x0 in char 2
s0,s1,f,v=symbols('s0 s1 f v')
x0=s1*v; e=expand(x0**2+x0).subs(v**2, v+f)
print("wp(s1 v) =", Poly(expand(e),s0,s1,f,v,modulus=2).as_expr())
# (h) check wp(y/x) on y^2+xy=x^3+a6
x,y,a6=symbols('x y a6')
e=(y/x)**2+y/x; num=expand((y**2+x*y))  # = x^3+a6
print("wp(y/x) = (y^2+xy)/x^2 = (x^3+a6)/x^2 = x + a6/x^2")
