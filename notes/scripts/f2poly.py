# Fast polynomials over F_2 in variables (s0,s1,s2): a polynomial is a frozenset of exponent tuples.
import itertools
def padd(a,b): return a ^ b
def pmul(a,b):
    out=set()
    for ea in a:
        for eb in b:
            m=(ea[0]+eb[0],ea[1]+eb[1],ea[2]+eb[2])
            if m in out: out.remove(m)
            else: out.add(m)
    return frozenset(out)
def psq(a): return frozenset((2*e[0],2*e[1],2*e[2]) for e in a)
def ppow(a,n):
    r=frozenset([(0,0,0)]); base=a
    while n:
        if n&1: r=pmul(r,base)
        base=psq(base); n>>=1
    return r
ONE=frozenset([(0,0,0)]); ZERO=frozenset()
def mono(i,j,l): return frozenset([(i,j,l)])
S0,S1,S2 = mono(1,0,0),mono(0,1,0),mono(0,0,1)
def in_wp(x):
    """x in wp(k[s0,s1,s2]) modulo constants?  Monomial chain test; returns (bool, y) with y^2+y = x + const."""
    x=set(e for e in x if sum(e)>0)
    y=set()
    while x:
        m=max(x, key=lambda e:(sum(e),e))
        if any(v%2 for v in m): return False,None
        h=(m[0]//2,m[1]//2,m[2]//2)
        y ^= {h}
        x ^= {m, h}
        x.discard((0,0,0))
    return True, frozenset(y)
def show(p):
    if not p: return "0"
    return " + ".join("s0^%d s1^%d s2^%d"%e for e in sorted(p,reverse=True))
