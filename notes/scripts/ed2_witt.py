# W_3 arithmetic for p=2 via ghost components; negation; s - wp(x); Theorem 6.2 family check.
from sympy import symbols, expand, Poly, GF
def ghost(x): return [x[0], x[0]**2+2*x[1], x[0]**4+2*x[1]**2+4*x[2]]
def unghost(w):
    x0=w[0]; x1=expand((w[1]-x0**2)/2); x2=expand((w[2]-x0**4-2*x1**2)/4); return [x0,x1,x2]
def add(x,y): return unghost([expand(a+b) for a,b in zip(ghost(x),ghost(y))])
def neg(x): return unghost([-g for g in ghost(x)])
def sub(x,y): return add(x,neg(y))
def mod2(e):
    e=expand(e)
    if e==0: return e
    return Poly(e,*sorted(e.free_symbols,key=str),modulus=2).as_expr()
def wp(x): return [mod2(c) for c in sub([c**2 for c in x],x)]
a0,a1,a2=symbols('a0 a1 a2')
print("-(a0,a1,a2) =",[mod2(c) for c in neg([a0,a1,a2])])
# check: a + (-a) = 0 mod 2
z=add([a0,a1,a2],[mod2(c) for c in neg([a0,a1,a2])]); print("a+(-a) mod 2 =",[mod2(c) for c in z])
s0,s1,s2,x0,x1,x2=symbols('s0 s1 s2 x0 x1 x2')
s=[s0,s1,s2]; P=wp([x0,x1,x2])
D=[mod2(c) for c in sub(s,P)]; S=[mod2(c) for c in add(s,P)]
print("s - wp(x):"); [print("  ",i,":",c) for i,c in enumerate(D)]
print("s + wp(x):"); [print("  ",i,":",c) for i,c in enumerate(S)]
print("(s-wp x)_1 - (s+wp x)_1 =", mod2(D[1]-S[1]))
print("(s-wp x)_2 - (s+wp x)_2 =", mod2(D[2]-S[2]))
# Level 2: is (s - wp(c,x1))_1 == c(c+1)(c+s0)+s1 mod wp K ?  Compare with x0=c.
c=symbols('c')
D1=D[1].subs(x0,c)
diff=mod2(D1 - (c*(c+1)*(c+s0)+s1))
print("(s-wp(c,x1))_1 + c(c+1)(c+s0)+s1 =",diff, " [should be x1^2+x1 or of form h^2+h]")
S1=S[1].subs(x0,c)
print("(s+wp(c,x1))_1 + c(c+1)(c+s0)+s1 =",mod2(S1-(c*(c+1)*(c+s0)+s1)))
