# Quadratic resolvent class (char 2) of X^3 + A X^2 + B X + C, and reduced form of R modulo squares.
from sympy import symbols, expand, Poly, S, factor, div, symmetrize
import pickle
exec(open('wittlib.py').read())
r1,r2,r3,A,B,C = symbols('r1 r2 r3 A B C')
P = r1**2*r2 + r2**2*r3 + r3**2*r1
Q = r1*r2**2 + r2*r3**2 + r3*r1**2
e1,e2,e3 = r1+r2+r3, r1*r2+r2*r3+r3*r1, r1*r2*r3
# express P+Q and PQ in e's (over Z), then reduce mod 2 with e1=A, e2=B, e3=C
sym1 = symmetrize(expand(P+Q), formal=True); sym2 = symmetrize(expand(P*Q), formal=True)
print("P+Q =", sym1[0], " rem", sym1[1]); print("PQ =", sym2[0], " rem", sym2[1])
subs = {sym1[2][0][0]:A, sym1[2][1][0]:B, sym1[2][2][0]:C}
D = mod2(sym1[0].subs(subs)); N = mod2(sym2[0].subs(subs))
print("D = P+Q mod 2 =", D); print("N = PQ mod 2 =", N)
# f = N / D^2 ; try to write N = D^2 * q + D * r1 + r0 ... we look for f == polynomial mod wp:  f + wp(g/D) = (N + g^2 + g D)/D^2
q,r = div(Poly(N,A,B,C), Poly(D,A,B,C))
print("N mod D:", r.as_expr(), " quotient:", q.as_expr())
pickle.dump({'D':D,'N':N}, open('resolvent.pkl','wb'))
