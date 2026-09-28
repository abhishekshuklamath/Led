# Strategy for the cubic slot: is ed^[3](τ_gen) = 1 at (p,n) = (2,3)?

Setting: k algebraically closed, char 2, G = Z/8 = ⟨g⟩, K = k(s0,s1,s2), L = k(z0,z1,z2), s = ℘(z),
τ_gen = L/K. Known: ed^[1] ∈ {2,3}, ed^[2] = 2 (ed2_equals_2.pdf), ed^[3] ∈ {1,2}, ed^[4] = 1,
d_1 ∈ {3,4}, d_1^{(p')} ∈ {3,5,7,9,11}. Target: decide ed^[3]; expected value 2, i.e. d_1 = 4.

## 0. The one idea

Everything below rests on a single rigidity fact, already verified in the quadratic proof:

  (R) For any faithful G-curve C over k and any d, every K-rational divisor class of degree d on the
      twist X = τ_gen C is constant: Pic^d_{X/K}(K) = Hom_G(Spec L, Pic^d_C) = Pic^d(C)(k)^G, because
      L is rational and Pic^d_C is a torsor under an abelian variety.

The quadratic proof applied (R) to the divisor Q + σQ. The point that was missed there: Q + σQ is
just the closed point of Q. So (R) applies to the closed point of a witness of ANY degree, and the
Galois structure of K'/K is irrelevant.

## 1. Phase 1 — the degree-d rigidity lemma (no computation)

Let K'/K be a witness of degree d (ed_k(τ_gen ⊗ K') = 1), C the descent curve (Cor. 4.4), and
Q̃ ⊂ X = τ_gen C the closed point of the free K'-point, of degree exactly d (degree 1 is excluded by
ed_k(τ_gen) ≥ 2). Assume L ⊗_K K' is a field (automatic for d odd; for d = 2 it excludes K(z0), handled
by Prop. 3.9). Then Q̃ ⊗ L is a single closed point of degree d of C ⊗ L, containing no L-rational point.

Lemma A (rigidity). Let D be a k-divisor on C in the (G-invariant, constant) class of Q̃ given by (R),
and write |D| = F + |M| with F the base locus. Then:
 (a) F = 0. (F is constant, every member of |D_L| contains F_L, but Q̃_L has no constant point.)
 (b) ℓ(D) ≥ 2. (If ℓ(D) = 1 then Q̃_L = D_L is constant.)
 (c) The morphism φ_D : C → P^r, r = ℓ(D) − 1, is G-equivariant for a projective action of G on P^r
     (the class is G-invariant, so G acts projectively on L(D)).
 (d) If r = 1: the kernel of G → PGL_2(k) consists of deck transformations of the degree-d map φ_D,
     hence acts freely on a generic fibre and has order dividing d; the image has order ≤ 2 (no element
     of order 4 in PGL_2(k), Lemma 2.5(ii)); so 4 | d.
 (e) If C has genus 1: C is an ordinary elliptic curve with G acting by translation by a point P of
     order 8 (Lemma 2.5(iii) excludes supersingular); t_P acts on Pic^d by adding d·(P − O), so
     Pic^d(C)(k)^G = ∅ unless 8 | d. Hence no K-rational divisor of degree d exists at all for 8 ∤ d.

Consequences.
 • d = 2 (re-proof of ed^[2] = 2, shorter than ed2_equals_2.pdf): ℓ(D) ≤ 2; ℓ = 2 base-point free
   ⇒ r = 1 ⇒ 4 | 2, contradiction (this also shows hyperelliptic Z/8-curves do not exist); genus 1 ⇒ (e).
   No Case-A step and no passage to C/⟨g⁴⟩ is needed.
 • d = 3 (the target): ℓ(D) ∈ {2,3}. ℓ = 2 ⇒ r = 1 ⇒ 4 | 3, contradiction. ℓ = 3 ⇒ by Riemann–Roch and
   Clifford (a special divisor of degree 3 has ℓ ≤ 2) the genus is 1 ⇒ (e), contradiction.
   Hence: NO faithful Z/8-curve carries a free point of degree 3 on its twist by τ_gen.

Claim to be established: ed^[3]_k(τ_gen) = 2, d_1(τ_gen) = 4, d_1^{(p')}(τ_gen) ∈ {5,7,9,11},
D(Z) ∩ {1,2,3} = ∅ for every faithful Z/8-curve Z (in particular for U_3, with no Witt computation).

Sanity checks the argument must pass:
 – n = 2 (Z/4): cubic witnesses EXIST (line sections of E', Theorem 11.1). In Lemma A the genus-1
   case (e) must then fail to give a contradiction: for E_0 with the Witt action the fixed point ∞
   gives G-invariant classes d·∞ in every degree, and ℓ(3∞) = 3, r = 2 — consistent. The Z/8 case
   differs only because Z/8 has no faithful action on a genus-1 curve with a fixed point.
 – the degree-4 point y0 = c on U_3: r = 1, deck group Z/4 = ⟨g²⟩, 4 | 4 — consistent with (d).
 – the degree-6 points of U_3 (line sections pulled back from E_0): |6∞| = ⟨1,y0,y1⟩, r = 2 — consistent.
 – the degree-11 points: |11∞| has r = 1? No: ⟨4,6,11⟩ gives ℓ(11∞) = 4 (0,4,6,8 are ≤ 11 non-gaps
   together with 10? check: non-gaps ≤ 11 are 0,4,6,8,10,11 so ℓ = 6, r = 5); consistent with (d) not
   applying.

## 2. Phase 2 — verification (the only work before writing)

Have the argument refereed exactly as the quadratic one was, with these specific checks:
 1. (R) for Pic^3: the twist description of the Picard scheme, injectivity Pic(X) → Pic_{X/K}(K),
    and the descent of the linear equivalence Q̃_L ∼ D_L to C ⊗ L. (Same facts as in ed2_equals_2.tex
    §1, Facts on Picard schemes and base change.)
 2. Lemma A(a): the base locus of |D| is defined over k and stable under base change (L(D) = L(D − F)).
 3. Lemma A(d): deck transformations act freely on generic fibres also when φ_D is inseparable
    (use the reduced geometric generic fibre; its cardinality divides d).
 4. Lemma A(e): Aut(E,O) = {±1} for ordinary E in char 2, so an element of order 8 is a translation;
    the action of t_P on Pic^d.
 5. Non-constancy and irreducibility of Q̃_L: L ⊗_K K' is a field for [K':K] = 3.
 6. That Cor. 4.4 applies: L ⊗_K K' a field ⇒ Z may be taken an irreducible faithful G-curve.
If all pass, write it up (one page beyond the existing note; it can be inserted as Section 11.4 of
the addendum, replacing Props 11.14–11.15, and as a remark simplifying ed2_equals_2.pdf).

## 3. Phase 3 — the prime-to-2 tail after d = 3

With d_1 = 4 settled, the remaining question is d_1^{(p')} ∈ {5,7,9,11}. Lemma A turns it into a
question about G-equivariant linear systems:

  a free point of odd degree d on τ_gen C exists only if C carries a base-point-free G-stable linear
  system |D| of degree d with r = ℓ(D) − 1 ≥ 2 (r = 1 is excluded by 4 ∤ d), whose twist has a
  K-rational member with no constant component.

 • d = 5 on U_3 (genus 7): r = 2 needs a g²_5; a plane quintic has genus ≤ 6, so the map is not
   birational, and 5 is prime, so no g²_5 exists; r ≥ 3 violates Clifford. Hence 5 ∉ D(U_3).
   For general Z/8-curves C: genus ≤ 4 excluded by Riemann–Hurwitz for p-rank 0 (Cor. 11.11) but
   positive p-rank curves of genus 5 exist in the table; check whether a genus-5 Z/8-curve can carry
   an equivariant g²_5 (a plane quintic model with a Z/8 ⊂ PGL_3 action).
 • d = 7: r = 2 needs a birational plane septic model with Z/8 ⊂ PGL_3 (p_a = 15, δ = 8 for genus 7);
   r = 3 has Clifford index 1, i.e. hyperelliptic/trigonal/plane quintic, all excluded. So the question
   is whether U_3 (or another Z/8-curve) has a G-equivariant g²_7 with a K-rational irreducible member.
 • d = 9: r = 2 (plane nonic, or degree 3 onto a plane cubic), r = 3 (Clifford index 3), r = 4
   (Clifford index 1, excluded).
 • d = 11: exists on U_3 (|11∞|). So d_1^{(p')} ≤ 11 is sharp on U_3 iff 7, 9 ∉ D(U_3).
Tools: Clifford's theorem, Castelnuovo's bound, the classification of Clifford-index-1 curves, and the
structure of finite cyclic subgroups of PGL_3(k) in characteristic 2 (an element of order 8 in PGL_3
lifts to GL_3 with a unipotent part; its fixed points on P² constrain the image curve).
The uniform bound of Theorem 11.19 (quantitative Reichstein–Vistoli) is then sharpened to
5 ≤ d_1^{(p')}(τ_gen) ≤ 11 with the same mechanism deciding each odd degree.

## 4. Phase 4 — fallback if a step of Lemma A fails

If (R) or Lemma A(d) does not survive refereeing, the previous reduction still stands: a cubic witness
curve has C/⟨g⁴⟩ = E_0 and C/G = P¹, so C = C_γ (class (t,0,γ(t)), γ ∈ k(t)) and the witness is a line
section (α,β) of E' with

    s2 + Φ2(s0,s1,u,αu+β) + γ(s0 + u² + u) ∈ ℘K(u).

Then: (i) redo Prop. 11.15 (chain conditions at s2 = ∞) with the γ term, since γ can cancel poles;
(ii) the trace condition becomes s2 + R(α,β) + Tr γ(t) ∈ ℘K with Tr γ(t) a polynomial in the
elementary symmetric functions of t, t', t''; (iii) local analysis at the places over s2 = ∞ for
pole orders ≥ 2 of α, β. This is a computation, and it is the only route that does not go through (R).

## 5. What NOT to do

 – Do not split into Galois and non-Galois cubics: the closed point is K-rational in both cases,
   corestriction exists in both cases, and the resolvent term never appears (δ-functor argument).
 – Do not try to force the descent parameter into K by a first-coordinate or trace-to-a-subfield
   argument (K·F_0 = K' does not make K'/K Cartesian over a subfield; this is the error in both
   rejected notes).
 – Do not search for cubic witnesses computationally before Phase 2 is done: if Lemma A holds there is
   nothing to find, and if it fails the search must include the γ parameter.
