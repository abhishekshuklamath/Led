# Search for lines w = alpha u + beta, alpha,beta in F_2[s0,s1,s2], with Tr(e_Q) = s2 + R(alpha,beta) in wp(K).
import pickle, itertools, sys, time
exec(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/f2poly.py').read())
terms = pickle.load(open('/tmp/claude-0/-home-user-Led/c4ba73c3-31cf-50a4-838b-901f57d3783c/scratchpad/x2p_terms.pkl','rb'))
# terms: exponents (s0,s1,s2,alpha,beta)
def R_eval(al, be):
    ap = {0:ONE}; bp={0:ONE}
    for i in range(1,17): ap[i]=pmul(ap[i-1],al) if i%2 else psq(ap[i//2])
    for i in range(1,5): bp[i]=pmul(bp[i-1],be) if i%2 else psq(bp[i//2])
    tot=set()
    for (i,j,l,a,b) in terms:
        t = pmul(pmul(mono(i,j,l), ap[a]), bp[b])
        tot ^= set(t)
    return frozenset(tot)
def monos(maxdeg, maxs2=None):
    out=[]
    for i in range(maxdeg+1):
        for j in range(maxdeg+1-i):
            for l in range(maxdeg+1-i-j):
                if maxs2 is None or l<=maxs2: out.append((i,j,l))
    return out
def subsets(ms):
    for r in range(len(ms)+1):
        for c in itertools.combinations(ms,r):
            yield frozenset(c)
if __name__=="__main__":
    dA=int(sys.argv[1]); dB=int(sys.argv[2])
    mA=monos(dA); mB=monos(dB)
    print("alpha monomials",len(mA),"beta monomials",len(mB), "pairs", 2**(len(mA)+len(mB)))
    t0=time.time(); n=0; found=[]
    for al in subsets(mA):
        for be in subsets(mB):
            n+=1
            x = R_eval(al,be)
            ok,y = in_wp(x)
            if ok:
                found.append((al,be,y)); print("FOUND alpha=",show(al)," beta=",show(be)); sys.stdout.flush()
    print("tested",n,"in %.1fs"%(time.time()-t0),"found",len(found))
