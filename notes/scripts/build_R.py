# Export x2' as a list of terms (exponents of s0,s1,alpha,beta, s2) for the fast evaluator.
import pickle
from sympy import symbols, Poly
s0,s1,s2,al,be = symbols('s0 s1 s2 alpha beta')
x2p = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/x2p.pkl','rb'))
P = Poly(x2p, s0,s1,s2,al,be)
terms = [m for m,c in P.terms() if c%2==1]
pickle.dump(terms, open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/x2p_terms.pkl','wb'))
print(len(terms), "terms; max alpha deg", max(m[3] for m in terms), "max beta deg", max(m[4] for m in terms))
