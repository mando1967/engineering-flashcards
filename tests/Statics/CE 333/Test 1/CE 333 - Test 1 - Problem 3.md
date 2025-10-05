
# Problem #3 — Find $\mathbf F_2$ (MathJax)

**Given.** $\mathbf F_1$ has magnitude $60$ lb and is oriented $50^\circ$ **below** the horizontal.  
Its horizontal projection makes $60^\circ$ from the $+y$‑axis toward $-x$.  
The resultant is $\mathbf F_R=\langle 0,\,0,\,-100\rangle$ lb.

## Resolve $\mathbf F_1$
Let $H=60\cos 50^\circ$ be the horizontal component of $\mathbf F_1$. Then
$$
\begin{aligned}
F_{1x} &= -\,H\sin 60^\circ,\\
F_{1y} &= \phantom{-}\,H\cos 60^\circ,\\
F_{1z} &= -\,60\sin 50^\circ.
\end{aligned}
$$

Numerically
$$
\begin{aligned}
H&=60\cos 50^\circ= {H:.3f}\ \text{lb},\\
\mathbf F_1&=\langle {F1x:.3f},\ {F1y:.3f},\ {F1z:.3f}\rangle\ \text{lb}.
\end{aligned}
$$

## Compute $\mathbf F_2$
Using $\ \mathbf F_R=\mathbf F_1+\mathbf F_2$,
$$
\mathbf F_2=\mathbf F_R-\mathbf F_1=\left\langle {F2x:.3f},\ {F2y:.3f},\ {F2z:.3f}\right\rangle\ \text{lb}.
$$

Magnitude and coordinate direction angles
$$
\begin{aligned}
|\mathbf F_2|&=\sqrt{F_{2x}^2+F_{2y}^2+F_{2z}^2}={F2_mag:.3f}\ \text{lb}\ \approx\ \boxed{66\ \text{lb}},\\[4pt]
\theta_x&=\cos^{-1}\!\left(\frac{F_{2x}}{|\mathbf F_2|}\right)= {theta_x:.1f}^\circ\ \approx\ \boxed{60^\circ},\\
\theta_y&=\cos^{-1}\!\left(\frac{F_{2y}}{|\mathbf F_2|}\right)= {theta_y:.1f}^\circ\ \approx\ \boxed{107^\circ},\\
\theta_z&=\cos^{-1}\!\left(\frac{F_{2z}}{|\mathbf F_2|}\right)= {theta_z:.1f}^\circ\ \approx\ \boxed{145^\circ}.
\end{aligned}
$$

**Check.** The net $x$ and $y$ components cancel ($F_{1x}+F_{2x}\approx0$, $F_{1y}+F_{2y}\approx0$) and  
$F_{1z}+F_{2z}\approx-100$ lb as required.
