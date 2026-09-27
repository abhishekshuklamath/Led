# Corestriction (Witt trace) necessary condition for a cubic witness at (p,n)=(2,3).
# F' = K(u), u^3 + A u^2 + B u + C = 0, t = s0 + u^2 + u.  Over the Galois closure M of F'/K,
# s = [t] = [t'] = [t''] mod wp, so 3 s = Tr[t] := [t]+[t']+[t'']  mod (wp W_3(M)), and the
# difference 3s - Tr[t] lies in ker(res_{M/K}) = Hom(Gal(M/K),Z/8) = {0} or Z/2.
# Here we (1) verify Tr[t] = (e1, e2, e1 e3 + e1^2 e2) for the elementary symmetric functions,
# (2) verify 3x = (x0, x1 + x0^2, x2 + x1^2 + x0^2 x1),
# (3) compute the reduced obstruction class x2' in terms of (s0,s1,s2,A,B,C) [equivalently (alpha,beta)].
from sympy import symbols, expand, Poly, together, cancel, factor, simplify, S
import pickle
def mod2(e):
    e = expand(e)
    fs = sorted(e.free_symbols, key=str)
    if not fs: return S(int(e) % 2)
    return Poly(e, *fs, modulus=2).as_expr()
def wadd(a,b):
    a0,a1,a2=a; b0,b1,b2=b
    return [mod2(a0+b0), mod2(a1+b1+a0*b0), mod2(a2+b2+a1*b1+a0*b0*(a1+b1)+a0**3*b0+a0*b0**3)]
def wp(a):
    a0,a1,a2=a
    C = a0**7+a0**4+a0**3*a1**2+a0**3*a1+a0**2*a1**2+a0**2*a1+a1**3+a1**2
    return [mod2(a0**2+a0), mod2(a1**2+a1+a0**3+a0**2), mod2(a2**2+a2+C)]
# (1)
t1,t2,t3 = symbols('t1 t2 t3')
Tr = wadd(wadd([t1,0,0],[t2,0,0]),[t3,0,0])
e1 = t1+t2+t3; e2 = t1*t2+t1*t3+t2*t3; e3 = t1*t2*t3
print("Tr[t] - (e1,e2,e1e3+e1^2e2):", [mod2(Tr[i]-x) for i,x in enumerate([e1,e2,e1*e3+e1**2*e2])])
# also check Tr[t] is symmetric under all permutations => in W_3(K); and check independence of the addition order
# (2)
x0,x1,x2=symbols('x0 x1 x2')
three = wadd(wadd([x0,x1,x2],[x0,x1,x2]),[x0,x1,x2])
print("3x =", three)
# (3) the obstruction.  u^3 + A u^2 + B u + C = 0; t = s0 + u^2 + u.
s0,s1,s2,A,B,C,u = symbols('s0 s1 s2 A B C u')
# power sums of u: Newton over Z then mod 2 (all identities are integral)
# elementary symmetric of roots u_i: E1 = -A, E2 = B, E3 = -C  (signs irrelevant mod 2)
E1,E2,E3 = A,B,C
def power_sums(E1,E2,E3,N):
    p=[3, E1]  # p0=3, p1=e1 (mod 2 signs irrelevant but we keep exact Newton with signs e1=-A etc.)
    # Use exact Newton with e1=-A,e2=B,e3=-C over Z
    e1,e2,e3 = -A,B,-C
    p=[S(3), e1]
    p.append(e1*p[1]-2*e2)
    p.append(e1*p[2]-e2*p[1]+3*e3)
    for k in range(4,N+1):
        p.append(expand(e1*p[k-1]-e2*p[k-2]+e3*p[k-3]))
    return [expand(x) for x in p]
P = power_sums(E1,E2,E3,8)
# elementary symmetric functions of t_i = s0 + u_i^2 + u_i  (over Z, then reduce mod 2)
# Use: e1(t) = sum t_i ; e2(t) = ((sum t_i)^2 - sum t_i^2)/2 ; e3(t) = (p1^3 - 3 p1 p2 + 2 p3)/6 with p_k = sum t_i^k
def psum_t(k):
    # sum_i (s0 + u_i^2 + u_i)^k expanded via multinomial in u_i: use polynomial in u then replace u^m -> P[m]
    expr = expand((s0+u**2+u)**k)
    poly = Poly(expr, u)
    tot = 0
    for (m,),c in poly.terms():
        tot += c*P[m]
    return expand(tot)
q1,q2,q3 = psum_t(1),psum_t(2),psum_t(3)
f1 = q1
f2 = expand((q1**2-q2)/2)
f3 = expand((q1**3-3*q1*q2+2*q3)/6)
f1,f2,f3 = mod2(f1),mod2(f2),mod2(f3)
print("e1(t) =",f1); print("e2(t) =",f2); print("e3(t) =",f3)
TrT = [f1, f2, mod2(f1*f3+f1**2*f2)]
threeS = wadd(wadd([s0,s1,s2],[s0,s1,s2]),[s0,s1,s2])
# d = 3s - Tr[t]  (subtraction: a - b = a + (-b); -b in char 2 W_3: compute via  -b = (b0, b1+b0^2, ...)?  Simply solve a = d + Tr numerically:
# better: compute negation from ghost components mod 2: -x has ghost (-w0,-w1,-w2). Use the formula from witt_check: we recompute:
def wneg(b):
    # -(b0,b1,b2) in W_3 of an F_2-algebra: (b0, b1 + b0^2, b2 + b1^2 + b0^2 b1 ... ) — verify below by checking b + neg(b) = 0
    c0 = b[0]
    # solve (b + c) = 0 coordinate by coordinate
    c1 = mod2(b[1] + b[0]*c0)          # (b+c)_1 = b1 + c1 + b0 c0 = 0
    c2 = mod2(b[2] + b[1]*c1 + b[0]*c0*(b[1]+c1) + b[0]**3*c0 + b[0]*c0**3)
    return [c0,c1,c2]
assert all(x==0 for x in wadd([x0,x1,x2],wneg([x0,x1,x2])))
d = wadd(threeS, wneg(TrT))
print("d0 =", d[0], "   (should be wp(A) = A^2 + A)")
assert mod2(d[0]-(A**2+A))==0
# subtract wp[A]:
d = wadd(d, wneg(wp([A,0,0])))
assert d[0]==0
print("x1 =", d[1])
pickle.dump({'d':d,'f1':f1,'f2':f2,'f3':f3}, open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/cores_d.pkl','wb'))
