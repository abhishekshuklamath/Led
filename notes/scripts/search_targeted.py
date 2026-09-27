import sys, time, itertools
exec(open('search_lines.py').read().split('if __name__')[0])
def monos2(maxs01, maxs2):
    return [(i,j,l) for i in range(maxs01+1) for j in range(maxs01+1-i) for l in range(maxs2+1)]
mA = monos2(int(sys.argv[1]), int(sys.argv[2])); mB = monos2(int(sys.argv[3]), int(sys.argv[4]))
print("alpha monomials",len(mA),"beta monomials",len(mB),"pairs",2**(len(mA)+len(mB))); sys.stdout.flush()
t0=time.time(); n=0; found=0
for al in subsets(mA):
    for be in subsets(mB):
        n+=1
        ok,y=in_wp(R_eval(al,be))
        if ok: found+=1; print("FOUND alpha=",show(al)," beta=",show(be)); sys.stdout.flush()
print("tested",n,"in %.1fs"%(time.time()-t0),"found",found)
