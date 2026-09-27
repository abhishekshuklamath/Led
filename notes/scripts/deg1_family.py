# alpha = a0 + a1 s2, beta = b0 + b1 s2 with a_i,b_i in K_2 = k(s0,s1) (symbolic).  Coefficients c_i of s2^i in s2 + R.
from sympy import symbols, Poly, expand, factor, S
import pickle, sys
exec(open('wittlib.py').read())
s0,s1,s2,al,be,a0,a1,b0,b1 = symbols('s0 s1 s2 alpha beta a0 a1 b0 b1')
x2p = pickle.load(open('x2p.pkl','rb'))
E = mod2(x2p.subs({al:a0+a1*s2, be:b0+b1*s2}))
P = Poly(E, s2)
c = {i:mod2(P.coeff_monomial(s2**i)) for i in range(17)}
for i in range(17):
    print(f"c_{i} =", c[i])
pickle.dump(c, open('deg1_coeffs.pkl','wb'))
