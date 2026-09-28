# q1 verification log (referee: sceptical check of q1_strategy.md)
Started 2026-09-28.
- Read q1_strategy.md and base paper §§2,4,5.2,6,7 (Fact 2.2, Lemmas 2.3-2.5, 4.1, Thm 4.2, Cor 4.4, Thm 6.2, Prop 7.5). Next: body_sec11.tex, ed2_analysis.md, ed4.txt.
- Read body_sec11.tex §11.3 (Thm 11.6 caseA, Cor 11.7 noquad, Prop 11.8 fft, Thm 11.9 fam, Thm 11.10 struct) and ed2_analysis.md (Lemma 1.3, Thm 2.3, Cor 2.4, §5). Next: ed4.txt.
- Read ed4.txt (Lemma 5.1, Thm 6.1, Prop 7.1). All inputs read. Beginning step-by-step check. Preliminary impression: setup, Step 1, 2, 3, 4 look sound; checking inseparable quadratic ext., effective-representative point in Step 2, descent of linear equivalence to K, cores/δ compatibility, Jac^G=0.
- Witt sanity: 2(a0,a1) = (0,a0^2) in W_2 (p=2) confirmed by ghost components; -(1,0) = (1,1). Verdict table written to q1_verify.md. Now writing detailed comments (Setup, Step 1).
- Steps 2, 3 detailed comments appended (both CORRECT; Step 3(vi) needs the descent of the linear equivalence to K, which holds by Pic(E_2) ↪ Pic_{E_2/K}(K)). Next: Step 4, completeness, by-product, overall verdict.
- Step 4(i),(ii), completeness, by-product appended: all CORRECT (4(i) needs the deg(1-α)=2 line). Next: overall verdict.
- Overall verdict written: argument CORRECT modulo routine additions (a)-(f). Report complete at q1_verify.md.
