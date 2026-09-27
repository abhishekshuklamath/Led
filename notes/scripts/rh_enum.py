# Enumerate ramification data of faithful Z/2^n-curves C in char 2 (n=2,3) with g(C) <= GMAX,
# via the tower C^(i) = C/<g^{2^i}>, i=0..n (C^(0)=C/G, C^(n)=C). An orbit with inertia of order 2^a
# has lower breaks l_1<...<l_a (odd, l_{j+1}-l_j = 2^j (u_{j+1}-u_j), u_{j+1} >= 2 u_j), and ramifies
# the steps i = n+1-a..n, at 2^{n-a} points of C^(i), each with break l_{a-n+i}.
# Per-step Riemann-Hurwitz: 2g_i-2 = 2(2g_{i-1}-2) + sum(break+1); Deuring-Shafarevich: sigma_i-1 = 2(sigma_{i-1}-1)+#ram.
import itertools, sys
def break_seqs(a, lmax):
    # lower breaks from upper breaks u_1<...<u_a with u_1 odd >=1, u_{j+1} >= 2u_j, u_j integers; l_1=u_1, l_{j+1}=l_j+2^j(u_{j+1}-u_j)
    out=[]
    def rec(us):
        if len(us)==a:
            ls=[us[0]]
            for j in range(1,a): ls.append(ls[-1]+2**j*(us[j]-us[j-1]))
            if ls[-1]<=lmax: out.append((tuple(us),tuple(ls)))
            return
        if not us:
            for u in range(1,lmax+1,2): rec([u])
        else:
            for u in range(2*us[-1], lmax+1): rec(us+[u])
    rec([]); return out
def enumerate_curves(n, GMAX):
    LMAX=2*GMAX+2+16
    orbit_types=[]
    for a in range(1,n+1):
        for us,ls in break_seqs(a,LMAX): orbit_types.append((a,us,ls))
    results=[]
    # bound on number of orbits: each orbit contributes at least ... use g' and multiset of orbits; brute force with up to 4 orbits
    for gq in range(0,GMAX+1):
        for norb in range(0,5):
            for combo in itertools.combinations_with_replacement(range(len(orbit_types)),norb):
                orbs=[orbit_types[c] for c in combo]
                g=[gq]; sig=[gq]  # sigma(C/G) unknown: treat p-rank of quotient as parameter later; here record genus only
                ok=True
                for i in range(1,n+1):
                    contrib=0; r=0
                    for (a,us,ls) in orbs:
                        if i>=n+1-a:
                            npts=2**(n-a); br=ls[a-n+i-1]
                            contrib+=npts*(br+1); r+=npts
                    twog=2*(2*g[-1]-2)+contrib
                    gi=(twog+2)//2
                    if (twog+2)%2 or gi<0 or gi>GMAX: ok=False;break
                    g.append(gi)
                if ok:
                    # p-rank: sigma_n - 1 = 2^n (sigma_0 - 1) + sum over orbits 2^n(1-1/e); need sigma_0<=gq; also stepwise sigma_i>=0
                    for s0 in range(0,gq+1):
                        s=[s0]; ok2=True
                        for i in range(1,n+1):
                            r=sum(2**(n-a) for (a,us,ls) in orbs if i>=n+1-a)
                            si=2*(s[-1]-1)+r+1
                            if si<0 or si>g[i]: ok2=False;break
                            s.append(si)
                        if ok2: results.append((g[-1],gq,s0,s[-1],tuple((a,ls) for (a,us,ls) in orbs),tuple(g),tuple(s)))
    return sorted(set(results))
if __name__=="__main__":
    for n,GMAX in [(2,6),(3,10)]:
        print(f"=== Z/{2**n}-curves, g(C) <= {GMAX} : (g(C), g(C/G), sigma(C/G), sigma(C), orbits (a=log2 inertia, lower breaks), genera of tower, p-ranks of tower)")
        for r in enumerate_curves(n,GMAX): print(r)
