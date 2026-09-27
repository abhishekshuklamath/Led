DRAFT — in progress

# Is ed^[3](τ_gen) = 1 at (p,n) = (2,3)?  Cubic witnesses, the Witt-trace obstruction, and Riemann–Roch bounds on the prime-to-p jump degree

Setting as in the paper: k algebraically closed of characteristic 2, G = Z/8, K = k(s0,s1,s2), L = k(z0,z1,z2), s = ℘(z), τ_gen the generic Z/8-torsor. K_2 = k(s0,s1), τ_2 the generic Z/4-torsor. E' : w²+w = u(u+1)(u+s0)+s1 over K_2 (Theorem 6.2), U_n the Artin–Schreier–Witt curve ℘y = [t].

Scripts (all in this scratchpad directory):
- `witt_check.py`: re-derives (3),(4) from ghost components and prints Φ_2.
- `wittlib.py`, `cores_cubic.py`, `cores_cubic2.py`, `cores_cubic3.py`: Witt trace of a Teichmüller vector along a cubic extension, the obstruction class, cross-checks.
- `f2poly.py`, `build_R.py`, `search_lines.py`: fast F_2-polynomial search for lines satisfying the necessary condition.

## 0. Summary of conclusions (status tags)

(S1) [proved here] For p = 2, n = 2: d_1^{(p')}(τ_2) = 3. Explicitly, u a root of u³+(1+s0)u²+s0u+s1 = 0 gives a cubic separable extension F' = K_2(u) with (s0,s1) ≡ [s0+u²+u] mod ℘W_2(F'). This closes the "[open]" item in Theorem 6.2 and the p = 2 part of Question 6.4. More precisely every line w = αu+β (α,β ∈ K_2) cuts E' in a free closed point of degree exactly 3, and these are all the cubic points of E'.

(S2) [proved here] General Riemann–Roch bound: d_1^{(p')}(τ_gen) ≤ l_n(p) := 1 + (p−1)·Σ_{i=1}^{n−1} p^{2i−1}, the largest lower ramification break of U_n at ∞ (= the pole order of the reduced top Witt coordinate). Values: (2,2): 3 [sharp]; (p,2): p²−p+1; (2,3): 11; (2,4): 43. Genus: g(U_3) = 7 for p = 2 [computed two ways], g(U_2) = p(p−1)²/2. At (2,3) the odd-degree free points of τ_gen Ū_3 obtained this way have degree in {3,5,7,9,11}. Moreover, l_n is the smallest prime-to-p pole order at ∞ of any function on the affine U_n, so this is the best bound obtainable from |d·∞''|.

(S3) [proved here] Reformulation at (2,3): ed^[3](τ_gen) = 1 is witnessed on U_3 iff there are α,β ∈ K with e_Q := s2 + Φ_2(s0,s1,u,αu+β) ∈ ℘K(u), where u³+(1+s0+α²)u²+(s0+α)u+(s1+β²+β) = 0. Every such cubic is irreducible over K (a root would be a K-point of E'), so ALL cubic points of E' over K arise from lines, and the cubic points of E' are in bijection with (α,β) ∈ K².

(S4) [proved here] Necessary condition (corestriction / Witt trace): Tr_{K(u)/K}(e_Q) ∈ ℘K + ε·⟨f⟩, ε ∈ {0,1}, where f is the Artin–Schreier class of the quadratic resolvent of the cubic (ε = 0 whenever the cubic is cyclic, and ε = 0 always granted the standard fact "corestriction = Witt-vector trace"). Explicitly Tr(e_Q) = s2 + R(s0,s1,α,β) with R an explicit 67-term polynomial (script). Coordinates 0 and 1 of the Witt-trace condition hold automatically (checked symbolically), so the whole cohomological content sits in the single Artin–Schreier condition s2 + R(α,β) ∈ ℘K.

(S5) [computed] Search results: see §4 below (appended as they are obtained).

(S6) [heuristic/open] Best judgement: see §5.


## 1. The case n = 2, p = 2: d_1^{(p')}(τ_2) = 3  [proved here]

**Theorem A.** Let p = 2, K_2 = k(s0,s1), τ_2 the generic Z/4-torsor of class (s0,s1) ∈ W_2(K_2). Let u be a root of
  P(u) := u³ + (1+s0)u² + s0·u + s1  ( = u(u+1)(u+s0) + s1 ).
Then F' := K_2(u) is a separable cubic extension of K_2 and
  (s0, s1) ≡ [s0 + u² + u] = (s0+u²+u, 0)   mod ℘W_2(F').
Hence ed_k(τ_2 ⊗ F') = 1, ed^[3]'(τ_2) = 1 (prime-to-p profile) and d_1^{(p')}(τ_2) = 3.

*Proof.* (i) Irreducibility: P ∈ k(s0)[s1][u] is monic in u and of degree 1 in s1 with coefficients 1 and u(u+1)(u+s0), which are coprime in k(s0)[u]; so P is irreducible in k(s0)[u][s1] = k(s0)[s1][u], and by Gauss's lemma irreducible in k(s0)(s1)[u] = K_2[u]. An irreducible polynomial of degree 3 over a field of characteristic 2 is separable (inseparable irreducible polynomials have degree divisible by 2). So [F':K_2] = 3, separable, prime to p.
(ii) The Witt identity: by (3),(4) (re-verified from ghost components in `witt_check.py`), for h = (u,0) ∈ W_2(F'),
  (s + ℘h)_0 = s0 + u² + u,   (s + ℘h)_1 = s1 + u³ + u² + s0u² + s0u = P(u) = 0.
So s + ℘h = (t,0) = [t] with t = s0+u²+u. (Equivalently: (u,0) is an F'-point of E'° = τ_2U_2, and Theorem 6.2's last sentence applies.)
(iii) [t] ∈ W_2(k(t)) with trdeg_k k(t) ≤ 1, so ed_k(τ_2⊗F') ≤ 1 (Lemma 2.3 / definition). It is ≥ 1 because τ_2⊗F' is not split ([F':K_2] = 3 < 4, Proposition 3.2(c)). Finally d_1^{(p')} is prime to 2 and ≥ d_1(τ_2) = 2 (Proposition 6.1), so d_1^{(p')}(τ_2) = 3. ∎

**Complement (all cubic points of E').** Since Pic⁰(E')(K_2) = E'(K_2) = 0 (Theorem 6.2), every effective K_2-rational divisor D of degree 3 on E' satisfies D ~ 3∞', i.e. D is the zero divisor of a nonzero element of L(3∞') = ⟨1,u,w⟩: a line section. Lines u = c give the degree-2 fibre plus ∞'. So the cubic closed points of E' are exactly the sections by lines w = αu+β, α,β ∈ K_2; each such cubic u³+(1+s0+α²)u²+(s0+α)u+(s1+β²+β) is irreducible over K_2 because a root would be a K_2-point of E'° (excluded by Theorem 6.2); the point lies in E'° = τ_2U_2, hence is free, and gives (s0,s1) ≡ [s0+u²+u] over K_2(u). So the "group-theoretic" obstruction E'(K_2) = 0 kills degree-1 points but produces the cubic ones. In terms of Riemann–Roch this is the case n = 2 of Theorem B below: the pole order of w at ∞' is 3 = l_2(2).

Remark (odd p, n = 2). The same mechanism gives d_1^{(p')}(τ_2) ≤ p²−p+1 for every p (Theorem B with n = 2), e.g. ≤ 7 for p = 3; the lower bound remains 2 (Proposition 6.1), and Question 6.4 (degrees in [2, p−1]) is untouched by this.

## 2. Genus of U_n, and a Riemann–Roch bound on the prime-to-p jump degree  [proved here; numerics in `genus_U3.py`]

### 2.1 Ramification data of U_n → P¹ at ∞
Ū_n → P¹_t is a Z/pⁿ-cover, étale over A¹ and totally ramified at ∞ (Proposition 3.7(c)). Its Witt class is [t] with v_∞(t) = −1, reduced. By the Schmid–Witt / Brylinski conductor formula (e.g. L. Thomas, *Ramification groups in Artin–Schreier–Witt extensions*, J. Théor. Nombres Bordeaux 2005, Thm. 1.1) the upper ramification breaks of a Witt vector (a_0,…,a_{n−1}) with reduced pole orders m_i are u_j = max_{i<j} p^{j−1−i} m_i; for [t]: u_j = p^{j−1} (j = 1,…,n). Herbrand's φ (slope 1/p^{j} between the j-th and (j+1)-st break) converts to lower breaks
  l_1 = 1,  l_{j+1} = l_j + p^j(u_{j+1}−u_j) = l_j + (p−1)p^{2j−1},   so   l_n(p) = 1 + (p−1)Σ_{j=1}^{n−1} p^{2j−1}.
Direct verification at (2,3) [computed]: the tower U_3 → U_2 = E_0 → P¹_{y0} → P¹_t has layers y0²+y0 = t (conductor 1), y1²+y1 = y0³+y0² (conductor 3) and y2²+y2 = C(y0,y1) with C from (4); on E_0 (using y1² = y1+y0³+y0²) C = y0⁷+y0⁶+(y0³+y0²)y1, and C + ℘(y0²y1) = y0⁴y1 + y0³y1, of pole order 8+3 = 11 (odd, reduced). So the conductors are (1,3,11) = (l_1,l_2,l_3) and the upper breaks φ(1)=1, φ(3)=2, φ(11)=4 = (1,p,p²), as predicted.

### 2.2 Genus
Riemann–Hurwitz with the lower breaks (l_0 := −1):  2g(U_n) − 2 = −2pⁿ + Σ_{j=1}^{n} (p^{n−j+1} − 1)(l_j − l_{j−1}).
Values: g(U_2) = p(p−1)²/2 (=1 for p=2, 6 for p=3, 40 for p=5); g(U_3) = 7 at p = 2 [also from the tower: 2g−2 = 2·0 + (11+1)]; g(U_4) = 35 at p = 2; g(U_3) = 78 at p = 3.
Weierstrass semigroup of ∞ on U_3 (p=2): pole orders of y0, y1, y2+y0²y1 are 4, 6, 11; ⟨4,6,11⟩ has exactly 7 gaps {1,2,3,5,7,9,13} = g, so the semigroup at ∞ is ⟨4,6,11⟩ and the smallest ODD pole order of a function regular on the affine curve U_3 is 11.

### 2.3 The bound
**Theorem B.** For every (p,n): d_1^{(p')}(τ_gen) ≤ l_n(p) = 1 + (p−1)Σ_{j=1}^{n−1} p^{2j−1}. More precisely D(U_n) (Definition 4.3) contains an integer prime to p and ≤ l_n. Values: l_2(2) = 3 (sharp by Theorem A), l_2(p) = p²−p+1, l_3(2) = 11, l_4(2) = 43, l_3(3) = 61.

*Proof.* X := τ_gen Ū_n is a smooth projective geometrically integral K-curve with the K-point ∞'' (the twist of the G-fixed point ∞), and its free locus is X ∖ {∞''} (the non-free locus of Ū_n is {∞}, and twisting commutes with taking the G-stable open U_n). Riemann–Roch dimensions ℓ(d·∞'') are invariant under base change K → K̄, where (X,∞'') ≅ (Ū_n,∞) because the twist of a G-fixed point by any torsor is that point after base change. Hence the sequence d ↦ ℓ(d∞'') − ℓ((d−1)∞'') is that of ∞ on Ū_n: it jumps at d = l_n (the pole order of the reduced top coordinate y_{n−1}' = y_{n−1} + (polynomial in y_0,…,y_{n−2}) — the top layer U_n → U_{n−1} is y^p − y = c with reduced pole order l_n, so v_{U_n}(y) = −l_n). So there is f ∈ K(X) with pole divisor exactly l_n·∞''. For c ∈ K, the fibre divisor f⁻¹(c) = div(f−c) + l_n∞'' is an effective K-rational divisor of degree l_n supported on X ∖ {∞''} = the free locus. Its closed points have degrees e_i with Σ m_i e_i = l_n, and p ∤ l_n (l_n ≡ 1 mod p), so some closed point has degree e prime to p, e ≤ l_n, and it is free; Theorem 4.2 gives ed_k^{[e]}(τ_gen) ≤ 1 with p ∤ e. ∎

Remarks. (a) This is the best that the pencils |d·∞''| can give: on the affine U_n the coordinate ring is free over k[U_{n−1}] with basis 1,y,…,y^{p−1} (y the reduced top coordinate), and v(a_j y^j) = p·v(a_j) − j·l_n are distinct mod p, so every function on U_n with pole order prime to p has pole order ≥ l_n. Divisors not linearly equivalent to a multiple of ∞'' would need K-rational divisor classes of other degrees; the degree-p^{n−1} points (u-fibres) are ~ p^{n−1}∞'', and at (2,3) degree-2 points are exactly the open Q1.
(b) At (2,3) the fibres of the pole-order-11 function are degree-11 free divisors; degree-1 components are impossible (τ_genŪ_3(K) = {∞''}, Proposition 7.5), so each fibre contains a free closed point of odd degree in {3,5,7,9,11}. Thus d_1^{(p')}(τ_gen) ∈ {3,5,7,9,11}, and 11 ∈ D(U_3) exactly (§5.4), refining "finite" in Theorem 7.1.
(c) Caveat on the naive "odd d ≥ g+1" argument: ℓ(d∞'') ≥ 2 for d ≥ g+1 gives a non-constant f ∈ L(d∞''), but the fibres of f have degree equal to the ACTUAL pole order of f, which lies in the Weierstrass semigroup and may be even (at (2,3): g+1 = 8, and every function of pole order ≤ 10 has even pole order 4, 6, 8, 10). So "some odd d ≥ g+1" does not suffice; the correct statement is the semigroup one, and the first odd element of the semigroup ⟨4,6,11⟩ is 11.

## 3. (p,n) = (2,3): reformulation of "ed^[3] = 1 on U_3", and the cohomological constraints  [proved here]

### 3.1 Which curves can carry a cubic witness
Let F'/K be cubic (separable, WLOG by Proposition 3.6). Then L⊗_K F' is a field (F' ⊉ K_1 = K(z0) for degree reasons), so Corollary 4.4 applies: a witness is a dominant equivariant W' ⇢ C to a smooth projective irreducible curve C with faithful Z/8-action, W' the normalisation of W_3 in L⊗F'. Constraints on C:
- C ≠ P¹ and C is not a supersingular elliptic curve (Lemma 2.5(ii),(iii)).
- C an ordinary elliptic curve E with Z/8 acting by translations by a point P of order 8 (the only way to get order 8: Aut(E,O) has order 2 for j ≠ 0 and E(k)[8] ≅ Z/8 in the ordinary case): then τC is a principal homogeneous space under E of period dividing 8 (image of τ under H¹(K,Z/8) → H¹(K,E)); by Lang–Tate / Lichtenbaum, period and index of a torsor under an abelian variety have the same prime divisors, so a NONtrivial such torsor has no closed point of odd degree, and a trivial one has a K-point, i.e. a free K-point (the action is free), forcing ed_k(τ_gen) ≤ 1, false. So translation actions on ordinary elliptic curves carry NO free point of odd degree. (If the action mixes a translation with the involution [−1], its order is ≤ 4 since [−1] has order 2 and t_P∘[−1] is an involution; hence the translation case is the only genus-1 case.)
- Hence a cubic witness lives on a curve of genus ≥ 2 with a faithful Z/8-action, e.g. U_3 (g = 7), or on other such curves; Proposition 3.7(c) guarantees U_3 works at SOME prime-to-2 degree (≤ 11 by Theorem B) but says nothing degree by degree. The rest of this section is about C = Ū_3.

### 3.2 Reformulation on U_3
By Proposition 5.2(a) and (3)–(4) (script `witt_check.py`), a free F'-point of τ_genŪ_3 is h = (u,w1,w2) ∈ W_3(F') with
  w1² + w1 = u(u+1)(u+s0) + s1      (i.e. Q = (u,w1) ∈ E'(F')),
  w2² + w2 = e_Q := s2 + Φ_2(s0,s1,u,w1),
  Φ_2 = s0³u² + s0³u + s0s1u² + s0s1u + s0u⁶ + s0u⁴ + s0u²w1² + s0u²w1 + s0uw1² + s0uw1 + s1u³ + s1u² + s1w1² + s1w1 + u⁷ + u⁴ + u³w1² + u³w1 + u²w1² + u²w1 + w1³ + w1²,
and then s ≡ [t] over F', t = s0+u²+u. Conversely any such h is a free F'-point (Proposition 7.5's proof).
Cubic points of E' over K: since E'(K) = {∞'} (Lemma 4.1(ii)), Pic⁰(E')(K) = 0 and every effective K-divisor of degree 3 lies in |3∞'| = {line sections}; as in §1, the cubic points are exactly the sections by lines w = αu+β with α,β ∈ K, every such section being an irreducible cubic point (a root would be a K-point of E'°). A free F'-point with [F':K] = 3 has u ∉ K automatically: F' = K(u) since (u,w1) generates a cubic point (and if u ∈ K then t ∈ K and s ≡ [t] over F' would give s ≡ [t] over K by injectivity of res_{F'/K}, see 3.3). Therefore:

**Proposition C.** ed^[3](τ_gen) = 1 is witnessed on Ū_3 iff there are α,β ∈ K = k(s0,s1,s2) such that, for u a root of
  u³ + (1+s0+α²)u² + (s0+α)u + (s1+β²+β) = 0,
one has e_Q = s2 + Φ_2(s0,s1,u,αu+β) ∈ ℘K(u).
The twisted G-action (u,w1,w2) ↦ (u+1, w1+u, …), (u,w1+1,w2+w1), (w2+1) acts on the set of lines by (α,β) ↦ (α+1, α+β+1), (α,β+1) and preserves the condition (checked symbolically, `cores_cubic3.py`).

### 3.3 Cohomological constraints for cubic F'/K
(a) res_{F'/K}: H¹(K,Z/8) → H¹(F',Z/8) is injective and cores_{F'/K} is surjective, since cores∘res = 3 ∈ (Z/8)^×. So, unlike the quadratic case (Proposition 7.5), inflation–restriction gives no kernel; but corestriction gives an equation: if s ≡ [t] over F' then 3s ≡ cores_{F'/K}[t], i.e.
  s ≡ 3·cores_{F'/K}[t]   in W_3(K)/℘.
(b) cores = Witt trace. The Artin–Schreier–Witt isomorphism is the connecting map of 0 → Z/8 → W_3(K_sep) →℘→ W_3(K_sep) → 0 (with H¹(K, W_3(K_sep)) = 0); corestriction is a morphism of δ-functors and on H⁰ it is the norm Σ_{g∈G_K/G_{F'}} g, i.e. the Witt-vector trace Tr_{F'/K}: W_3(F') → W_3(K), x ↦ x + x' + x'' (sum of conjugates in W_3(M), M the Galois closure). So cores_{F'/K}[t] = [t]+[t']+[t''] = (e1, e2, e1e3 + e1²e2) with e_i the elementary symmetric functions of t,t',t'' (verified from (3): `cores_cubic.py`; in general the Witt vector Σ[t_i] has ghost components the power sums Σt_i^{2^m}). Also 3x = (x0, x1+x0², x2+x1²+x0²x1). [Independently of (b): over M, s ≡ [t] ≡ [t'] ≡ [t''], so 3s − Tr[t] ∈ ker(res_{M/K}) = Hom(Gal(M/K),Z/8) ∈ {0, Z/2}; the Z/2 case would add the class V²(f) of the quadratic resolvent, f = (A³C+B³+C²)/(AB+C)² for u³+Au²+Bu+C (script `resolvent.py`; for A = 0 this is Berlekamp's B³/C²). By (b) this extra term does not occur.]
(c) Coordinates. With A = 1+s0+α², B = s0+α, C = s1+β²+β and t = s0+u²+u, the script computes e1 = s0 + A² + A, e2 = AB+B²+B+C+s0², e3 = (explicit), and d := 3s − Tr[t] has d0 = ℘(A); after subtracting ℘[A], the coordinate-1 entry is x1 = α⁸+α⁶+α⁴+α³+α²s0²+αs0+β²+β+s0⁴+s0 = ℘(α⁴+α³+αs0+β+s0²+s0) — automatically in ℘K, as it must be (it is the n = 2 statement of §1 seen through cores). After subtracting ℘V[y1], the last coordinate is
  x2' = s2 + R(s0,s1,α,β),   R an explicit polynomial (67 terms, `x2p.pkl`), and x2' ≡ Tr_{K(u)/K}(e_Q) mod ℘K (checked: the difference is ℘ of an explicit polynomial).
So the complete cohomological content of "s ≡ [t] over K(u)" is the single condition
  (N1)   Tr_{K(u)/K}(e_Q) = s2 + R(α,β) ∈ ℘K.
Reducing squares (x² ≡ x), R ≡ R_red with 53 terms (`R_red.pkl`):
  R_red = α¹¹ + s0α¹⁰ + s0α⁹ + α⁸β + s1α⁸ + s0α⁷ + α⁶β + s1α⁶ + s0α⁶ + α⁵β² + α⁵β + α⁵ + s1α⁵ + s0²α⁵ + s0α⁴β² + α⁴β + s0α⁴β + s0s1α⁴ + α³β + α³ + s0α³ + s0³α³ + s0⁴α³ + s0²α²β + s0α² + s0²s1α² + s0³α² + s0⁵α² + αβ² + s0αβ² + s0²αβ² + αβ + s0²αβ + α + s1α + s0α + s0s1α + s0²s1α + s0⁴α + s0⁵α + β³ + s1β² + s0β² + s0³β² + β + s1β + s0³β + s0⁴β + s1 + s0s1 + s0²s1 + s0³s1 + s0⁴s1.
(N1) is necessary but not sufficient (ker(cores) on H¹(F',Z/2) is large). Immediate consequences: (i) α,β ∈ K_2 = k(s0,s1) is impossible (then Tr(e_Q) = s2 + (element of K_2) has a simple pole at s2 = ∞; this is Remark 7.4's argument); so the line must involve s2. (ii) If α,β ∈ K_2[s2] then s2 + R(α,β) ∈ ℘(K_2[s2]) (integrality), and the monomial-chain test decides it exactly (`f2poly.in_wp`); in particular the s2-degree of R must be even unless deg ≤ 1.

### 3.4 A rigorous partial obstruction: lines with pole order ≤ 1 at s2 = ∞  [proved here; coefficients in `deg1_family.py`]
Let v = v_∞ be the valuation of K = K_2(s2) at s2 = ∞ (residue field K_2, v(s2) = −1), K̂ = K_2((1/s2)) the completion. For e ∈ K, e ∈ ℘K ⇒ e ∈ ℘K̂. Writing e = Σ_{i ≤ N} c_i s2^i (c_i ∈ K_2): the part with i < 0 is always in ℘K̂ (x = m + m² + m⁴ + … converges), so e ∈ ℘K̂ iff c_0 ∈ ℘K_2 and, for every odd i0 ≥ 1 with 2^J i0 the last index of the chain i0, 2i0, 4i0, … carrying a nonzero coefficient,
  (Ch_{i0})   Σ_{j=0}^{J} c_{i0 2^j}^{2^{J−j}} = 0   in K_2
(the solution y = Σ b_i s2^i of y² + y = Σ_{i>0} c_i s2^i has b_{i0} = c_{i0}, b_{2m} = c_{2m} + b_m², and must be a finite sum: b_{2^{J} i0} = 0, i.e. (Ch_{i0}); conversely these conditions make the polar part ℘-exact). In particular, if the top coefficient c_N ≠ 0 has N odd, e ∉ ℘K.

**Proposition D.** There is no line with v_∞(α) ≥ −1 and v_∞(β) ≥ −1 satisfying (N1). Hence a cubic witness on Ū_3 (if any) has a line w = αu+β with α or β of pole order ≥ 2 at s2 = ∞ (i.e. s2-degree ≥ 2).

*Proof.* Write α = Σ_{i≤1} a_i s2^i, β = Σ_{i≤1} b_i s2^i ∈ K̂ (a_i, b_i ∈ K_2). The coefficient of s2^{11} in s2 + R(α,β): R's monomials are α^{16}, α^{12}, α^{11}, s0α^{10}, s0α⁹, α⁸β, …, β⁴(s0²+1), β³, … ; using α^{2^r} = Σ a_i^{2^r} s2^{2^r i}, one checks that the only monomial that can produce s2^{11} from exponents ≤ 1 is α^{11} = α⁸α²α with (i,j,l) = (1,1,1): c_{11} = a_1^{11} (the symbolic computation confirms c_11 = a1^11, c_13 = c_14 = c_15 = 0 and c_22 = … = 0 since deg ≤ 16). The chain of 11 is {11} alone, so (Ch_11) reads a_1^{11} = 0: a_1 = 0. Then α is ∞-integral and the only monomials reaching s2-degree 3 or 6 are β³ (giving c_3 ∋ b_1³, c_6 = 0) — more precisely with a_1 = 0 the script gives c_3 = b_1³, c_6 = c_{12} = 0 — so (Ch_3) reads b_1³ = 0: b_1 = 0. Now α, β are ∞-integral, R(α,β) is ∞-integral and s2 + R has a simple pole: contradiction with (Ch_1). ∎

Note that Proposition D holds for arbitrary coefficients a_i, b_i ∈ K_2 (rational functions in s0,s1 with coefficients in k), not only F_2-polynomials, and includes rational α, β in s2 with ∞-pole order ≤ 1. For pole order ≥ 2 at ∞ the chain equations become genuinely nonlinear in the coefficients (e.g. for v(α) ≥ 0, v(β) = −2: (Ch_3) is b_2³ = c_3², with c_3 involving tail coefficients), and Laurent tails matter; we have not found a general argument.

## 4. Computations  [computed; scripts `search_lines.py`, `search_targeted.py`, `ff_test.py`]
The exact test used: α, β ∈ F_2[s0,s1,s2] (subsets of a monomial basis); s2 + R(α,β) ∈ ℘K ⟺ ∈ ℘(k[s0,s1,s2]) (integral closure) ⟺ the monomial-chain algorithm `in_wp` succeeds (top monomial must be a square, subtract ℘(√), iterate; constants are absorbed by k algebraically closed).
- α of total degree ≤ 1 (4 monomials), β of total degree ≤ 2 (10 monomials): 16384 lines, none satisfies (N1).
- α = 0, β of total degree ≤ 3 (20 monomials): 1 048 576 lines, none satisfies (N1).
(further runs appended below)
- α ∈ F_2[s0,s1] of degree ≤ 2 (6 monomials), β with s2-degree ≤ 2 and (s0,s1)-degree ≤ 1 (9 monomials): 32768 lines, none.
- α with s2-degree ≤ 1 and (s0,s1)-degree ≤ 1 (6 monomials), β as before (9): 32768 lines, none.

The finite-field specialisation test (`ff_test.py`) is available as an independent check on any candidate line, including rational α, β: specialise (s0,s1,s2) ∈ F_8³ ⊂ F_512, take the roots u ∈ F_512 of the specialised cubic, and compute the absolute trace of e_Q(u); membership e_Q ∈ ℘K(u) forces trace 0 at all points where a solution x is regular (all but a proper closed subset), whereas non-members fail at ≈ 1/2 of the points. Sanity checks: a genuine ℘-element passes 1088/1088; the lines w = 0, w = s2, w = s2u + s1 pass at 544/1088, 544/1088, 580/1088 (i.e. fail). No candidate surviving (N1) has been found, so this test has not yet been needed for a real candidate.

## 5. Interpretation, general framework, and what remains open

### 5.1 Placement in the paper's framework
- Remark 4.5: the prime-to-p profile is governed by Reichstein–Scavia Thm 10.1 through correspondences of prime-to-p degree. Theorem B makes this concrete for the generic torsor: the correspondence W_n ⇝ U_n given by a fibre of the pole-order-l_n function has degree l_n ≡ 1 (mod p) and lands in the free locus, so d_1^{(p')}(τ_gen) ≤ l_n; Proposition 3.7(b),(c) only gave finiteness.
- Theorem 6.2 / Question 6.4 (p = 2): d_1^{(p')}(τ_2) = 3 (Theorem A), so the n = 2, p = 2 profile is completely known including its prime-to-p refinement: ed^[1] = 2, ed^[2] = ed^[3] = 1 with a cubic (prime-to-2) witness, ed^[4] = 0.
- Question 6.4 (p ≥ 3): d_1^{(p')}(τ_2) ≤ p²−p+1 (Theorem B); whether degrees in [2,p−1] occur is still open, and the fibre construction cannot reach them (the smallest prime-to-p pole order at ∞ is p²−p+1 > p).
- (Q2): ed^[3](τ_gen) = 1 on Ū_3 ⟺ Proposition C. Necessary condition (N1); Proposition D and the searches of §4 give no witness. d_1^{(p')}(τ_gen) ∈ {3,5,7,9,11}.
- Prop 3.7(c) says the witness for the prime-to-p tail can be taken on Ū_n at some prime-to-p degree; degree by degree this is NOT automatic: at d = 3 the curve could a priori be another faithful Z/8-curve of genus ≥ 2 (§3.1 rules out genus ≤ 1), and the Witt-trace obstruction is specific to Ū_3.

### 5.2 Judgement on Q2  [heuristic]
Evidence against a cubic witness on Ū_3: (a) (N1) is a single Artin–Schreier condition in the infinite-dimensional F_2-space K/℘K on two "free" parameters α,β ∈ K, and in the polynomial (in s2) case it unfolds into one chain equation per odd exponent up to 16·deg α — roughly 8·deg α equations in ~2·deg α + 2 unknown K_2-coefficients, plus the residue condition c_0 ∈ ℘K_2; the n = 2 analogue (coordinate 1) is automatically satisfied for structural reasons (E' is the twist of a genus-1 curve), but coordinate 2 has no such structure: R contains the isolated term α^{11} with no companion, which is what kills all pole orders ≤ 1 (Proposition D). (b) All exact searches over F_2-polynomial lines (≈ 2.4·10⁶ lines) fail (N1). (c) Even if (N1) held, e_Q ∈ ℘K(u) is a much stronger condition (ker cores on H¹(K(u), Z/2) is huge).
Evidence for: none beyond the fact that at n = 2 every line works, and that the curve Ū_3 does carry odd-degree free points of degree ≤ 11.
Our best guess: ed^[3](τ_gen) = 2 on Ū_3, i.e. no cubic witness on the Artin–Schreier–Witt curve; whether another faithful Z/8-curve of genus ≥ 2 gives a cubic witness is a separate (harder) question, so Q2 itself stays open. The value of d_1^{(p')}(τ_gen) is in {3,5,7,9,11}; the RR mechanism gives 11 and nothing better from |d∞''|.

### 5.3 Most promising next steps
1. Prove (N1) fails for all α,β ∈ K by a complete local analysis at s2 = ∞ (leading-term/Newton-polygon analysis of the chains (Ch_{i0}) for v(α) = −a, v(β) = −b; the isolated monomials α^{11}, β³, α⁸β, α⁵β², α⁴β² s0 are the natural handles) together with the finite places (where only R contributes). If successful: "no cubic witness on Ū_3". A cheaper intermediate: settle the case v(α) ≥ 0, v(β) = −2 by a Gröbner/elimination computation over F_2[s0,s1] in the finitely many tail coefficients that enter the chains (Ch_1), (Ch_3), (Ch_5), (Ch_7).
2. To decide degree 5, 7, 9 on Ū_3: the odd-degree points of Ū_3 obtained from the pole-order-11 pencil (fibres of y2 + y0²y1 twisted) split over K into points of degrees summing to 11; compute, for a specific fibre value c ∈ K, the factorisation type over K of the degree-11 divisor (e.g. by specialisation to finite fields: the splitting type of the degree-11 polynomial in y2-coordinate) to see whether degree-3, 5, 7 or 9 free points occur generically. This is a finite computation that would pin d_1^{(p')}(τ_gen) on Ū_3 further.
3. For curves other than Ū_3: a cubic witness C must have genus ≥ 2 and a faithful Z/8-action with k(C) ⊂ L·F'; classify Z/8-curves of small genus (g = 2: Z/8 ⊂ Aut of a genus-2 curve in char 2 — the hyperelliptic involution is central, so Z/8 would act on the P¹ quotient through Z/4 or Z/8 — impossible by Lemma 2.5(ii) unless the involution is g⁴; then Z/8/⟨g⁴⟩ = Z/4 ⊂ PGL_2, again excluded; so g(C) ≥ 3) and apply the Riemann–Hurwitz constraints, as in Theorem 7.3's method with Lemma 7.2 over the cubic base change.

### 5.4 Addendum to Theorem B: exact degrees on Ū_n  [proved here modulo Hilbert irreducibility, cited]
Let H ⊂ Z_{≥0} be the Weierstrass semigroup of ∞ on Ū_n (H = ⟨4,6,11⟩ at (2,3), H = ⟨2,3⟩ at (2,2)). Then D(U_n) ⊇ H ∖ {0}. Indeed for d ∈ H there is f ∈ K(τŪ_n) with pole divisor d·∞''; K(τŪ_n) is a separable field extension of degree d of K(f) (f is a K-morphism of degree d from a geometrically integral curve; separable because it is not purely inseparable in our cases — e.g. at (2,3) the degree 11 is odd; for the general statement restrict to d prime to p or check separability), so by Hilbert's irreducibility theorem (K = k(s0,…,s_{n−1}) is Hilbertian) there are infinitely many c ∈ K for which the fibre f = c is a single closed point of degree d, lying in the free locus. Consequences: at (2,3), D(U_3) ⊇ ⟨4,6,11⟩∖{0} = {4,6,8,10,11,12,14,15,16,17,18,…} (13 is a gap) and D(U_3) ∩ {1,2,3,5,7,9} is exactly the unknown part (1 ∉ D(U_3); 2 ∈ D(U_3) ⟺ Q1 holds on Ū_3; 3 ∈ D(U_3) ⟺ Proposition C's condition holds). At (2,2): D(U_2) = Z_{≥2}. This also shows the correct degree-by-degree reading of Proposition 3.7(c): on Ū_3 the prime-to-2 degrees realised so far are exactly the odd elements ≥ 11 of ⟨4,6,11⟩ (11, 15, 17, 19, …; 13 is a Weierstrass gap) — so 3, 5, 7, 9 and 13 are the open odd degrees on Ū_3.
- α with s2-degree ≤ 1 and (s0,s1)-degree ≤ 1 (6 monomials), β with s2-degree ≤ 3 and (s0,s1)-degree ≤ 1 (12 monomials): 262144 lines, none.
