# Finite-field specialisation test for  e_Q in wp(K(u)).
# Specialise (s0,s1,s2) -> F_8^3 (inside F_512 = F_8^3), find the roots u of the specialised cubic in F_512,
# and compute the absolute trace of e_Q(u) to F_2.  If e_Q = x^2 + x in K(u), the trace vanishes at every
# specialisation point where x is regular (all but a proper closed subset), so a failure rate near 1/2 disproves membership.
import random, itertools
M=9; POLY=(1<<9)|(1<<4)|1   # x^9+x^4+1 irreducible over F_2
def gmul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a>>M: a^=POLY
    return r
def gpow(a,n):
    r=1
    while n:
        if n&1: r=gmul(r,a)
        a=gmul(a,a); n>>=1
    return r
def tr(a):  # absolute trace F_512 -> F_2
    t=0; x=a
    for i in range(M):
        t^=x; x=gmul(x,x)
    return t
F8=[x for x in range(512) if gpow(x,8)==x]
assert len(F8)==8
def evalpoly(terms, vals):
    """terms: iterable of exponent tuples (over F_2) in variables vals (list of field elements)"""
    r=0
    for e in terms:
        m=1
        for v,k in zip(vals,e):
            if k: m=gmul(m,gpow(v,k))
        r^=m
    return r
import pickle
from sympy import symbols, Poly
s0,s1,s2,u,w1 = symbols('s0 s1 s2 u w1')
Phi2 = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/phi2.pkl','rb'))['Phi2']
PHI_TERMS=[m for m,c in Poly(Phi2,s0,s1,u,w1).terms() if c%2]
def test_line(alpha_terms, beta_terms, verbose=False, points=None):
    """alpha_terms, beta_terms: sets of exponent tuples in (s0,s1,s2). Returns (#good, #tested)."""
    good=tested=0
    pts = points if points is not None else itertools.product(F8,F8,F8)
    for a0,a1,a2 in pts:
        al=evalpoly(alpha_terms,[a0,a1,a2]); be=evalpoly(beta_terms,[a0,a1,a2])
        A=1^a0^gmul(al,al); B=a0^al; C=a1^gmul(be,be)^be
        roots=[x for x in range(512) if gmul(gmul(x,x),x)^gmul(A,gmul(x,x))^gmul(B,x)^C==0]
        for r in roots:
            w=gmul(al,r)^be
            e=a2^evalpoly(PHI_TERMS,[a0,a1,r,w])
            tested+=1; good+= (tr(e)==0)
    return good,tested
if __name__=="__main__":
    # sanity: e = w1^2+w1 should always pass; use a modified evaluation
    print("line w=0 :", test_line(set(),set()))
    print("line w=s2:", test_line(set(),{(0,0,1)}))
    print("line w=s2 u + s1:", test_line({(0,0,1)},{(0,1,0)}))
