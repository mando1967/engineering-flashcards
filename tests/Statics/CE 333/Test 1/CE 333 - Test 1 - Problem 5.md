
# Problem #5 — Moments of $\mathbf F$ (MathJax, KaTeX‑safe)

Use right‑handed axes. Coordinates (m) chosen to match the figure and answer key:
$$
O=(0,0,0),\quad C=(0,0,0.6),\quad B=(-0.3,\,0.8,\,0.6),\quad A=(-0.8,\,-0.3,\,0.6).
$$

Force at $B$ (N):
$$
\mathbf F=80\,\mathbf i-40\,\mathbf j-120\,\mathbf k.
$$

## 1) Moment of $\mathbf F$ about point $C$
Position vector $\mathbf r_{CB}=B-C=(-0.3,\,0.8,\,0)$.
$$
\begin{aligned}
\mathbf M_C
&=\mathbf r_{CB}\times\mathbf F\\
&=\big(0.8(-120)-0(-40)\big)\,\mathbf i
+\big(0\cdot 80-(-0.3)(-120)\big)\,\mathbf j
+\big((-0.3)(-40)-0.8(80)\big)\,\mathbf k\\
&= -96\,\mathbf i-36\,\mathbf j-52\,\mathbf k\;\mathrm{N\cdot m}.
\end{aligned}
$$

## 2) Moment of $\mathbf F$ about the $x$‑axis
Moment about $O$ uses $\mathbf r_{OB}=(-0.3,\,0.8,\,0.6)$:
$$
\begin{aligned}
\mathbf M_O&=\mathbf r_{OB}\times\mathbf F,\\
M_x&=(\mathbf M_O)_x=yF_z-zF_y=0.8(-120)-0.6(-40)=-72\ \mathrm{N\cdot m}.
\end{aligned}
$$

## 3) Moment of $\mathbf F$ about the axis $OA$
Unit vector along $OA$:
$$
\mathbf u_{OA}=\dfrac{(-0.8,\,-0.3,\,0.6)}{\sqrt{(-0.8)^2+(-0.3)^2+(0.6)^2}}\approx(-0.766,\,-0.288,\,0.575).
$$
Project $\mathbf M_O$ on $\mathbf u_{OA}$ (right‑hand rule, axis from $O$ to $A$):
$$
M_{OA}=\mathbf u_{OA}\cdot\mathbf M_O\approx-21.6\ \mathrm{N\cdot m}.
$$

---

### Final answers
$$
\boxed{\mathbf M_C=-96\,\mathbf i-36\,\mathbf j-52\,\mathbf k\ \mathrm{N\cdot m}},\qquad
\boxed{M_x=-72\ \mathrm{N\cdot m}},\qquad
\boxed{M_{OA}=-21.6\ \mathrm{N\cdot m}}.
$$
