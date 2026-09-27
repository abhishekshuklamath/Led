from sympy import symbols, expand, Poly, S, sqrt
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
def wneg(b):
    c0 = b[0]
    c1 = mod2(b[1] + b[0]*c0)
    c2 = mod2(b[2] + b[1]*c1 + b[0]*c0*(b[1]+c1) + b[0]**3*c0 + b[0]*c0**3)
    return [c0,c1,c2]
def wp_inverse_poly(x):
    """Given a polynomial x over F_2 (coefficients 0/1, symbols algebraically independent), return y with y^2+y = x,
    or None if x not in wp(F_2[symbols]).  (Constant term: y_const^2+y_const=c solvable over alg. closed k; we
    ignore the constant term, i.e. work modulo k.)  Algorithm: process monomials from highest total degree down:
    a monomial m with coefficient 1: if m is a square m=m'^2, put m' into y (y^2 contributes m, y contributes m');
    else put m into y (y contributes m, y^2 contributes m^2 which has higher degree and must have been handled) -> failure.
    Correct procedure: chains. We do it via repeated subtraction from the top."""
    x = mod2(x)
    syms = sorted(x.free_symbols, key=str)
    if not syms: return S(0)
    P = Poly(x, *syms, modulus=2)
    y = S(0)
    while True:
        P = Poly(mod2(P.as_expr()), *syms, modulus=2)
        terms = [m for m,c in P.terms() if c%2==1 and sum(m)>0]
        if not terms: return mod2(y)
        m = max(terms, key=lambda m:(sum(m),m))
        if all(e%2==0 for e in m):
            mono = S(1)
            for s,e in zip(syms,m): mono *= s**(e//2)
        else:
            return None  # a top monomial that is not a square: x not in wp (since y^2 top monomial must cancel it)
        y += mono
        P = Poly(mod2(P.as_expr() + mono**2 + mono), *syms, modulus=2)
