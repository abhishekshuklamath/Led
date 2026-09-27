# Verify Witt-vector addition and wp formulas (3),(4) of the paper for p=2, n=3 via ghost components,
# and compute Phi_2(s0,s1,u,w1).
from sympy import symbols, expand, Poly, GF, simplify, factor
a0,a1,a2,b0,b1,b2 = symbols('a0 a1 a2 b0 b1 b2')
p=2
def ghost(x):
    return [x[0], x[0]**2+2*x[1], x[0]**4+2*x[1]**2+4*x[2]]
def unghost(w):
    # solve for Witt coordinates over Z[...] (polynomial division exact)
    x0 = w[0]
    x1 = expand((w[1]-x0**2)/2)
    x2 = expand((w[2]-x0**4-2*x1**2)/4)
    return [x0,x1,x2]
def add(x,y):
    gx,gy=ghost(x),ghost(y)
    return unghost([expand(gx[i]+gy[i]) for i in range(3)])
def mod2(e):
    return Poly(expand(e), *sorted(e.free_symbols,key=str), modulus=2).as_expr()
S = add([a0,a1,a2],[b0,b1,b2])
for i,c in enumerate(S):
    print("sum coordinate",i,":", mod2(c))
# Frobenius F(x) = (x_i^2), wp = F - id ; subtraction: x - y = x + (-y), -y computed via ghost
def neg(x):
    return unghost([-g for g in ghost(x)])
def sub(x,y): return add(x,neg(y))
P = sub([a0**2,a1**2,a2**2],[a0,a1,a2])
for i,c in enumerate(P):
    print("wp coordinate",i,":", mod2(c))
# Phi_2: s + wp(u,w1,w2), coordinate 2, minus (w2^2+w2), with (s+wp h)_1 = 0 imposed? No: Phi_2 is defined
# as the coordinate-2 polynomial with (s+wp h)_2 = w2^2 + w2 + eQ, eQ = s2 + Phi_2(s0,s1,u,w1).
s0,s1,s2,u,w1,w2 = symbols('s0 s1 s2 u w1 w2')
h=[u,w1,w2]
T = add([s0,s1,s2], P.__class__([mod2(c) for c in sub([u**2,w1**2,w2**2],[u,w1,w2])]))
T = [mod2(c) for c in T]
print("coord0:",T[0]); print("coord1:",T[1])
Phi2 = mod2(T[2] - w2**2 - w2 - s2)
print("Phi2 =",Phi2)
print("Phi2 depends on w2?", w2 in Phi2.free_symbols)
import pickle
pickle.dump({'coord1':T[1],'Phi2':Phi2}, open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/phi2.pkl','wb'))
