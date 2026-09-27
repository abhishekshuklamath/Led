# (a) Artin-Schreier reduction of C(y0,y1) on E_0: y1^2 = y1 + y0^3 + y0^2  (char 2), pole orders v(y0)=-2, v(y1)=-3.
from sympy import symbols, Poly, expand, S
exec(open('wittlib.py').read())
y0,y1=symbols('y0 y1')
C = y0**7+y0**4+y0**3*y1**2+y0**3*y1+y0**2*y1**2+y0**2*y1+y1**3+y1**2
def reduce_E0(e):  # reduce y1-degree to <=1 using y1^2 = y1 + y0^3 + y0^2
    e=mod2(e); 
    while Poly(e,y1).degree()>1:
        p=Poly(e,y1); new=0
        for (d,),c in p.terms():
            if d>=2: new += c*y1**(d-2)*(y1+y0**3+y0**2)
            else: new += c*y1**d
        e=mod2(new)
    return e
Cr=reduce_E0(C); print("C on E_0 =",Cr)
Cr2=reduce_E0(Cr + (y0**2*y1)**2 + y0**2*y1); print("C + wp(y0^2 y1) =",Cr2)
def poleorder(e):
    return max(2*i+3*j for (i,j),c in Poly(e,y0,y1).terms())
print("pole order (E_0 valuation):",poleorder(Cr2))
# (b) breaks and genus for general (p,n)
def data(p,n):
    l=[1]
    for i in range(1,n): l.append(l[-1]+(p-1)*p**(2*i-1))
    lp=[-1]+l
    twog2=-2*p**n+sum((p**(n-i+1)-1)*(lp[i]-lp[i-1]) for i in range(1,n+1))
    return l,(twog2+2)//2
for p,n in [(2,2),(3,2),(5,2),(2,3),(2,4),(3,3)]:
    print((p,n),"lower breaks",data(p,n)[0],"genus",data(p,n)[1])
