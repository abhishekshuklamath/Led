# Cross-check: x2' (from the Witt trace of [t]) versus Tr_{K(u)/K}(e_Q), e_Q = s2 + Phi2(s0,s1,u,alpha u+beta),
# and the symmetry beta -> beta+1.
from sympy import symbols, expand, Poly, S
import pickle
exec(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/wittlib.py').read())
s0,s1,s2,u,w1,al,be = symbols('s0 s1 s2 u w1 alpha beta')
Phi2 = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/phi2.pkl','rb'))['Phi2']
x2p = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/x2p.pkl','rb'))
A,B,C = 1+s0+al**2, s0+al, s1+be**2+be
# power sums of the roots of u^3+Au^2+Bu+C over Z (e1=-A,e2=B,e3=-C), reduce mod 2 at the end
e1,e2,e3 = -A,B,-C
P=[S(3), e1, expand(e1*e1-2*e2)]
P.append(expand(e1*P[2]-e2*P[1]+3*e3))
for k in range(4,12): P.append(expand(e1*P[k-1]-e2*P[k-2]+e3*P[k-3]))
def trace_poly_in_u(expr):
    poly = Poly(expand(expr), u)
    return mod2(sum(c*P[m] for (m,),c in poly.terms()))
eQ = s2 + Phi2.subs(w1, al*u+be)
TreQ = trace_poly_in_u(eQ)
diff = mod2(TreQ - x2p)
print("Tr(e_Q) - x2' =", diff)
y = wp_inverse_poly(diff)
print("  is wp of:", y)
# symmetry beta -> beta+1
d2 = mod2(x2p.subs(be, be+1) - x2p)
print("x2'(beta+1)-x2'(beta) =", d2, " wp-inverse:", wp_inverse_poly(d2))
# symmetry u -> u+1 (translation by 1 = (1,0,0)): h+1 = (u+1, w1+u, w2 + u w1 + u^3 + u)... line w1' = w1 + u = (alpha+1)u + beta, in coordinate u'=u+1: w1' = (alpha+1)(u'+1)+beta = (alpha+1)u' + (alpha+1+beta)
d3 = mod2(x2p.subs({al:al+1, be:al+1+be}) - x2p)
print("x2'(g.line)-x2'(line) =", d3, " wp-inverse:", wp_inverse_poly(d3))
