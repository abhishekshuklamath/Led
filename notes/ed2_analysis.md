## Summary of conclusions

1. [proved here] **Case A of the collaborator's dichotomy is empty**: no quadratic witness has a descent field inside
   K (Theorem 2.3(b)) — truncating to W_2 would make the Z/4-class (s0,s1)_K one-dimensional over K, against
   ed_k(Z/4) = 2. The dichotomy itself is verified; every witness is "Case B", and Q1 cannot disprove Ledet this way.
2. [proved here] **U_3 is never a quadratic witness** (Corollary 2.4): condition (i) of Prop. 7.5 (u ∉ K) can never
   hold, because Q + σQ ∈ E'(K) = {∞'} forces σQ = −Q and u ∈ K. Algorithm 9.1 is therefore moot.
3. [proved here] **New families with ed_k(τ_gen ⊗ K(v_f)) = 2** (Theorem 3.2): f ∈ K2 + ℘K; f ∈ s2 + K2 + ℘K
   (includes K(v2), not in Thm 7.3); f ∈ k(g) + ℘K with K = K2(g); every polynomial in s2 over k(s0,s1) of degree ≤ 7.
   Tool: a "fixed-field trick" (Prop. 3.1) — Lemma 7.2 along a purely transcendental fibration whose base is fixed by
   a nontrivial group element; it reproves Theorem 7.3's quadratic cases in two lines.
4. [proved here] **Structure of a hypothetical witness** (Theorems 3.3, 3.4): C/G is dominated by the Artin–Schreier
   curves y² + y = f(a0,a1,s2) (general a), C by their pullbacks along z2 ↦ z2² + z2 + c; for polynomial f, C has
   p-rank 0, one totally ramified point, 7 ≤ g(C) ≤ deg_{s2} f − 1, and C/G = P¹ if deg ≤ 15.
5. [proved here + computed] Riemann–Hurwitz/Deuring–Shafarevich: p-rank-0 Z/8-curves have genus ≥ 7 (= g(U_3), lower
   breaks (1,3,11), upper (1,2,4)); Z/8-curves of genus ≤ 6 are ordinary elliptic with translation action or genus 5
   with p-rank 5; the faithful Z/4-action on the supersingular elliptic curve is unique (E_0, Witt action).
6. [proved here] Level 2: 𝔉_A is explicit (Prop. 4.1); the E_0-part of 𝔉 is exactly Theorem 6.2's u-fibre family
   (Prop. 4.2), i.e. E'^{(f)}(K) ≠ 0 iff f ≡ s1 + u(u+1)(u+s0); k(s0) ∩ 𝔉 = {s0} (Prop. 4.3); a corestriction
   exclusion for "constant" descents (Prop. 4.4).
7. [open] Q1 itself. Remaining candidates: f with ≥ 2 poles in s2 (the ordinary-elliptic isogeny mechanism, §5), and
   polynomial f of s2-degree ≥ 8 (ASW curves of polynomial Witt vectors with t ∈ K'∖K). Nothing found suggests d1 = 2.

# Q1 at (p,n) = (2,3): quadratic witnesses for ed^[2](τ_gen) = 1 — a research note

Setting as in the paper: k algebraically closed, char 2, G = Z/8, K = k(s0,s1,s2), L = k(z0,z1,z2), s = ℘(z),
K2 = k(s0,s1), τ2 = (s0,s1). Every separable quadratic K' = K(v_f), v_f² + v_f = f ∈ K/℘K.
Scripts (all in this scratchpad): `witt_check.py` (formulas (3),(4), Φ2), `ed2_witt.py` (negation, s ± ℘x, Thm 6.2 family),
`genus_U3.py` (g(U_3)), `rh_enum.py` → `rh_enum.out` (Riemann–Hurwitz / Deuring–Shafarevich enumeration),
and further scripts named below.

## 0. Conventions and computed Witt facts  [computed]

* (3),(4) of the paper re-verified via ghost components (`witt_check.py`).
* Negation in W_3 (p=2):  −(a0,a1,a2) = (a0, a1 + a0², a2 + a1² + a0²a1 + a0⁴).  In particular −x ≠ x, but
  {s − ℘x : x ∈ W_3(K)} = {s + ℘x : x ∈ W_3(K)} since −x ranges over W_3(K) as x does. I use s + ℘x throughout.
* s + ℘(x0,x1,x2) = (t, r1, r2) with
  t  = s0 + x0² + x0,
  r1 = s1 + x0³ + x0² + s0(x0² + x0) + x1² + x1 = s1 + x0(x0+1)(x0+s0) + ℘(x1),
  r2 = s2 + Φ2(s0,s1,x0,x1) + ℘(x2),  Φ2 as printed by `witt_check.py` (independent of x2), namely
  Φ2 = s0³(x0²+x0) + s0s1(x0²+x0) + s0(x0⁶+x0⁴) + s0(x0²+x0)(x1²+x1) + s1(x0³+x0²) + s1(x1²+x1) + x0⁷ + x0⁴
       + (x0³+x0²)(x1²+x1) + x1³ + x1².
* Check (Thm 6.2 family = b=0 part of 𝔉_A):  (s + ℘(c,x1))_1 − (c(c+1)(c+s0) + s1) = x1² + x1 ∈ ℘K.  ✓
* g(U_3) = 7  [computed, `genus_U3.py`]: on E_0 : y1²+y1 = y0³+y0² (v_∞(y0) = −2, v_∞(y1) = −3) the third-layer
  right-hand side C(y0,y1) has pole order 14; one reduction step (h = y0²y1) gives the reduced element y0³y1 + y0⁴y1
  of pole order 11. Hence the lower ramification breaks of U_3 → P¹_t at ∞ are (1,3,11), the upper breaks (1,2,4)
  (Garuti's rule u_{i+1} = max(2u_i, m_i) with m = (1,0,0)), and 2g − 2 = 2(2·1 − 2) + (11+1) = 12, g(U_3) = 7.
  Cross-check with the different formula d = Σ_{i=1}^{3} (2^i − 2^{i−1})(u_i+1) = 2 + 6 + 20 = 28, 2g−2 = −16+28 = 12 ✓.
  (Note: the weights in this formula are (p^i − p^{i−1}), increasing in i; upper breaks need not be odd — the lower
  breaks are the odd ones.)

## 1. Riemann–Hurwitz / Deuring–Shafarevich for cyclic 2^n-curves  [proved here + computed]

**Set-up.** C a smooth projective curve over k with faithful G = Z/2^n action, tower C^{(i)} := C/⟨g^{2^i}⟩,
C^{(0)} = C/G, C^{(n)} = C; each step C^{(i)} → C^{(i−1)} is an Artin–Schreier double cover. A G-orbit with inertia
of order 2^a has lower breaks l_1 < … < l_a (odd) and upper breaks u_1 < … < u_a, related by l_1 = u_1,
l_{j+1} = l_j + 2^j(u_{j+1} − u_j); Hasse–Arf makes the u_j integers and (Schmid–Garuti, cyclic p^n-extensions of a
local field of char p) u_{j+1} ≥ 2u_j [cited]. Since lower numbering restricts to subgroups and upper numbering passes
to quotients, the step i is ramified over that orbit iff i ≥ n+1−a, at 2^{n−a} points of C^{(i)}, each with break
l_{a−n+i}. Per step: 2g_i − 2 = 2(2g_{i−1} − 2) + Σ(break + 1) (Riemann–Hurwitz) and
σ_i − 1 = 2(σ_{i−1} − 1) + #(ramified points of C^{(i)}) (Deuring–Shafarevich, σ = p-rank).
For the whole cover: σ(C) − 1 = 2^n(σ(C/G) − 1) + Σ_orbits 2^n(1 − 1/e_orbit).

**Lemma 1.1 (p-rank 0).** If σ(C) = 0 then σ(C/G) = 0, there is exactly one G-orbit with nontrivial inertia, it is a
single totally ramified point, and the cover is étale elsewhere. [proved: 2^n(σ'−1) + Σ 2^n(1−1/e) = −1 forces σ' = 0
and Σ 2^n(1−1/e) = 2^n − 1, which is attained only by a single orbit with e = 2^n.]
Conversely (Deuring–Shafarevich) a Z/2^n-cover of a p-rank-0 curve totally ramified at one point and étale
elsewhere has p-rank 0.

**Lemma 1.2 (p-rank under dominant maps).** A dominant map of curves C_1 → C_2 induces a surjection
Jac(C_1) → Jac(C_2) (up to isogeny/Frobenius factors), so σ(C_2) ≤ σ(C_1) and g(C_2) ≤ g(C_1). [standard]

**Table (script `rh_enum.py`, output `rh_enum.out`; entries (g(C), g(C/G), σ(C/G), σ(C), orbits (a, lower breaks),
genera of the tower, p-ranks of the tower)); the enumeration imposes only the necessary conditions above (integrality,
nonnegativity of genus and p-rank at every level, u_{j+1} ≥ 2u_j), so it is a superset of what exists.**

Z/8, g(C) ≤ 10:
```
(1, 1, 1, 1, (), (1,1,1,1), (1,1,1,1))                       ordinary elliptic, free action (translation by 8-torsion)
(5, 1, 1, 5, ((1,(1,)),), (1,1,1,5), (1,1,1,5))               ordinary elliptic quotient, one Z/2-orbit
(7, 0, 0, 0, ((3,(1,3,11)),), (0,0,1,7), (0,0,0,0))           = U_3 type: P^1 quotient, one totally ramified point
(9, 0, 0, 0, ((3,(1,3,15)),), (0,0,1,9), (0,0,0,0))           p-rank 0, upper breaks (1,2,5)
(9, 1, 1, 5, ((1,(3,)),), …), (9,1,1,7, ((2,(1,3)),), …), (9,1,1,9, two Z/2-orbits), (9,2,1,1, free), (9,2,2,9, free)
```
Consequences [proved here]:
* (a) A faithful Z/8-curve of genus ≤ 10 with p-rank 0 has g ∈ {7, 9}, quotient P^1, a single totally ramified point,
  lower breaks (1,3,11) or (1,3,15). Its Z/4-quotient C^{(2)} is a genus-1 p-rank-0 (hence supersingular) curve and
  its Z/2-quotient C^{(1)} is P^1. In particular g(U_3) = 7 is the minimal genus of a Z/8-curve in char 2 with a
  G-fixed point, and 7 is the minimal genus of a p-rank-0 Z/8-curve.
* (b) A faithful Z/8-curve of genus ≤ 6 is an ordinary elliptic curve E with G acting by translation by a point of
  order 8 (C/G = E/⟨P⟩, étale isogeny), or has genus 5 with C/G ordinary elliptic and a single Z/2-orbit
  (p-rank 5 — so it is NOT dominated by any p-rank-0 curve).
* (c) No Z/8-curve has genus 2, 3, 4, 6, 8 (within the necessary conditions), and none of genus ≤ 10 has p-rank
  in {1,…,4} except σ = 1 (the elliptic translation case, and the g = 9, g' = 2 free case).

Z/4, g(C) ≤ 6 (same format): p-rank-0 entries are g = 1 (E_0 = U_2, breaks (1,3)), g = 2 (1,5), 3 (1,7), 4 (1,9),
5 (1,11), 5 [g' = 1, σ' = 0, breaks (1,3)], 6 (1,13), 6 (3,9), 6 [g' = 1, σ' = 0, (1,5)]; ordinary elliptic with
translation by a 4-torsion point (g = 1, free) is the only other genus-1 entry. Genus-2 Z/4-curves must have
p-rank 0 with a single totally ramified point with lower breaks (1,5) and quotient P^1.

**Lemma 1.3 (faithful Z/4-actions on the supersingular elliptic curve).** [proved here] Let E be the (unique) supersingular
elliptic curve over k, char 2. Every subgroup of Aut(E) = E(k) ⋊ Aut(E,O) isomorphic to Z/4 is conjugate (in Aut(E))
to one fixing O, and the six elements of order 4 of Aut(E,O) ≅ SL_2(F_3) form a single conjugacy class; hence, up to
isomorphism of G-curves and replacing the generator by its inverse (which lies in the same class), (E, Z/4) is
(E_0, Witt action) of Theorem 6.2.
Proof. φ = t_P ∘ α, α ∈ Aut(E,O). If α = 1, ord φ = ord P is odd (E(k)[2] = 0). If ord α = 2, i.e. α = −1, then
φ² = t_{P+αP} = t_0 = 1. So ord φ = 4 forces ord α = 4, and t_Q φ t_{−Q} = t_{(1−α)Q} α with 1 − α a nonzero isogeny,
hence surjective on E(k); choosing Q with (1−α)Q = −P conjugates φ to α. Elements of order 4 in SL_2(F_3) form one
class of size 6 (classes: 1, −1, two of order 3, two of order 6, one of order 4). ∎
(Lemma 2.5(iii) of the paper is consistent with this: no element of order 8.)

## 2. The Case A / Case B dichotomy — and Case A is empty  [proved here]

Notation. A *witness* is a quadratic K' = K(v_f), f ∈ K∖℘K, with ed_k(τ_gen ⊗ K') = 1; a *descent field* is a subfield
k ⊂ F_0 ⊂ K' with trdeg_k F_0 = 1 and a class β ∈ W_3(F_0)/℘ with s ≡ β in W_3(K')/℘ (trdeg 0 is impossible since
τ_gen ⊗ K' is non-split, [K':K] = 2 < 8, Prop. 3.2(c)). (s0,s1)_K denotes the Z/4-class (s0,s1) ∈ W_2(K)/℘, i.e.
τ_2 ⊗_{K2} K; by Lemma 4.1(i) (K = K2(s2) purely transcendental) ed_k((s0,s1)_K) = ed_k(τ_2) = 2 (Prop. 6.1).

**Lemma 2.1 (kernel of restriction).** For K'/K Galois with group Z/2 = ⟨σ⟩, ker(H¹(K,Z/8) → H¹(K',Z/8)) =
inf H¹(Z/2, Z/8) = Hom(Z/2, Z/8) ≅ Z/2, generated by the class of Ind_{Z/2}^{Z/8}(K'/K), whose Witt class is
V²(f) = (0,0,f). [inflation–restriction with trivial coefficients; V^{n−m} ↔ Z/p^m ↪ Z/p^n, paper §2.2.] Likewise at
level 2 the kernel of W_2(K)/℘ → W_2(K')/℘ is {0, (0,f)}.

**Lemma 2.2 (Lüroth for trdeg-1 subfields).** If k ⊂ F_0 ⊂ k(x_1,…,x_n) has trdeg_k F_0 = 1 then F_0 = k(t).
[F_0 is finitely generated (subfield of a f.g. extension), F_0 = k(B) for a curve B; the inclusion is a dominant
rational map A^n ⇢ B; restricting to a general line gives a nonconstant map P¹ → B̃, and a curve dominated by P¹ has
genus 0 (paper Lemma 2.5(i),(iv)), so B̃ ≅ P¹.]

**Theorem 2.3 (dichotomy; Case A is empty).** Let K' = K(v_f) be a witness with descent field F_0 and class β.
(a) (Case A would give Ledet's failure) If F_0 ⊂ K then s ≡ β + ε(0,0,f) mod ℘W_3(K) with ε ∈ {0,1}, F_0 = k(t) is
rational, and ed_k(τ_gen) ≤ trdeg_k k(t,f) ≤ 2.
(b) (Case A does not occur) F_0 ⊄ K.
(c) In all cases the truncation gives ed_k((s0,s1)_K ⊗ K') = 1: f ∈ 𝔉 := {f ∈ K/℘K : ed_k((s0,s1)_K ⊗ K(v_f)) ≤ 1}
(the value 0 is impossible: (s0,s1)_K ⊗ K' is non-split, its total space k(z0,z1,s2) having degree 4 > 2 over K).
Proof. (a) s and β lie in W_3(K)/℘ and agree over K'; Lemma 2.1 gives s − β ≡ ε(0,0,f) over K, so
s ≡ β + ε(0,0,f) = (β0, β1, β2 + εf) (formula (2)) is defined over F_0(f); Lemma 2.2 gives F_0 = k(t).
(b) Suppose F_0 ⊂ K. Truncate the congruence of (a) to W_2: since (0,0,f) truncates to 0, (s0,s1) ≡ (β0,β1) mod
℘W_2(K) with β0,β1 ∈ F_0 of trdeg 1. Hence ed_k((s0,s1)_K) ≤ 1, contradicting ed_k((s0,s1)_K) = 2.
(c) Truncation W_3 → W_2 commutes with ℘ and with base change, so s ≡ β over K' implies (s0,s1) ≡ (β0,β1) over K'. ∎

Remarks. (i) The collaborator's dichotomy is correct as stated, but its Case A is vacuous by (b): the truncation
argument is exactly the one used inside the proof of Prop. 7.5 (the "ε = 1 ⇒ K-point of E'" step), applied to an
arbitrary descent class instead of [t]. So every quadratic witness, if one exists, is a genuine Case-B witness:
its descent field is not contained in K, and it can never be turned into a counterexample to Ledet by this route.
(ii) Reformulation: "Case A for f" ⇔ ed_k((s0,s1,s2+f)_K) ≤ 1 (since s − V²f = (s0,s1,s2+f)); (b) says that the
Z/8-class (s0,s1,s2+f) over K has ed_k = 2 for every f ∈ K (it is ≥ ed of its truncation (s0,s1)_K = 2, and ≤ 2 by
the tower K(v_{s2+f})… in fact ≤ ed of τ_gen ≤ 3; the value is 2 or 3 — only the lower bound matters here).

**Corollary 2.4 (U_3 admits no quadratic witness at all).** [proved here] For every quadratic K'/K, τ_gen U_3 has no
free K'-point; i.e. s is not Teichmüller over any quadratic extension of K; δ_free(U_3) ≥ 3.
Proof. By Prop. 7.5 a free K'-point needs Q = (u,w1) ∈ E'(K') with u ∉ K. But E'(K') is an abelian group on which
σ ∈ Gal(K'/K) acts, Q + σQ is σ-invariant hence lies in E'(K) = {∞'} (Lemma 4.1(ii)), so σQ = −Q = (u, w1+1)
(negation on w² + w = cubic(u) is w ↦ w+1), whence σ(u) = u and u ∈ K. So condition (i) of Prop. 7.5 never holds. ∎
(Equivalently: E'(K') = E'^{(f)}(K) (the anti-invariant points) and every point of the quadratic twist has u ∈ K;
Remark 7.6's "points not coming from the s2-line" do not exist. The same argument at level 2 shows that the
E_0-witnesses of Theorem 6.2 are exactly the u-fibres over c ∈ K2: see §4.)

**Corollary 2.5 (K(v2)).** ed_k(τ_gen ⊗ K(v2)) = 2 (v2² + v2 = s2), and more generally ed_k(τ_gen ⊗ K(v_f)) = 2 for
f ∈ s2 + K2 + ℘K. [proved here] Proof: over K' = K(v_f), f = s2 + e, s ≡ (s0,s1,e) (as (0,0,℘v_f) ∈ ℘W_3(K')),
and K' = K2(v_f) is purely transcendental over K2, so by Lemma 4.1(i) ed_k(τ_gen ⊗ K') = ed_k((s0,s1,e)_{K2}) ≥
ed_k((s0,s1)_{K2}) = 2. ∎  (This case is not covered by Theorem 7.3.)

## 3. The fixed-field trick, and new families of quadratic extensions with ed exactly 2  [proved here]

Throughout, K' = K(v_f) with f ∉ {0, s0} + ℘K, so L' := L ⊗_K K' = L(v_f) is a field (the only quadratic subfield of
L/K is K(z0)) and, by Corollary 4.4, a witness gives a smooth projective curve C with faithful G-action and a
G-equivariant embedding k(C) ↪ L' (G acting on L' through L, fixing v_f); F_0 = k(C)^G = k(C/G) ⊂ K'.

**Proposition 3.1 (fixed-field trick).** Suppose there are a subfield M ⊂ L' and x ∈ L' with L' = M(x) purely
transcendental, such that M is fixed pointwise by some 1 ≠ h ∈ G. Then τ_gen ⊗ K' has no free K'-point on any
faithful G-curve, hence ed_k(τ_gen ⊗ K') ≥ 2. The same holds for the truncated torsor (s0,s1)_K ⊗ K' (with L'
replaced by its total space L_2(s2) ⊗_K K', G by Z/4).
Proof. Choose an integral model V = B × A¹ with k(B) = M; the fibres A¹ are geometrically integral. Lemma 7.2 applied
to V → B and the dominant rational map V ⇢ C gives: some fibre A¹ maps nonconstantly to C, so C ≅ P¹ (Lemma 2.5(i)),
impossible (Lemma 2.5(ii)); or k(C) ⊂ M ⊂ (L')^h, so h acts trivially on k(C), contradicting faithfulness. ∎

**Theorem 3.2.** ed_k(τ_gen ⊗ K(v_f)) = 2 (and f ∉ 𝔉 in case (c)) for every f in the following classes:
 (a) f ∈ K2 + ℘K = k(s0,s1) + ℘K, f ∉ ℘K  (this contains the cases K(v1), K(z0) of Theorem 7.3);
 (b) f ∈ s2 + K2 + ℘K  (Corollary 2.5; contains K(v2));
 (c) f ∈ k(g) + ℘K, f ∉ ℘K, for any g ∈ K with K = K2(g), i.e. g = (a s2 + b)/(c s2 + d), a,b,c,d ∈ K2, ad ≠ bc
     (e.g. f ∈ k(s2), f = 1/(s2 + s0 s1), f = (s0 s2 + s1)³ + 1/(s0 s2 + s1), …);
 (d) f ∈ k(s0,s1)[s2] a polynomial in s2 of degree ≤ 7, f ∉ ℘K.
Proof. Upper bound 2: Theorem 7.1. (a) If f ≡ s0, Prop. 3.9. Otherwise put M := L_2(v_f) = k(z0,z1,v_f): v_f is
algebraic over L_2 = k(z0,z1) since f ∈ K2 ⊂ L_2, so L' = k(z0,z1,z2,v_f) = M(z2) is purely transcendental over M,
and g⁴ (z ↦ z + V²(1): z2 ↦ z2+1, z0,z1,v_f fixed) fixes M. Apply Prop. 3.1. (b) Corollary 2.5.
(c) K' = F(s0,s1) with F := k(g, v_f) (s0,s1 are algebraically independent over F for degree reasons), and the total
space of (s0,s1)_K ⊗ K' is k(z0,z1,s2)(v_f) = k(z0,z1)(g,v_f) = F(z0,z1). If f ≡ s0 use Prop. 3.9. Otherwise
F(z0,z1) is a field, G/⟨g⁴⟩ = Z/4 acts on it fixing F; a faithful Z/4-curve C with k(C) ↪ F(z0,z1) equivariantly
is excluded by Prop. 3.1 with M = F (fibration B × A² → B, Lemma 7.2 twice or directly: a fibre A² dominating C
forces C = P¹). Hence ed_k((s0,s1)_K ⊗ K') = 2, and a descent of s over K' would truncate to a descent of
(s0,s1)_K ⊗ K', so ed_k(τ_gen ⊗ K') = 2. (Equivalently: (s0,s1) is the generic Z/4-torsor over the field F, and
ed_k ≥ ed_F(Z/4) ≥ ed_{F̄}(Z/4) = 2 — the argument of Prop. 3.9 — but the proof above is self-contained.)
(d) If f ∈ K2 + ℘K (e.g. degree 0, or f = s2² + s2 + e) use (a). Otherwise Theorem 3.4 below applies: a witness curve C would have p-rank 0 and
g(C) ≤ deg_{s2} f − 1 ≤ 6, contradicting Corollary 3.5 (p-rank-0 Z/8-curves have genus ≥ 7). ∎

**Theorem 3.3 (structure of Case-B witnesses).** Let K' = K(v_f) be a witness with f ∉ K2 + ℘K, C the witness curve,
C' = C/G, F_0 = k(C') ⊂ K' (F_0 ⊄ K by Theorem 2.3). Let B_f := {y² + y = f(s0,s1,s2)} (an integral 3-fold with
k(B_f) = K'), D_f its generic fibre over A²_{(s0,s1)}, i.e. the Artin–Schreier curve y² + y = f over K2 in the s2-line,
and for a ∈ k² let D_{f,a} : y² + y = f(a0,a1,s2) (a curve over k), and for b ∈ ℘_2^{-1}(a) ⊂ A²_z let
D_b : y² + y = f(a0, a1, z2² + z2 + C(b0,b1)) (the pullback of D_{f,a} along the Artin–Schreier map z2 ↦ s2 of P¹).
Then, for a in a dense open subset of A²(k):
 (1) D_{f,a} is integral and dominates C' (so g(C') ≤ g(D_{f,a}), σ(C') ≤ σ(D_{f,a}));
 (2) every irreducible component of D_b dominates C (equivariantly for the stabiliser ⟨g⁴⟩ of the component, which
     acts on D_b by z2 ↦ z2 + 1); so g(C) ≤ g(D̂) and σ(C) ≤ σ(D̂), where D̂ is the normalisation of a component
     of D_b (D̂ = D̃_b if D_b is irreducible; otherwise the components are rational and C = P¹, impossible).
Proof. D_f is geometrically integral over K2 iff f ∉ K2 + ℘K (an element of K' algebraic over K2 and not in K2
generates a constant quadratic subextension K2(v_e), forcing f ≡ e ∈ K2). Apply Lemma 7.2 to B_f → A²_s and the
dominant rational map B_f ⇢ C' (the free point's image): either k(C') ⊂ k(s0,s1) ⊂ K — excluded by Theorem 2.3(b) —
or (its proof: the generic-fibre map is dominant and spreads out) D_{f,a} ⇢ C' is dominant for general a; general
fibres are integral by openness of geometric integrality. For (2): Y_f := normalisation of A³_z ×_{A³_s} B_f has
function field L', the equivariant map Y_f ⇢ C composed with C → C' factors through Y_f → B_f ⇢ C' (the free point
is Spec L' → Spec K' → C'), and the fibre of Y_f over a is ⊔_{b ∈ ℘_2^{-1}(a)} D_b, with G permuting the four
components transitively and ⟨g⁴⟩ acting on each by z2 ↦ z2+1. Each D_b → D_{f,a} → C' is nonconstant, hence so is
D_b → C. Genus and p-rank are non-increasing under dominant maps of curves (Lemma 1.2). ∎

**Theorem 3.4 (polynomial f).** Let f ∈ k(s0,s1)[s2] with m := deg_{s2} f ≥ 1 and f ∉ K2 + ℘K. If K(v_f) is a witness
with curve C, then σ(C) = 0, C/G has p-rank 0 and genus ≤ ⌊(m−1)/2⌋, C → C/G is totally ramified at exactly one
point and étale elsewhere (Lemma 1.1), and 7 ≤ g(C) ≤ m − 1. In particular no witness exists for m ≤ 7, and for
8 ≤ m ≤ 15 a witness curve must have C/G ≅ P¹, i.e. C is the Artin–Schreier–Witt curve ℘y = β(t) of a polynomial
Witt vector β ∈ W_3(k[t]) with β0 nonconstant, and s ≡ β(t) over K' with t ∈ K'∖K.
Proof. For general a, D_{f,a}: y² + y = (polynomial of degree m in s2) has a single branch point, so
σ(D_{f,a}) = 0 (Deuring–Shafarevich) and g ≤ ⌊(m−1)/2⌋; D_b : y² + y = (polynomial of degree 2m in z2) has σ = 0 and,
after Artin–Schreier reduction to odd degree ≤ 2m−1, g(D_b) ≤ m−1. Theorem 3.3 gives σ(C) = 0, g(C) ≤ m−1,
σ(C') = 0. Lemma 1.1 and Corollary 3.5 give the rest; for C' = P¹ and the cover étale outside one point, the class
lies in H¹(A¹, Z/8) = W_3(k[t])/℘W_3(k[t]), and β0 nonconstant because s0 ∉ ℘K' (else K' = K(z0)). For g(C') = 1
(then C' = E_0 as a curve, p-rank 0) Riemann–Hurwitz gives 2g(C) − 2 ≥ 0 + 28, g(C) ≥ 15, so m ≥ 16. ∎

**Corollary 3.5 (minimal genus).** A faithful Z/8-curve of p-rank 0 in characteristic 2 has genus ≥ 7, with equality
iff C/G = P¹ and the upper breaks at the unique ramified point are (1,2,4); the ASW curve U_3 is an example (§0).
A faithful Z/4-curve of p-rank 0 has genus ≥ 1, with equality iff it is (E_0, Witt action) (Lemma 1.3).
Proof. Lemma 1.1: one totally ramified point, C/G of p-rank 0. 2g − 2 = 8(2g' − 2) + (u1+1) + 2(u2+1) + 4(u3+1)
with u1 ≥ 1, u2 ≥ 2u1 ≥ 2, u3 ≥ 2u2 ≥ 4 (Schmid–Garuti), so 2g − 2 ≥ −16 + 28 = 12. For Z/4: 2g−2 ≥ −8 + 2 + 6 = 0. ∎

Remark 3.6 (what Theorem 7.3's method really uses). Theorem 7.3's proofs for K(v1) and K(v1,v2) are special cases of
Theorem 3.3's mechanism; for quadratic f ∈ K2 the fixed-field trick (Theorem 3.2(a)) is shorter. For the quartic
tower K(v1,v2) the trick does not apply directly (g⁴ moves y' = v2 + z2), and the paper's argument is needed.

## 4. The level-2 set 𝔉  [proved here unless tagged]

Recall 𝔉 = {f ∈ K/℘K : ed_k((s0,s1)_K ⊗ K(v_f)) = 1}; by Theorem 2.3(c) every witness f lies in 𝔉, and by Theorem
2.3(b) a witness needs a descent field of the truncation that is NOT inside K. So 𝔉 splits into the level-2 Case-A
part 𝔉_A (descent field inside K) and the level-2 Case-B part; a witness f must admit a level-2 Case-B descent
(possibly in addition to Case-A descents — descent fields are not unique).

**Proposition 4.1 (level-2 Case A is explicit).** f ∈ K/℘K admits a level-2 Case-A descent (i.e. (s0,s1) ≡ β(t) over
K(v_f) with t ∈ K, β ∈ W_2(k(T))) iff
  f ≡ s1 + x0(x0+1)(x0+s0) + β1(t) mod ℘K  for some x0, t ∈ K, β0, β1 ∈ k(T) with β0(t) = s0 + x0² + x0.
Call this set 𝔉_A. In particular (β0 = T) it contains {s1 + x0(x0+1)(x0+s0) + b(s0 + x0² + x0) : x0 ∈ K, b ∈ k(T)},
which is the collaborator's family (with x = (x0,x1): (s − ℘x)_1 and (s + ℘x)_1 differ by x0⁴ + x0² ∈ ℘K, script
`ed2_witt.py`; the x1-dependence is only through ℘(x1)).
Proof. ⇐: over K' = K(v_f) put x1 := v_f + h where f = s1 + x0(x0+1)(x0+s0) + β1(t) + ℘h; by §0,
(s0,s1) + ℘(x0,x1) = (s0 + ℘x0, s1 + x0(x0+1)(x0+s0) + ℘x1) = (β0(t), β1(t)). ⇒: F_0 ⊂ K of trdeg 1 is k(t) (Lemma
2.2); (s0,s1) and β(t) agree over K', so by Lemma 2.1 (level 2) (s0,s1) ≡ β(t) + ε(0,f) over K, and ε = 1 since
ed_k((s0,s1)_K) = 2; write (s0,s1) + ℘(x0,x1) = (β0(t), β1(t) + f) and read off the coordinates. ∎

**Proposition 4.2 (the E_0-part of 𝔉 is exactly the u-fibre family).** Let 𝔉_{E0} := {f : τ_2E_0 = E' has a free
K(v_f)-point} = {f : E'(K(v_f)) ≠ {∞'}} (every affine point of E' is free). Then
  𝔉_{E0} = { s1 + u(u+1)(u+s0) : u ∈ K } + ℘K  ⊂ 𝔉_A  (the case β = (T,0), t = s0 + u² + u).
Proof. As in Corollary 2.4, every Q ∈ E'(K') satisfies σQ = −Q, so u(Q) ∈ K; then w ∈ K'∖K with w² + w = g(u) ∈ K
forces w = a + v_f, a ∈ K, and f ≡ g(u) = s1 + u(u+1)(u+s0) mod ℘K. Conversely such f gives the point (u, v_f + a). ∎
So the Mordell–Weil problem "E'^{(f)}(K) ≠ 0" of the collaborator's step (1) is solved: E'^{(f)}(K) ≅ E'(K(v_f)) is
nontrivial iff f is in this explicit family (Theorem 6.2's fibres over c = u ∈ K), and never contributes u ∉ K.

**Proposition 4.3 (f ∈ k(s0)).** For e ∈ k(s0) with e ∉ {0, s0} + ℘k(s0): ed_k(τ_2 ⊗ K2(v_e)) = 2, i.e. e ∉ 𝔉_2 :=
{e ∈ K2/℘K2 : ed_k(τ_2 ⊗ K2(v_e)) = 1}; hence k(s0) ∩ 𝔉_2 = {s0 + ℘K2} and, by Lemma 4.1(i), k(s0) ∩ 𝔉 = {s0} + ℘K.
No genus condition on D_e : v² + v = e(z0² + z0) is needed.
Proof. The total space of τ_2 ⊗ K2(v_e) is L_2(v_e) = k(z0, v_e)(z1) = M(z1), M := k(z0,v_e) (v_e is algebraic over
k(z0)); M is fixed by g² (z0 ↦ z0, z1 ↦ z1 + 1, v_e fixed), and L_2 ⊗ K2(v_e) is a field since e ≢ s0. Apply
Prop. 3.1 (with Z/4, h = g²). ∎
Remarks. (i) This is stronger than the route suggested in the task (Lemma 7.2 + Lemma 1.3 + the twist isomorphism
E'^{(e)} ≅ E' via s1 ↦ s1 + e for e ∈ k(s0)); that route only handles g(D_e) ≤ 1. The twist isomorphism does show
directly that E'^{(e)}(K2) = 0 for e ∈ k(s0), consistent with Prop. 4.2. (ii) The same trick with M = k(z0,z1,v_e),
h = g⁴ gives Theorem 3.2(a) at level 3; with M = k(z0, v_e) and the fibration k(z0,v_e)(z1, z2) it gives, for
e ∈ k(s0), ed_k(τ_gen ⊗ K(v_e)) = 2 directly (also a special case of 3.2(a)).

**Proposition 4.4 (corestriction / constant-descent exclusion).** Let M_0 ⊂ K be a subfield algebraically closed in K,
f' ∈ M_0 with f ≡ f' mod ℘K, M := M_0(v_{f'}), so K' = K(v_f) = K ⊗_{M_0} M. If s0 ∉ M_0 + ℘K (e.g. M_0 ⊂ k(s1,s2),
by the simple pole at s0 = ∞), then no descent field F_0 of (s0,s1)_K ⊗ K' (in particular none of τ_gen ⊗ K') is
contained in M.
Proof. Let (s0,s1) ≡ β over K' with β ∈ W_2(F_0)/℘ ⊂ W_2(M)/℘. Corestriction is compatible with base change
(cores_{K'/K} ∘ res_{K'/M} = res_{K/M_0} ∘ cores_{M/M_0} for the finite separable M/M_0 and K' = K ⊗_{M_0} M a field),
so cores_{K'/K}(β) = γ comes from W_2(M_0)/℘; and cores_{K'/K} res(s0,s1) = 2(s0,s1) = VF(s0,s1) = (0,s0²) ≡ (0,s0).
Thus (0,s0) ≡ (γ0,γ1) over K with γ_i ∈ M_0. γ0 ∈ ℘K ∩ M_0 = ℘M_0 (M_0 algebraically closed in K), so after subtracting
℘(h,0), h ∈ M_0, γ0 = 0 and (0, s0 + γ1) ∈ ℘W_2(K), i.e. s0 + γ1 ∈ ℘K by (5), contradicting s0 ∉ M_0 + ℘K. ∎
This is not contradictory with Case B in general (the collaborator's remark is right: cores of a class from a
σ-stable descent field only says (0,s0) descends to it, and (0,s0) = Ind(s0) already has ed 1). For M_0 = k(s2) it is
superseded by Theorem 3.2(c), which needs no hypothesis on F_0; Prop. 4.4 remains useful for M_0 = k(g) with g ∈
k(s1,s2) but K ≠ K2(g), where it excludes only descents inside M.

## 5. What a witness would have to look like; the ordinary-elliptic ("isogeny") mechanism  [partly proved, mostly open]

By Theorems 2.3 and 3.3, a witness K(v_f) (f ∉ K2 + ℘K, f not in any class of Theorem 3.2) has a faithful Z/8-curve
C with C' = C/G dominated by the Artin–Schreier curves D_{f,a} : y² + y = f(a0,a1,s2) for general a ∈ k², C dominated
by D_b (pullback along z2 ↦ z2² + z2 + c), and k(C') ⊂ K' with k(C') ⊄ K.
Write r(a) for the number of poles (on P¹_{s2}, after Artin–Schreier reduction) of f(a,s2) and m_P for their odd
reduced orders; then σ(D_{f,a}) = r − 1 and g(D_{f,a}) = Σ_P (m_P + 1)/2 − 1 (Deuring–Shafarevich, Riemann–Hurwitz).
D_b → D_{f,a} is branched only over s2 = ∞ with breaks ≤ 1, so g(D_b) ≤ 2g(D_{f,a}) + 1, σ(D_b) ≤ 2σ(D_{f,a}) + 1.

(5.1) [proved] Polynomial f (r = 1): Theorem 3.4 — C has p-rank 0, one totally ramified point, g(C) ≥ 7, deg_{s2} f ≥ 8.
(5.2) [proved] If g(D_b) ≤ 6 then by the table of §1, C is an ordinary elliptic curve with G acting by translation by a
point of order 8 (so C' = C/⟨P⟩ is ordinary elliptic and C → C' is the étale Z/8-isogeny, i.e. V³: E^{(8)} → E),
or g(C) = 5 with C' ordinary elliptic and σ(C) = 5 (needs σ(D_b) ≥ 5, so r(a) ≥ 3). In both cases C' is an ordinary
elliptic curve dominated by D_{f,a} for general a: Jac(D_{f,a}) has a FIXED ordinary elliptic isogeny factor C'.
Necessary: r(a) ≥ 2 for general a, i.e. f must have a pole in s2 other than ∞ (or no pole at ∞ and ≥ 2 finite poles).
(5.3) [proved] In the isogeny case the class of τ_gen ⊗ K' is δ(Q) for the connecting map δ: C'(K') → H¹(K',Z/8) of
0 → Z/8 → C → C' → 0 and Q ∈ C'(K') the (non-constant) point given by k(C') ⊂ K'. For n = 1 and E: y² + xy = x³ + a6
(ordinary, j = 1/a6) the substitution y = xz gives z² + z = x + a6/x², so the étale Z/2-isogeny torsor at (x,y) has
Artin–Schreier class x + a6/x²; the Z/8 version is the Witt vector of the tower E^{(8)} → E^{(4)} → E^{(2)} → E (not
computed here). Since δ is a homomorphism and s is σ-invariant, δ(Q + σQ) = 2·s = (0,0,s0²) ≡ (0,0,s0) and
δ(Q − σQ) = 0, i.e. Q − σQ ∈ image(C(K') → C'(K')). These are the constraints to exploit; I did not find a
contradiction from them alone. [open]
(5.4) [heuristic] For f ∈ k(s2) + ℘K the fibre curve D_{f,a} = D is independent of a, so rigidity (Hom(D, C') is
discrete up to translations, and A² ⇢ C' is constant) gives k(C') ⊂ k(D); Theorem 3.2(c) excludes this anyway, by a
different route. For f genuinely depending on (s0,s1) with r ≥ 2, the requirement that the family a ↦ Jac(D_{f,a})
has a constant ordinary elliptic factor is a strong, checkable condition (e.g. via the family's j-invariants when
g(D_{f,a}) = 1, i.e. f(a,s2) with two simple poles or one pole of order 3), but I have not analysed it.
(5.5) [open] For non-elliptic C (g(C) ≥ 7 when σ = 0; g(C) = 5 or ≥ 9 otherwise, table §1) nothing beyond the bounds
above is known. Note that C is dominated by D_b, which carries the ⟨g⁴⟩-action z2 ↦ z2 + 1; so C has a Z/8-action
and a compatible dominant map from a Z/2-curve — a further constraint (the ⟨g⁴⟩-action on D_b has quotient D_{f,a},
which dominates C' = C/G, consistent with C/⟨g⁴⟩ being dominated by D_{f,a}, so g(C/⟨g⁴⟩) ≤ g(D_{f,a})).

## 6. Computations (scripts in this scratchpad)

* `witt_check.py` (pre-existing): ghost-component verification of (3),(4); prints Φ2 (coordinate 2 of s + ℘(u,w1,w2)
  minus w2² + w2 + s2), independent of w2.  [computed ✓]
* `ed2_witt.py`: −(a0,a1,a2) = (a0, a1 + a0², a2 + a1² + a0²a1 + a0⁴); a + (−a) = 0 ✓; full s ± ℘x; the identity
  (s + ℘(c,x1))_1 = c(c+1)(c+s0) + s1 + ℘(x1), confirming that Theorem 6.2's u-fibre family is the β = (T,0) part of
  𝔉_A; (s − ℘x)_1 − (s + ℘x)_1 = x0⁴ + x0² ∈ ℘K.  [computed ✓]
* `genus_U3.py`: Artin–Schreier reduction on E_0 gives reduced pole order 11 for the third layer of U_3, hence
  g(U_3) = 7, lower breaks (1,3,11), upper breaks (1,2,4).  [computed ✓]
* `rh_enum.py` → `rh_enum.out`: enumeration of ramification data (tower genera and p-ranks) of faithful Z/4-curves
  with g ≤ 6 and Z/8-curves with g ≤ 10 satisfying the necessary conditions (Riemann–Hurwitz and Deuring–Shafarevich
  at every level of the tower, Hasse–Arf, u_{i+1} ≥ 2u_i). Output reproduced in §1.  [computed]
* No search for level-3 Case-A candidates was run (task item 4(e)): Theorem 2.3(b) proves there are none, for every
  u ∈ K (whether or not u depends on s2) and every β2 ∈ k(T). Likewise Algorithm 9.1 needs no execution:
  Corollary 2.4 shows U_3 has no free point over any quadratic extension.

## 7. Assessment of Q1 and next steps

What is now known about quadratic witnesses (f ∈ K∖℘K, K' = K(v_f)):
1. [proved] ed_k(τ_gen ⊗ K') = 2 for f ∈ K2 + ℘K, for f ∈ s2 + K2 + ℘K, for f ∈ k(g) + ℘K with K = K2(g), and for all
   polynomials in s2 over k(s0,s1) of degree ≤ 7. This covers the three quadratic cases of Theorem 7.3 and much more.
2. [proved] A witness is never of "Case A" type: its descent field is not inside K. So Q1 is decoupled from Ledet's
   conjecture at this degree: a positive answer to Q1 would NOT disprove Ledet via the dichotomy, and Ledet's failure
   is not what a quadratic witness would detect.
3. [proved] U_3 is never a witness curve for a quadratic extension; the E_0-part of 𝔉 is exactly the u-fibre family.
4. [proved] A witness curve C for polynomial f of degree m ≥ 8 has p-rank 0, genus in [7, m−1], one totally ramified
   point, C/G = P¹ for m ≤ 15 (so C is an ASW curve of a polynomial Witt vector β(t), t ∈ K'∖K, s ≡ β(t) over K').
5. [open] Rational f with ≥ 2 poles in s2: the ordinary-elliptic isogeny mechanism (5.2)–(5.3) is the only way to get a
   small-genus witness; whether it can occur is the main open sub-question. Polynomial f of degree ≥ 8: open.

Honest assessment. Nothing found points towards d1 = 2; every family analysed has ed exactly 2, and the structural
results (Case A empty; U_3 excluded; p-rank-0 curves need genus ≥ 7 and f of s2-degree ≥ 8) make a quadratic witness
increasingly constrained but do not exclude it. I could not prove d1 ≥ 3.

Most promising next steps.
(A) Isogeny mechanism, level 2 first: decide whether (s0,s1)_K ⊗ K(v_f) can be the étale Z/4-isogeny torsor of an
    ordinary elliptic curve. Concretely: compute the Witt class (in W_2(k(E))/℘) of the tower E^{(4)} → E^{(2)} → E
    for E: y² + xy = x³ + a6 (first coordinate x + a6/x²), and test the constraints δ(Q + σQ) ≡ (0,s0), δ(Q − σQ) = 0
    for Q ∈ E(K') non-constant. A negative answer at level 2 kills all isogeny-type level-3 witnesses (truncation).
(B) Polynomial f, m ≥ 8: use the shape s ≡ β(t), β ∈ W_3(k[t]), t ∈ K'∖K, plus σ: β(t) + β(σt) ∈ ℘W_3(K') (where σt ≠ t),
    and the Z/2-layer s0 ≡ β0(t) mod ℘K'; a valuation/pole analysis on the curve D_f over K2 (as in Remark 3.5) may
    give a general obstruction.
(C) The trdeg-2 analogue: since the descent field F_0 ⊄ K, the compositum F_0·K = K' is quadratic over K; F_0 ∩ K
    has trdeg ≤ 1; if trdeg(F_0 ∩ K) = 1 then F_0/(F_0 ∩ K) is finite — analyse whether it must be quadratic and
    σ-stable, which would make cores-type arguments (Prop. 4.4) bite.
