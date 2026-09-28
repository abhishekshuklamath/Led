# ed7 verification log
2026-09-28T21:44:16Z started; reading ed7.txt
21:44:30Z read ed7.txt fully; now checking citations in base paper
21:44:52Z citations: Thm8.2->6.2 OK, Prop3.10->3.9 OK, Lemma3.5->Prop3.6 OK, Prop7.2->3.4 OK, Lemma4.1(i) OK; note's '[1, Lemma 2.3(a)]' for inflation-restriction is a wrong pointer (paper's 2.3 is free-point lemma) but claim true
21:48:18Z (a) Thm 3.1 matches verified proof (thm:caseA) verbatim; judged CORRECT. Now running sympy Witt checks for Fact 2.1, 4a, candidate (f)
21:49:19Z (b) Lemma 4.2: sympy confirms 4(a0,a1,a2)=(0,0,a0^4), 2a=(0,a0^2,a1^2); order argument fine; CORRECT (typo wp(c^2) should be wp(c^4)).
21:49:19Z (c) Lemma 5.1 CORRECT (trivial). (d) Cor 5.2 WRONG: K' has trdeg 3, K(B_K) trdeg 4; K'/K algebraic not 'rational'; counterexample F0=k(s2,v_f), f=s2^3+s2^2 (genus 1, KF0=K').
21:49:19Z (e) 'P^1_{v_f}', 'unramified', 't^{-1}(u0)' meaningless: K(v_f) is algebraic over K. (f) candidate x0=s1 v_f, t=s0+wp(x0) verified by sympy: solves (6.1) with t notin K, K(t)=K', beta0=T; Prop 6.1 proof WRONG (false sentence: 's0 regular'/'single point').
21:49:19Z (h) Lemma 2.3 WRONG on genus>=1: B: y^2+xy=x^3+a6 ordinary, beta0=x (only pole O, order 2) but x notin wp k(B): w^2+w=x is the etale double cover (checked via k(x)(Y,w') inertia computation; wp(y/x)=x+a6/x^2 shows the reduction cycles). True on P^1.
21:49:19Z (i) Lemma 4.1 CORRECT; Lemma 1.4 CORRECT (s=(s0,s1,0)+V^2[s2], wp V^2=V^2 wp); Cor 1.3 needs Lemma 3.2 (given later) - FIXABLE/ok; citations OK except '[1, Lemma 2.3(a)]' mislabel. (g) Theorem 6.2 NOT proved. Writing report.
21:50:05Z report written: ed7_verify.md (sections 1-3). Verdict: Thm 6.2 not proved; Cor 5.2, Prop 6.1, Lemma 2.3 WRONG.
