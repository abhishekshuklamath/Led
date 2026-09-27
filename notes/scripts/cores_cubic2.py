# Continue: substitute A=1+s0+alpha^2, B=s0+alpha, C=s1+beta^2+beta; show x1 in wp K, and compute the final obstruction x2'.
from sympy import symbols, expand, Poly, S, factor
import pickle
exec(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/wittlib.py').read())
dd = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/cores_d.pkl','rb'))
s0,s1,s2,A,B,C,al,be = symbols('s0 s1 s2 A B C alpha beta')
sub = {A:1+s0+al**2, B:s0+al, C:s1+be**2+be}
d = [mod2(x.subs(sub)) for x in dd['d']]
print("x1(alpha,beta) =", d[1])
# find y1 with y1^2+y1 = x1 by the monomial-chain algorithm (polynomial case)
y1 = wp_inverse_poly(d[1])
print("y1 =", y1)
assert mod2(y1**2+y1-d[1])==0
# subtract wp(V[y1]) = wp(0,y1,0)
d2 = wadd(d, wneg(wp([0,y1,0])))
assert d2[0]==0 and d2[1]==0
x2p = d2[2]
print("x2' =", x2p)
print("number of terms:", len(Poly(x2p, s0,s1,s2,al,be).terms()))
pickle.dump(x2p, open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/x2p.pkl','wb'))
