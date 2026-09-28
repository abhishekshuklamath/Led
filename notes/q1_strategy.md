# Proposed proof that ed^[2](τ_gen) = 2 at (p,n) = (2,3) — TO BE VERIFIED

Setting: k algebraically closed, char 2, G = Z/8 = <g>, K = k(s0,s1,s2), L = k(z0,z1,z2), s = ℘(z), τ_gen = L/K.
K_2 = k(s0,s1), (s0,s1)_K the truncated Z/4-class over K. K' = K(v_f) a separable quadratic extension, σ its involution.
Known (addendum §11.3 and the new note "The second slot..."):
 (K1) [Thm 11.6(b)] a quadratic witness K' has NO descent field F_0 ⊂ K (Case A is empty): if F_0 ⊂ K then truncation
      gives ed_k((s0,s1)_K) ≤ 1, contradicting ed_k((s0,s1)_K) = ed_k(τ_2) = 2 (Lemma 4.1(i)).
 (K2) Pic^0 of twists: for a G-curve C over k and the twist E = τC, E(K)-points and Jac-points are G-equivariant maps
      from Spec of the total space of the torsor.
 (K3) Lemma 4.1(ii): for an abelian variety A over k and F purely transcendental over k, A(F) = A(k).
 (K4) Lemma 2.5(ii): PGL_2(k) has no element of order 4 (char 2).

Claim: no quadratic witness exists; hence ed^[2](τ_gen) = 2.

Setup of a hypothetical witness: K' = K(v_f), ed_k(τ_gen ⊗ K') = 1. By Cor 4.4 there is a smooth projective curve C
with faithful G-action and a dominant G-equivariant map Spec L' → C, L' = L ⊗_K K' (a field when K' ≠ K(z0); the case
K' = K(z0) is excluded by Prop 3.9). Put B = C/G, F_0 = k(B) ⊂ K' the descent field (the map Spec K' → B is the
G-quotient of Spec L' → C; it is non-constant since it is a field embedding). Let C_2 = C/<g^4> with its Z/4-action,
E_2 = the twist of C_2 by (s0,s1)_K (over K). The <g^4>-quotient of Spec L' → C is a Z/4-equivariant map
Spec(L'^{<g^4>}) → C_2, where L'^{<g^4>} = k(z0,z1,s2)(v_f) = total space of (s0,s1)_K ⊗ K'; so it is a K'-point
Q ∈ E_2(K'). Its image in B = C_2/(Z/4) is the descent point, so Q is non-constant.

Step 1 (all K-rational degree-2 classes on E_2 are constant). Pic^2_{E_2/K}(K) = Hom_G(Spec k(z0,z1,s2), Pic^2_{C_2})
by the twist description (Fact 2.2(a)); k(z0,z1,s2) is rational and Pic^2_{C_2} is a torsor under Jac(C_2), so every
such map is constant (extends to a morphism A^3 → Pic^2, constant since A^3 is rational), with value in
Pic^2(C_2)(k)^G. Hence the class of the K-rational divisor Q + σQ on E_2 is the class of a divisor D on C_2 defined
over k (with G-invariant class). Over L_2' := k(z0,z1,s2), E_2 ⊗ L_2' ≅ C_2 ⊗ L_2', and Q + σQ ∼ D there (Pic(C_2⊗L_2')
injects into Pic_{C_2/k}(L_2') because C_2 has a k-point).

Step 2 (dichotomy). deg D = 2, g(C_2) ≥ 1 ⇒ ℓ(D) ∈ {1,2}.
 (2a) ℓ(D) = 1 ⇒ Q + σQ = D as divisors on C_2 ⊗ L_2'; D is constant (supported on k-points), so the closed point
      of Q is constant, so Spec(L_2' ⊗_K K') → C_2 is constant, so Spec K' → B is constant: contradiction.
      This applies whenever C_2 is non-hyperelliptic of genus ≥ 2 (then ℓ(D) = 1 for every degree-2 D).
 (2b) ℓ(D) = 2 ⇒ C_2 hyperelliptic of genus ≥ 2 with D ∼ the unique g^1_2, or g(C_2) = 1.

Step 3 (hyperelliptic C_2, genus ≥ 2). The g^1_2 is unique hence Z/4-stable; Z/4 → Aut(P^1) = PGL_2 has kernel ⊂ <ι>
(ι the hyperelliptic involution) and image with no element of order 4 (K4), so kernel = <g^2> = <ι>, image Z/2.
An involution in PGL_2(k), char 2, is conjugate to u ↦ u+1. So C_2 → P^1_u = C_2/<g^2> → B = P^1_t, t = u^2 + u
(hence B = P^1). The map C_2 → P^1_u is Z/4-equivariant with Z/4 acting on P^1_u through Z/4 → Z/2, u ↦ u+1; twisting
by (s0,s1)_K (which induces the Z/2-class s0) gives E_2 → τP^1_u, and τP^1_u ≅ P^1_K with K-rational coordinate
ũ = u + z0 (as in Prop 5.2(a) with n = 1). Since Q + σQ ∼ D = g^1_2 and |g^1_2| is the set of ũ-fibres, Q + σQ is the
ũ-fibre over some c ∈ P^1(K); thus ũ(Q) = c ∈ K and t(Q) = ũ^2 + ũ + s0 (+ const) ∈ K. So the descent embedding
k(B) = k(t) → K' lands in K: Case A, contradicting (K1).

Step 4 (g(C_2) = 1). Faithful Z/4 on an elliptic curve: (i) supersingular with fixed point (E_0 with Witt action,
Lemma C.2): D ∼ 2∞ (Jac(k)^G = 0 as 2-rank 0), Q + σQ ∈ |2∞'| = fibres of the K-rational coordinate ũ = y0-twisted,
so ũ(Q) ∈ K and t(Q) ∈ K: Case A, contradiction (this is Cor 11.7 + (K1)); (ii) ordinary with translation by a point
of order 4, B elliptic, C_2 → B an étale isogeny φ with kernel Z/4: the class of (s0,s1)_K ⊗ K' is δ_{K'}(Q_B) for
the connecting map δ of 0 → Z/4 → C_2 → B → 0 and Q_B ∈ B(K') the image of Q. Corestriction: δ_K(Q_B + σQ_B) =
cores res (s0,s1) = 2(s0,s1) = (0, s0^2) ≡ (0,s0) ≠ 0 in W_2(K)/℘. But Q_B + σQ_B ∈ B(K) = B(k) (K3), and δ_K of a
constant point is 0 (the fibre torsor is defined over k, split). Contradiction.

Conclusion: no witness; ed^[2](τ_gen) = 2, d_1(τ_gen) ∈ {3,4}.

Also claimed as a by-product (same norm argument at level 3): a witness whose cover C → B is étale, or of "isogeny
shape" (C, C' ordinary elliptic over k, G by translation), is impossible because C'(K) = C'(k) makes δ_K(Q+σQ) = 0 ≠ 2s.
